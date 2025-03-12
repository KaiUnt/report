from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fwt_rankings.api.client import LiveheatsClient
from fastapi.responses import FileResponse
import os
import asyncio
import logging
import subprocess
from datetime import datetime, timedelta
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from fwt_rankings.data.processors import RankingsProcessor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Pfad zur Python-Umgebung
python_executable = os.path.join(os.getcwd(), "venv", "bin", "python")

app.mount("/index", StaticFiles(directory="frontend", html=True), name="static")

# CORS Middleware hinzufügen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://report.open-faces.com"],  # Nur deine Domain erlauben
    allow_methods=["GET", "POST"],  # Erlaube nur notwendige HTTP-Methoden
    allow_headers=["Content-Type", "Authorization"],  # Nur notwendige Header erlauben
)

# Cache für Event-Daten
event_cache = {
    "data": None,
    "last_updated": None
}

# Hintergrundtask für die tägliche Aktualisierung
async def update_events_cache():
    """Holt Events und aktualisiert den Cache."""
    global event_cache
    client = LiveheatsClient()
    try:
        logger.info("Starte Aktualisierung des Event-Caches...")
        events = await client.get_future_events()
        event_cache["data"] = events
        event_cache["last_updated"] = datetime.now()
        logger.info("Event-Cache erfolgreich aktualisiert.")
    except Exception as e:
        logger.error(f"Fehler bei der Aktualisierung des Event-Caches: {e}")

async def update_events_daily_at_fixed_time():
    """Aktualisiert den Cache jeden Tag um 3:00 Uhr morgens."""
    while True:
        try:
            now = datetime.now()
            next_update = now.replace(hour=3, minute=0, second=0, microsecond=0)
            if now >= next_update:
                next_update += timedelta(days=1)

            wait_time = (next_update - now).total_seconds()
            logger.info(f"Nächste Aktualisierung des Event-Caches um: {next_update}")
            await asyncio.sleep(wait_time)

            # Aktualisiere den Cache
            await update_events_cache()
        except Exception as e:
            logger.error(f"Fehler im täglichen Aktualisierungs-Task: {e}")
            # Task wird neu gestartet
            continue

async def lifespan(app: FastAPI):
    # Initialisierung beim Start
    logger.info("Initialisiere den Event-Cache beim Start der Anwendung...")
    await update_events_cache()  # Einmaliger Start
    asyncio.create_task(update_events_daily_at_fixed_time())  # Täglichen Task starten

    yield  # App wird gestartet

    # Bereinigung beim Shutdown (falls erforderlich)
    logger.info("Anwendung wird heruntergefahren...")

@app.get("/events")
async def get_events():
    """Endpunkt für Events - prüft Cache und aktualisiert ihn bei Bedarf."""
    global event_cache
    # Prüfe, ob der Cache gültig ist
    if not event_cache["data"] or (datetime.now() - event_cache["last_updated"]).total_seconds() > 24 * 3600:
        logger.info("Cache ist veraltet oder leer. Lade Events erneut...")
        await update_events_cache()
    return {"events": event_cache["data"]}

@app.get("/generate_pdf")
async def generate_pdf(event_id: str):
    """Generiert ein PDF für ein ausgewähltes Event."""
    try:
        logger.info(f"Starte PDF-Generierung für Event-ID: {event_id}")
        script_path = os.path.join(os.path.dirname(__file__), "generate_rankings_web.py")

        os.makedirs("reports", exist_ok=True)
        subprocess.run(
            [python_executable, script_path, event_id],
            check=True
        )

        # PDF-Datei suchen
        output_dir = "reports"
        pdf_files = sorted(
            [f for f in os.listdir(output_dir) if f.endswith(".pdf")],
            key=lambda x: os.path.getmtime(os.path.join(output_dir, x)),
            reverse=True
        )

        if not pdf_files:
            raise HTTPException(status_code=404, detail="PDF konnte nicht gefunden werden.")

        # Pfad zur neuesten PDF
        pdf_path = os.path.join(output_dir, pdf_files[0])
        logger.info(f"PDF gefunden: {pdf_path}")
        return FileResponse(pdf_path, filename=os.path.basename(pdf_path))

    except Exception as e:
        logger.error(f"Fehler bei der PDF-Generierung: {e}")
        raise HTTPException(status_code=500, detail="Fehler bei der PDF-Generierung.")

@app.get("/athlete_data")
async def get_athlete_data(event_id: str):
    """Endpunkt, der die aufbereiteten Athletendaten für ein Event zurückgibt."""
    try:
        logger.info(f"Hole Athletendaten für Event-ID: {event_id}")
        
        client = LiveheatsClient()
        
        # Event-Details mit BIB Nummern holen
        event_data = await client.get_event_athletes(event_id)
        if not event_data or "event" not in event_data:
            logger.error(f"Keine Event-Daten gefunden für ID: {event_id}")
            raise HTTPException(status_code=404, detail="Event nicht gefunden")
            
        # Event-Name extrahieren
        event_name = event_data["event"]["name"]
        
        # Athlete IDs und BIB-Mapping erstellen
        bib_mapping = {}
        athlete_ids = []
        
        for division in event_data["event"]["eventDivisions"]:
            for entry in division["entries"]:
                if entry["status"] in ["confirmed", "waitlisted"]:
                    athlete = entry["athlete"]
                    athlete_id = athlete["id"]
                    athlete_ids.append(athlete_id)
                    
                    bib = entry.get("bib")
                    if bib:
                        bib_mapping[athlete_id] = bib
        
        # FWT Series IDs holen
        series_ids = await client.get_fwt_series("fwtglobal")
        
        # Rankings für Athleten abrufen
        raw_data = await client.fetch_multiple_series(series_ids, athlete_ids)
        
        if not raw_data:
            logger.error("Keine Rankings gefunden!")
            return {"event_name": event_name, "athletes": []}
            
        # Daten verarbeiten
        processor = RankingsProcessor()
        rankings_data = processor.process_rankings({"results": raw_data}, bib_mapping)
        
        # Daten in JSON-Format konvertieren
        athletes_json = []
        for athlete_data in rankings_data:
            athlete_json = {
                "id": athlete_data.athlete.id,
                "name": athlete_data.athlete.name,
                "nationality": athlete_data.athlete.nationality,
                "bib": athlete_data.athlete.bib,
                "image": athlete_data.athlete.image,
                "dob": athlete_data.athlete.dob.isoformat() if athlete_data.athlete.dob else None,
                "stats": {
                    "total_events": athlete_data.stats.total_events,
                    "total_series": athlete_data.stats.total_series,
                },
                "series_results": []
            }
            
            # Best results
            if athlete_data.stats.best_result:
                if athlete_data.stats.best_result.get('by_points'):
                    best_by_points = athlete_data.stats.best_result['by_points']
                    athlete_json["stats"]["best_result_by_points"] = {
                        "event_name": best_by_points.event_name,
                        "points": best_by_points.points,
                        "place": best_by_points.place,
                        "date": best_by_points.date.isoformat() if best_by_points.date else None
                    }
                
                if athlete_data.stats.best_result.get('by_rank'):
                    best_by_rank = athlete_data.stats.best_result['by_rank']
                    athlete_json["stats"]["best_result_by_rank"] = {
                        "event_name": best_by_rank.event_name,
                        "points": best_by_rank.points,
                        "place": best_by_rank.place,
                        "date": best_by_rank.date.isoformat() if best_by_rank.date else None
                    }
            
            # Oldest result
            if athlete_data.stats.oldest_result:
                oldest = athlete_data.stats.oldest_result
                athlete_json["stats"]["oldest_result"] = {
                    "event_name": oldest.event_name,
                    "points": oldest.points,
                    "place": oldest.place,
                    "date": oldest.date.isoformat() if oldest.date else None
                }
            
            # Best series
            if athlete_data.stats.best_series_place:
                best_series = athlete_data.stats.best_series_place
                athlete_json["stats"]["best_series"] = {
                    "series_name": best_series.series_name,
                    "series_year": best_series.series_year,
                    "place": best_series.place,
                    "points": best_series.points
                }
            
            # Best Pro/Challenger
            if athlete_data.stats.best_pro_place:
                best_pro = athlete_data.stats.best_pro_place
                athlete_json["stats"]["best_pro_series"] = {
                    "series_name": best_pro.series_name,
                    "series_year": best_pro.series_year,
                    "place": best_pro.place,
                    "points": best_pro.points
                }
            
            if athlete_data.stats.best_challenger_place:
                best_challenger = athlete_data.stats.best_challenger_place
                athlete_json["stats"]["best_challenger_series"] = {
                    "series_name": best_challenger.series_name,
                    "series_year": best_challenger.series_year,
                    "place": best_challenger.place,
                    "points": best_challenger.points
                }
            
            if athlete_data.stats.best_pro_event:
                best_pro_event = athlete_data.stats.best_pro_event
                athlete_json["stats"]["best_pro_event"] = {
                    "event_name": best_pro_event.event_name,
                    "points": best_pro_event.points,
                    "place": best_pro_event.place,
                    "date": best_pro_event.date.isoformat() if best_pro_event.date else None
                }
                
            if athlete_data.stats.best_challenger_event:
                best_challenger_event = athlete_data.stats.best_challenger_event
                athlete_json["stats"]["best_challenger_event"] = {
                    "event_name": best_challenger_event.event_name,
                    "points": best_challenger_event.points,
                    "place": best_challenger_event.place,
                    "date": best_challenger_event.date.isoformat() if best_challenger_event.date else None
                }
            
            # Series results
            for series in athlete_data.series_results:
                # Filter unwanted series
                excluded_terms = ["National Rankings", "Seeding List"]
                if any(term.lower() in series.series_name.lower() for term in excluded_terms):
                    continue
                
                series_json = {
                    "series_name": series.series_name,
                    "series_year": series.series_year,
                    "division_name": series.division_name,
                    "place": series.place,
                    "points": series.points,
                    "events": []
                }
                
                # Event results
                for event in series.results:
                    event_json = {
                        "event_name": event.event_name,
                        "date": event.date.isoformat() if event.date else None,
                        "place": event.place,
                        "points": event.points
                    }
                    series_json["events"].append(event_json)
                
                athlete_json["series_results"].append(series_json)
            
            athletes_json.append(athlete_json)
        
        # Sortieren nach BIB-Nummer
        athletes_json.sort(key=lambda x: int(x["bib"]) if x["bib"] and x["bib"].isdigit() else float('inf'))
        
        return {
            "event_name": event_name,
            "athletes": athletes_json
        }

    except Exception as e:
        logger.error(f"Fehler beim Abrufen der Athletendaten: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Interner Serverfehler")
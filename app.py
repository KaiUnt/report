from fastapi import FastAPI, HTTPException, staticfiles
from fwt_rankings.api.client import LiveheatsClient
from fastapi.responses import FileResponse
import os
import asyncio
import logging
import subprocess
from datetime import datetime, timedelta
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.mount("/", staticfiles(directory="frontend", html=True), name="static")

# CORS Middleware hinzufügen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Erlaube alle Ursprünge (für lokale Entwicklung)
    allow_methods=["*"],  # Erlaube alle Methoden
    allow_headers=["*"],  # Erlaube alle Header
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
        now = datetime.now()
        # Berechne die nächste Ausführungszeit
        next_update = now.replace(hour=3, minute=0, second=0, microsecond=0)
        if now >= next_update:
            next_update += timedelta(days=1)  # Falls die Zeit heute schon vorbei ist, auf morgen setzen
        
        # Warte bis zur nächsten Ausführungszeit
        wait_time = (next_update - now).total_seconds()
        logger.info(f"Nächste Aktualisierung des Event-Caches um: {next_update}")
        await asyncio.sleep(wait_time)

        # Aktualisiere den Cache
        await update_events_cache()

@app.get("/events")
async def get_events():
    """Endpunkt für Events - prüft Cache und aktualisiert bei Bedarf."""
    global event_cache
    # Prüfe, ob der Cache gültig ist
    if not event_cache["data"] or (datetime.now() - event_cache["last_updated"] > timedelta(hours=24)):
        logger.info("Cache ist veraltet oder leer. Aktualisiere...")
        await update_events_cache()
    return {"events": event_cache["data"]}

@app.get("/generate_pdf")
async def generate_pdf(event_id: str):
    """Generiert ein PDF für ein ausgewähltes Event."""
    try:
        logger.info(f"Starte PDF-Generierung für Event-ID: {event_id}")
        script_path = os.path.join(os.path.dirname(__file__), "generate_rankings_web.py")

        # Starte das Skript
        os.makedirs("reports", exist_ok=True)
        subprocess.run(
            ["python", script_path, event_id],
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

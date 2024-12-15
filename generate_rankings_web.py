import asyncio
import sys
from pathlib import Path
from datetime import datetime
from fwt_rankings.api.client import LiveheatsClient
from fwt_rankings.data.processors import RankingsProcessor
from fwt_rankings.pdf.generator import RankingsReportGenerator
from fwt_rankings.utils.logging import get_logger

logger = get_logger(__name__)

async def main(event_id: str):
    fwt_org_shortname = "fwtglobal"  # Der korrekte Short Name
    output_dir = "reports"
    
    # Erstelle Output-Verzeichnis falls nicht vorhanden
    Path(output_dir).mkdir(exist_ok=True)
    
    try:       
        # Client initialisieren
        client = LiveheatsClient()

        # 1. Zuerst Event-Details mit BIB Nummern holen
        event_data = await client.get_event_athletes(event_id)
        if not event_data or "event" not in event_data:
            logger.error("Keine Event-Daten gefunden!")
            return
            
        # Event-Name für Dateinamen extrahieren und säubern
        event_name = event_data["event"]["name"]
        safe_event_name = "".join(c for c in event_name if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_event_name = safe_event_name.replace(' ', '_')
        
        # Generiere Output-Dateinamen mit Timestamp und Event-Name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        output_file = f"{output_dir}/{safe_event_name}_Rankings_{timestamp}.pdf"
        
        logger.info(f"Erstelle Report für Event: {event_name}")
        
        # Erstelle Mapping: Athlete ID -> BIB Nummer
        bib_mapping = {}
        athlete_ids = []
        
        for division in event_data["event"]["eventDivisions"]:
            logger.info(f"Verarbeite Division: {division['division']['name']}")
            
            for entry in division["entries"]:
                if entry["status"] in ["confirmed", "waitlisted"]:
                    athlete = entry["athlete"]
                    athlete_id = athlete["id"]
                    athlete_ids.append(athlete_id)
                    
                    bib = entry.get("bib")
                    if bib:
                        bib_mapping[athlete_id] = bib
                        logger.info(f"Athlet gefunden: {athlete['name']} (BIB: {bib}, Status: {entry['status']})")
                    else:
                        logger.info(f"Athlet gefunden: {athlete['name']} (Status: {entry['status']})")
        
        logger.info(f"{len(athlete_ids)} Athleten gefunden")
        
        # Hole Series IDs direkt von Liveheats
        logger.info(f"Hole FWT Series IDs für Organisation: {fwt_org_shortname}")
        series_ids = await client.get_fwt_series(fwt_org_shortname)
        
        # Rankings für diese Athleten abrufen
        logger.info("Hole Rankings Daten...")
        raw_data = await client.fetch_multiple_series(series_ids, athlete_ids)
        
        if not raw_data:
            logger.error("Keine Rankings gefunden!")
            return
            
        # Daten verarbeiten
        logger.info("Verarbeite Rankings...")
        processor = RankingsProcessor()
        rankings_data = processor.process_rankings({"results": raw_data}, bib_mapping)
        
        # PDF generieren
        logger.info("Generiere PDF Report...")
        generator = RankingsReportGenerator()
        generator.generate_report(rankings_data, output_file)
        
        # Zusammenfassung
        logger.info("\nZusammenfassung:")
        logger.info(f"- Verarbeitete Series: {len(raw_data)}")
        logger.info(f"- Gefundene Athleten: {len(rankings_data)}")
        logger.info(f"- Report erstellt: {output_file}")

    except Exception as e:
        logger.error(f"Fehler beim Erstellen des Reports: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Verwendung: python generate_report.py <event_id>")
        sys.exit(1)
    
    event_id = sys.argv[1]
    asyncio.run(main(event_id))
import asyncio
from fwt_rankings.api.client import LiveheatsClient
from fwt_rankings.utils.logging import get_logger

logger = get_logger(__name__)

async def test_athlete_bibs():
    # Test Event ID
    event_id = "176499"
    
    try:
        client = LiveheatsClient()
        
        # Hole Event-Details
        event_data = await client.get_event_athletes(event_id)
        if not event_data or "event" not in event_data:
            logger.error("Keine Event-Daten gefunden!")
            return
            
        event = event_data["event"]
        logger.info(f"\nEvent: {event['name']} ({event['date']})")
        
        # Sammle und zeige Athleten mit BIB-Nummern
        athlete_count = 0
        for division in event["eventDivisions"]:
            logger.info(f"\nDivision: {division['division']['name']}")
            
            # Sortiere Entries nach BIB-Nummer
            sorted_entries = sorted(
                division["entries"],
                key=lambda x: int(x.get("bib", "999999")) if x.get("bib") and x["bib"].isdigit() else 999999
            )
            
            for entry in sorted_entries:
                if entry["status"] in ["confirmed", "waitlisted"]:
                    athlete = entry["athlete"]
                    bib = entry.get("bib", "No BIB")
                    status = entry["status"]
                    logger.info(f"BIB {bib:3} | {athlete['name']:30} | Status: {status}")
                    athlete_count += 1
        
        logger.info(f"\nGesamt Athleten gefunden: {athlete_count}")

    except Exception as e:
        logger.error(f"Fehler beim Abrufen der Daten: {e}", exc_info=True)

if __name__ == "__main__":
    asyncio.run(test_athlete_bibs())
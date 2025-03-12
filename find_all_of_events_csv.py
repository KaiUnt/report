import asyncio
import json
import csv
from fwt_rankings.api.client import LiveheatsClient
from datetime import datetime, timezone
import time
import re

async def fetch_open_faces_events_with_results():
    client = LiveheatsClient()
    start_time = time.time()
    
    print("Suche nach Open Faces Events mit Ergebnissen...")
    
    # Hole FWT-Serien IDs
    series_ids = await client.get_fwt_series("fwtglobal")
    if not series_ids:
        print("Keine FWT-Serien gefunden.")
        return
    
    # Sammle alle Events aus allen Serien (ohne Duplikate)
    all_events = {}  # Verwende ein Dictionary für schnelle Deduplizierung
    for series_id in series_ids:
        async with client.client as gql_client:
            result = await gql_client.execute(
                """
                query GetEventsBySeries($id: ID!) {
                    series(id: $id) {
                        events {
                            id
                            name
                            date
                            status
                        }
                    }
                }
                """, 
                variables={"id": series_id}
            )
            
            if result and "series" in result and "events" in result["series"]:
                for event in result["series"]["events"]:
                    # Nur Events mit "Open Faces" im Namen
                    if "Open Faces" in event['name']:
                        all_events[event['id']] = event
    
    if not all_events:
        print("Keine Open Faces Events gefunden.")
        return
    
    # Konvertiere zurück in eine Liste und sortiere nach Datum
    open_faces_events = list(all_events.values())
    open_faces_events.sort(key=lambda e: e["date"], reverse=True)
    
    print(f"Gefunden: {len(open_faces_events)} einzigartige Open Faces Events")
    
    # Liste für Events mit Ergebnissen
    events_with_results = []
    
    # Direkter GraphQL-Query für Event-Ergebnisse
    for idx, event in enumerate(open_faces_events):
        try:
            # Status-Update (alle 5 Events)
            if idx % 5 == 0:
                elapsed = time.time() - start_time
                print(f"Verarbeite Events... ({idx}/{len(open_faces_events)}) - {elapsed:.1f}s vergangen")
            
            event_date = datetime.fromisoformat(event['date'].replace('Z', '+00:00'))
            
            # GraphQL-Query für Event mit Ergebnissen
            async with client.client as gql_client:
                event_data = await gql_client.execute(
                    """
                    query GetEventWithResults($id: ID!) {
                        event(id: $id) {
                            name
                            date
                            status
                            eventDivisions {
                                division {
                                    name
                                }
                                id
                                ranking {
                                    total
                                }
                            }
                        }
                    }
                    """, 
                    variables={"id": event['id']}
                )
            
            if not event_data or "event" not in event_data:
                continue
            
            event_info = event_data["event"]
            has_results = False
            
            # Bestimme Veranstaltungstyp (Junior, FWQ oder beides)
            is_junior = "Junior" in event_info["name"] or "U-16" in event_info["name"] or "U-18" in event_info["name"]
            has_fwq = any(x in event_info["name"] for x in ["1*", "2*", "3*", "4*"])
            
            event_type = []
            if is_junior:
                event_type.append("Junior")
            if has_fwq:
                event_type.append("FWQ")
            
            # Ermittle Star-Rating
            star_rating = None
            for star in ["1*", "2*", "3*", "4*"]:
                if star in event_info["name"]:
                    star_rating = star
                    break
            
            # Prüfe, ob Ergebnisse vorhanden sind
            for division in event_info.get("eventDivisions", []):
                ranking = division.get("ranking", [])
                if ranking and len(ranking) > 0:
                    has_results = True
                    break
            
            # Nur Events mit Ergebnissen speichern
            if has_results:
                date_str = event_date.strftime("%d.%m.%Y")
                type_str = " & ".join(event_type) if event_type else "Unbekannt"
                
                # Extrahiere Location auf sicherere Weise
                location = ""
                event_name = event_info["name"]
                if "Open Faces" in event_name:
                    # Verwende reguläre Ausdrücke, um den Ort zu extrahieren
                    # Suche nach dem Text zwischen "Open Faces" und der Star-Bewertung oder dem Ende
                    match = re.search(r"Open Faces\s+(.*?)(?:(?:1\*|2\*|3\*|4\*)|\s+(?:Junior|U-\d+)|$)", event_name)
                    if match:
                        location = match.group(1).strip()
                
                events_with_results.append({
                    "id": event['id'],
                    "name": event_info["name"],
                    "date": date_str,
                    "type": type_str,
                    "rating": star_rating if star_rating else "",
                    "location": location
                })
        
        except Exception as e:
            print(f"Fehler bei Event {event['id']}: {str(e)}")
    
    # Sortiere nach Datum (neueste zuerst)
    events_with_results.sort(key=lambda e: datetime.strptime(e["date"], "%d.%m.%Y"), reverse=True)
    
    # Ergebnisse ausgeben und speichern
    print(f"\nGefunden: {len(events_with_results)} Open Faces Events mit Ergebnissen")
    
    # Ausgabe für die Konsole
    for event in events_with_results:
        print(f"{event['date']} - {event['name']} - Typ: {event['type']}")
    
    # Speichern als JSON
    with open("open_faces_events_with_results.json", "w", encoding="utf-8") as f:
        json.dump(events_with_results, f, indent=2, ensure_ascii=False)
    
    # Speichern als CSV
    with open("open_faces_events_with_results.csv", "w", newline="", encoding="utf-8") as f:
        fieldnames = ["date", "name", "type", "rating", "location"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for event in events_with_results:
            writer.writerow({field: event.get(field, "") for field in fieldnames})
    
    print(f"\nEvent-Details wurden in 'open_faces_events_with_results.json' und 'open_faces_events_with_results.csv' gespeichert")
    
    # Zeige Statistiken
    total_time = time.time() - start_time
    print(f"Ausführungszeit: {total_time:.1f} Sekunden")

if __name__ == "__main__":
    asyncio.run(fetch_open_faces_events_with_results())
import asyncio
from aiohttp import ClientSession
import re
from datetime import datetime, timezone

# GraphQL Endpoint
GRAPHQL_URL = "https://liveheats.com/api/graphql"

# Query für Serien einer Organisation
GET_ORGANISATION_SERIES = """
query GetOrganisationSeries($shortName: String!) {
    organisationByShortName(shortName: $shortName) {
        series {
            id
            name
        }
    }
}
"""

# Query für Events einer Serie
GET_EVENTS_BY_SERIES = """
query GetEventsBySeries($id: ID!) {
    series(id: $id) {
        events {
            id
            name
            date
        }
    }
}
"""

async def fetch_series(short_name: str, session: ClientSession) -> list:
    """Fetch series from an organisation."""
    try:
        response = await session.post(
            GRAPHQL_URL,
            json={
                "query": GET_ORGANISATION_SERIES,
                "variables": {"shortName": short_name},
            },
        )
        if response.status != 200:
            print(f"HTTP-Fehler: {response.status}")
            print(await response.text())
            return []

        data = await response.json()
        if "errors" in data:
            print(f"GraphQL-Fehler: {data['errors']}")
            return []

        series = data.get("data", {}).get("organisationByShortName", {}).get("series", [])
        return series
    except Exception as e:
        print(f"Fehler beim Abrufen der Serien: {e}")
        return []

async def fetch_events(series_id: str, session: ClientSession) -> list:
    """Fetch events from a series."""
    try:
        response = await session.post(
            GRAPHQL_URL,
            json={
                "query": GET_EVENTS_BY_SERIES,
                "variables": {"id": series_id},
            },
        )
        if response.status != 200:
            print(f"HTTP-Fehler: {response.status}")
            print(await response.text())
            return []

        data = await response.json()
        if "errors" in data:
            print(f"GraphQL-Fehler: {data['errors']}")
            return []

        events = data.get("data", {}).get("series", {}).get("events", [])
        return events
    except Exception as e:
        print(f"Fehler beim Abrufen der Events: {e}")
        return []

async def test_future_events():
    async with ClientSession() as session:
        # Schritt 1: Serien abrufen
        short_name = "fwtglobal"
        series = await fetch_series(short_name, session)

        if not series:
            print("Keine Serien gefunden.")
            return

        print(f"{len(series)} Serien gefunden.")

        # Schritt 2: Serien filtern (Jahre 2024–2029)
        years = range(2024, 2030)
        filtered_series = [
            s for s in series if re.search(r'\b(202[4-9])\b', s["name"])
            and int(re.search(r'\b(202[4-9])\b', s["name"]).group(1)) in years
        ]

        print(f"{len(filtered_series)} Serien in den Jahren 2024–2029 gefunden.")

        # Schritt 3: Events für die gefilterten Serien abrufen
        all_events = []
        for s in filtered_series:
            series_events = await fetch_events(s["id"], session)
            all_events.extend(series_events)

        # Schritt 4: Events nach Datum filtern
        now = datetime.now(timezone.utc)
        future_events = [
            event for event in all_events
            if datetime.fromisoformat(event["date"].replace("Z", "+00:00")) >= now
        ]

        # Schritt 5: Deduplizieren basierend auf der Event-ID
        unique_events = {event["id"]: event for event in future_events}.values()

        print(f"{len(unique_events)} eindeutige zukünftige Events gefunden:")
        for event in unique_events:
            print(f"- {event['name']} am {event['date']}")

# Starte das Testskript
if __name__ == "__main__":
    asyncio.run(test_future_events())

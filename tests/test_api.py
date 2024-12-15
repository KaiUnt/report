import asyncio
import sys 
import os
from fwt_rankings.api.client import LiveheatsClient
print(f"Client.py wird geladen von: {os.path.abspath(__file__)}")


async def debug_client_methods():
    client = LiveheatsClient()
    print(dir(client))  # Zeigt alle verfügbaren Methoden an

async def test_get_future_events():
    client = LiveheatsClient()
    print("Starte Test für get_future_events...")

    try:
        # Rufe die zukünftigen Events ab
        future_events = await client.get_future_events()

        if not future_events:
            print("Keine zukünftigen Events gefunden.")
        else:
            print(f"{len(future_events)} zukünftige Events gefunden:")
            for event in future_events:
                print(f"- {event['name']} am {event['date']}")
    except Exception as e:
        print(f"Test fehlgeschlagen: {e}")

if __name__ == "__main__":
    asyncio.run(debug_client_methods())
    asyncio.run(test_get_future_events())

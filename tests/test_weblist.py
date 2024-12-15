import asyncio
import sys 
import os
import importlib
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import fwt_rankings.api.client
importlib.reload(fwt_rankings.api.client)
from fwt_rankings.api.client import LiveheatsClient
print(f"Client.py wird geladen von: {os.path.abspath(__file__)}")
print(f"LiveheatsClient Modulpfad: {LiveheatsClient.__module__}")
print(f"Client.py wird geladen von: {os.path.abspath(sys.modules[LiveheatsClient.__module__].__file__)}")

client = LiveheatsClient()
print(dir(client))

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

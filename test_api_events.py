import asyncio
from fwt_rankings.api.client import LiveheatsClient

async def test_fetch_events():
    client = LiveheatsClient()
    events = await client.get_future_events()
    for event in events:
        print(f"{event['id']}: {event['name']} ({event['date']})")

if __name__ == "__main__":
    asyncio.run(test_fetch_events())

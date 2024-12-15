# test_live_scores.py

import asyncio
import sys
from typing import Dict, Optional
from fwt_rankings.api.client import GraphQLClient
from fwt_rankings.utils.logging import get_logger

logger = get_logger(__name__)

class LiveScoresTest:
    def __init__(self):
        self.client = GraphQLClient()
        self.current_heats_query = """
        query event($id: ID!) {
            event(id: $id) {
                name
                currentHeats {
                    competitors {
                        athlete {
                            id
                            name
                        }
                        result {
                            place
                            total
                            rides
                            needs
                        }
                    }
                    round
                    roundPosition
                    startTime
                    endTime
                }
                eventDivisions {
                    division {
                        name
                    }
                    status
                }
            }
        }
        """

    async def test_current_heats(self, event_id: str) -> Optional[Dict]:
        """Test current heats query for a specific event."""
        async with self.client as client:
            try:
                logger.info(f"Testing current heats query for event ID: {event_id}")
                result = await client.execute(
                    self.current_heats_query,
                    {"id": event_id}
                )

                if not result:
                    logger.error("No data received from API")
                    return None

                if "event" not in result:
                    logger.error("No event data in response")
                    return None

                event = result["event"]
                logger.info(f"Event Name: {event['name']}")

                # Log divisions info
                logger.info("\nDivisions:")
                for division in event.get("eventDivisions", []):
                    div_name = division["division"]["name"]
                    div_status = division["status"]
                    logger.info(f"- {div_name} (Status: {div_status})")

                # Log current heats info
                current_heats = event.get("currentHeats", [])
                if not current_heats:
                    logger.info("No current heats running")
                else:
                    logger.info(f"\nFound {len(current_heats)} current heat(s)")
                    for heat in current_heats:
                        logger.info(f"\nRound: {heat['round']}, Position: {heat['roundPosition']}")
                        logger.info(f"Start Time: {heat['startTime']}")
                        logger.info(f"End Time: {heat['endTime']}")
                        
                        for competitor in heat.get("competitors", []):
                            athlete = competitor["athlete"]
                            result = competitor["result"]
                            logger.info(
                                f"Athlete: {athlete['name']}"
                                f" | Total: {result['total']}"
                                f" | Place: {result['place']}"
                                f" | Needs: {result['needs']}"
                            )

                return result

            except Exception as e:
                logger.error(f"Error testing current heats: {e}")
                return None

async def main():
    if len(sys.argv) != 2:
        print("Usage: python test_live_scores.py <event_id>")
        sys.exit(1)

    event_id = sys.argv[1]
    tester = LiveScoresTest()
    await tester.test_current_heats(event_id)

if __name__ == "__main__":
    asyncio.run(main())
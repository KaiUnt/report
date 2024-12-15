import asyncio
from pathlib import Path
from datetime import datetime
from fwt_rankings.api.client import LiveheatsClient
from fwt_rankings.data.processors import RankingsProcessor
from fwt_rankings.pdf.generator import RankingsReportGenerator
from fwt_rankings.utils.logging import get_logger

logger = get_logger(__name__)

async def main():
    # Konfiguration
    event_id = "286586"
    output_dir = "reports"
    Path(output_dir).mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_file = f"{output_dir}/test_report_{timestamp}.pdf"

    client = LiveheatsClient()
    event_data = await client.get_event_athletes(event_id)
    
    athlete_ids = []
    for division in event_data["event"]["eventDivisions"]:
        for entry in division["entries"]:
            if entry["status"] in ["confirmed", "waitlisted"]:
                athlete_ids.append(entry["athlete"]["id"])

    series_ids = ["35763"]  # Test mit einer Series ID für schnelleren Test
    raw_data = await client.fetch_multiple_series(series_ids, athlete_ids)
    
    processor = RankingsProcessor()
    rankings_data = processor.process_rankings({"results": raw_data})
    
    generator = RankingsReportGenerator()
    generator.generate_report(rankings_data, output_file)

if __name__ == "__main__":
    asyncio.run(main())
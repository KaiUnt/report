import os

class ModuleContentCreator:
    def __init__(self, base_path: str = "fwt_rankings"):
        self.base_path = os.path.join(base_path, "fwt_rankings")

    def create_file(self, path: str, content: str):
        """Create a file with the given content."""
        # Ensure directory exists
        os.makedirs(os.path.dirname(path), exist_ok=True)
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
            
    def create_all_modules(self):
        """Create all module files with their content."""
        # API Module Files
        self.create_api_files()
        
        # Data Module Files
        self.create_data_files()
        
        # PDF Module Files
        self.create_pdf_files()
        
        # Utils Module Files
        self.create_utils_files()
        
        print("All module files created successfully!")

    def create_api_files(self):
        """Create API module files."""
        # client.py
        client_content = '''
import aiohttp
import asyncio
from typing import Dict, Optional, Any
from ..utils.logging import get_logger

logger = get_logger(__name__)

class GraphQLClient:
    def __init__(self, base_url: str = "https://liveheats.com/api/graphql"):
        self.base_url = base_url
        self._session: Optional[aiohttp.ClientSession] = None
        
    async def __aenter__(self):
        self._session = aiohttp.ClientSession()
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._session:
            await self._session.close()
            
    async def execute(self, query: str, variables: Dict[str, Any] = None) -> Dict:
        if not self._session:
            raise RuntimeError("Client not initialized. Use 'async with' context manager.")
            
        try:
            async with self._session.post(
                self.base_url,
                json={
                    "query": query,
                    "variables": variables or {}
                }
            ) as response:
                if response.status != 200:
                    logger.error(f"HTTP Error {response.status}")
                    return None
                    
                data = await response.json()
                if "errors" in data:
                    logger.error(f"GraphQL Error: {data['errors']}")
                    return None
                    
                return data.get("data")
                
        except Exception as e:
            logger.error(f"Request failed: {str(e)}")
            return None

class LiveheatsClient:
    def __init__(self):
        self.client = GraphQLClient()
        
    async def get_series_rankings(self, series_id: str, division_id: str) -> Dict:
        from .queries import GET_SERIES_RANKINGS
        
        async with self.client as client:
            return await client.execute(
                GET_SERIES_RANKINGS,
                {"id": series_id, "divisionId": division_id}
            )
            
    async def fetch_multiple_series(self, series_ids: list, athlete_ids: list) -> list:
        async with self.client as client:
            tasks = [
                self._process_series(client, series_id, athlete_ids)
                for series_id in series_ids
            ]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            return [r for r in results if r is not None and not isinstance(r, Exception)]
'''
        self.create_file(os.path.join(self.base_path, "api", "client.py"), client_content)

        # queries.py
        queries_content = '''
# GraphQL Queries
GET_SERIES_RANKINGS = """
query GetSeriesRankings($id: ID!, $divisionId: ID!) {
    series(id: $id) {
        rankings(divisionId: $divisionId) {
            athlete {
                id
                name
                dob
                nationality
                image
            }
            place
            points
            results {
                place
                points
                eventDivision {
                    event {
                        name
                        date
                    }
                }
            }
        }
    }
}
"""

GET_DIVISIONS = """
query GetDivisions($id: ID!) {
    series(id: $id) {
        name
        rankingsDivisions {
            id
            name
        }
    }
}
"""
'''
        self.create_file(os.path.join(self.base_path, "api", "queries.py"), queries_content)

    def create_data_files(self):
        """Create Data module files."""
        # models.py
        models_content = '''
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Dict

@dataclass
class Athlete:
    id: str
    name: str
    nationality: Optional[str] = None
    dob: Optional[datetime] = None
    image: Optional[str] = None

@dataclass
class EventResult:
    event_name: str
    date: datetime
    place: Optional[int]
    points: Optional[float]

@dataclass
class SeriesResult:
    series_name: str
    series_year: int
    division_name: str
    place: int
    points: float
    results: List[EventResult]

@dataclass
class AthleteStats:
    best_result: Optional[EventResult]
    oldest_result: Optional[EventResult]
    best_series_place: Optional[SeriesResult]
    best_pro_place: Optional[SeriesResult]
    best_challenger_place: Optional[SeriesResult]
    total_events: int
    total_series: int
'''
        self.create_file(os.path.join(self.base_path, "data", "models.py"), models_content)

        # processors.py
        processors_content = '''
from datetime import datetime
from typing import List, Dict
from .models import (
    Athlete, EventResult, SeriesResult, 
    AthleteStats, RankingsData
)
import re

class RankingsProcessor:
    @staticmethod
    def extract_year_from_series(series_name: str) -> int:
        match = re.search(r'(\d{4})', series_name)
        return int(match.group(1)) if match else datetime.now().year
    
    @staticmethod
    def process_event_result(raw_result: Dict) -> EventResult:
        event_data = raw_result['eventDivision']['event']
        return EventResult(
            event_name=event_data['name'],
            date=datetime.fromisoformat(event_data['date'].replace('Z', '+00:00')),
            place=int(raw_result['place']) if raw_result['place'] else None,
            points=float(raw_result['points']) if raw_result['points'] else None
        )
'''
        self.create_file(os.path.join(self.base_path, "data", "processors.py"), processors_content)

    def create_pdf_files(self):
        """Create PDF module files."""
        # generator.py
        generator_content = '''
from fpdf import FPDF
import tempfile
from PIL import Image
from io import BytesIO
import requests
import matplotlib.pyplot as plt
from typing import List
from datetime import datetime
from ..data.models import RankingsData
from .components import PDFComponents
from .styles import PDFStyles

class RankingsPDF(FPDF):
    def __init__(self):
        super().__init__(orientation='L', unit='mm', format='A4')
        self.set_auto_page_break(auto=True, margin=15)
        self.styles = PDFStyles(self)
        self.components = PDFComponents(self)
'''
        self.create_file(os.path.join(self.base_path, "pdf", "generator.py"), generator_content)

    def create_utils_files(self):
        """Create Utils module files."""
        # logging.py
        logging_content = '''
import logging
from typing import Optional

def get_logger(name: str, level: Optional[int] = None) -> logging.Logger:
    """Create and configure a logger instance."""
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    if level is not None:
        logger.setLevel(level)
    elif not logger.level:
        logger.setLevel(logging.INFO)
    
    return logger
'''
        self.create_file(os.path.join(self.base_path, "utils", "logging.py"), logging_content)

def main():
    creator = ModuleContentCreator()
    creator.create_all_modules()

if __name__ == "__main__":
    main()
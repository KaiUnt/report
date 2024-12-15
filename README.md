# fwt_rankings

A Python package for generating FWT rankings reports in PDF format.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
import asyncio
from fwt_rankings.api.client import LiveheatsClient
from fwt_rankings.data.processors import RankingsProcessor
from fwt_rankings.pdf.generator import RankingsReportGenerator

async def main():
    client = LiveheatsClient()
    processor = RankingsProcessor()
    generator = RankingsReportGenerator()
    
    # Add your implementation here

if __name__ == "__main__":
    asyncio.run(main())
```

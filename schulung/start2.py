import requests
from datetime import datetime
import csv

def get_series_rankings(series_id: str, athlete_ids: list):
    url = "https://liveheats.com/api/graphql"
    
    divisions_query = """
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
    
    rankings_query = """
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
    
    divisions_response = requests.post(
        url,
        json={"query": divisions_query, "variables": {"id": series_id}}
    )
    divisions_data = divisions_response.json()
    series_name = divisions_data['data']['series']['name']
    
    with open(f'rankings_{series_id}_filtered.txt', 'w', encoding='utf-8') as f:
        f.write(f"Series: {series_name}\n\n")
        
        for division in divisions_data['data']['series']['rankingsDivisions']:
            variables = {
                "id": series_id,
                "divisionId": division['id']
            }
            
            rankings_response = requests.post(
                url,
                json={"query": rankings_query, "variables": variables}
            )
            rankings_data = rankings_response.json()
            rankings = rankings_data['data']['series'].get('rankings', [])
            
            filtered_rankings = [r for r in rankings if r['athlete']['id'] in athlete_ids]
            
            if filtered_rankings:
                f.write(f"\nDivision: {division['name']}\n")
                f.write("=" * 80 + "\n")
                
                for ranking in filtered_rankings:
                    athlete = ranking['athlete']
                    f.write(f"\nAthlete: {athlete['name']}\n")
                    f.write(f"ID: {athlete['id']}\n")
                    f.write(f"DOB: {athlete.get('dob', 'N/A')}\n")
                    f.write(f"Nationality: {athlete.get('nationality', 'N/A')}\n")
                    f.write(f"Image URL: {athlete.get('image', 'N/A')}\n")
                    f.write(f"Overall Place: {ranking['place']}\n")
                    f.write(f"Total Points: {ranking['points']}\n")
                    
                    if ranking['results']:
                        f.write("Event Results:\n")
                        for result in ranking['results']:
                            event = result['eventDivision']['event']
                            date = datetime.fromisoformat(event['date'].replace('Z', '+00:00'))
                            f.write(f"- {event['name']}\n")
                            f.write(f"  Date: {date.strftime('%Y-%m-%d')}\n")
                            f.write(f"  Place: {result['place']}\n")
                            f.write(f"  Points: {result['points']}\n")
                    f.write("\n")
                f.write("-" * 80 + "\n")

def read_athlete_ids(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        return [row[0] for row in reader]

if __name__ == "__main__":
    series_id = "18306"
    athlete_ids = read_athlete_ids('athlete_ids.csv')
    get_series_rankings(series_id, athlete_ids)
    print(f"Results have been saved to rankings_{series_id}_filtered.txt")
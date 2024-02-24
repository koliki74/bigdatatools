"""
HASVITHA KOLIKINENI
ASSIGNMENT 3 SUBMISSION
BIG DATA TOOLS AND TECHNIQUES
"""

import requests
from datetime import datetime, timedelta


# This class fetches the NEO from NASA API. I have defined my Key in the main function.
class DataFetcher:

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.nasa.gov/neo/rest/v1/feed"

    def fetch_neo_data(self):
        # Fetches the count of Near-Earth Objects (NEOs) for the current week.
        start_date = datetime.now().date()
        end_date = start_date + timedelta(days=7)
        params = {
            "api_key": self.api_key,
            "start_date": start_date,
            "end_date": end_date,
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            raise Exception(f"Failed to fetch NEO data: {response.status_code}")

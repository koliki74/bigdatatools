"""
HASVITHA KOLIKINENI
ASSIGNMENT 3 SUBMISSION
BIG DATA TOOLS AND TECHNIQUES
"""

from data_fetcher import DataFetcher
from data_process import DataProcessor
from redis_handler import RedisHandler

if __name__ == "__main__":
    api_key = None
    # I have hidden my API key, since I am submitting this file to public github repository. I have added the API key for your reference on the google docs that I have submitted.
    redis_config = {"host": "localhost", "port": 6379, "db": 0}

    # Initialize classes
    fetcher = DataFetcher(api_key)

    redis_handler = RedisHandler()

    # Fetch Data
    neo_data = fetcher.fetch_neo_data()
    processor = DataProcessor(neo_data)

    key = "neo_weekly_data"

    # Insert the fetched data into Redis
    redis_handler.insert_data(key, neo_data)  # Using neo_data directly

    # Asking the user if they want to save the generated plots as PNGs before displaying them.
    save_input = input(
        "Do you want to save the Generated charts into your local drive? \n[Say 'Y' or 'Yes' for Yes.]"
    )
    if save_input.lower() == "yes" or save_input.lower() == "y":
        save = True
    else:
        save = False

    # Process the data and generate charts
    processor.generate_line_chart(save)
    processor.generate_bar_chart(save)
    processor.generate_pie_chart(save)

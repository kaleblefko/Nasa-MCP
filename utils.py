import os
import requests

def fetch_apod_data(date: str | None = None, start_date: str | None = None, end_date: str | None = None) -> dict:
    url = f"https://api.nasa.gov/planetary/apod?api_key={os.getenv('NASA_API_KEY')}"
    if date:
        url += f"&date={date}"
    elif start_date and end_date:
        url += f"&start_date={start_date}&end_date={end_date}"
    else:
        raise Exception("Must provide either a single date or a start_date + end_date range")
    response = requests.get(url)
    return response.json()
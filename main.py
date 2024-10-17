import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv('API_KEY')

# Base URL for AccuWeather API
BASE_URL = "http://dataservice.accuweather.com"

def get_location_key(city_name):
    """Fetch location key for the specified city."""
    url = f"{BASE_URL}/locations/v1/cities/search"
    params = {'apikey': API_KEY, 'q': city_name}
    response = requests.get(url, params=params)
    data = response.json()

    if data:
        return data[0]['Key']
    else:
        print("City not found.")
        return None

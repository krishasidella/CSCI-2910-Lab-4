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
        
def get_weather_data(location_key):
    """Fetch current weather data for the specified location key."""
    url = f"{BASE_URL}/currentconditions/v1/{location_key}"
    params = {'apikey': API_KEY}
    response = requests.get(url, params=params)
    return response.json()

def main():
    city_name = input("Enter the city name: ")
    location_key = get_location_key(city_name)

if location_key:
        weather_data = get_weather_data(location_key)
        if weather_data:
            current_weather = weather_data[0]
            print(f"Current temperature in {city_name}: {current_weather['Temperature']['Metric']['Value']}°C")
        else:
            print("Weather data not available.")

if __name__ == "__main__":
    main()

    


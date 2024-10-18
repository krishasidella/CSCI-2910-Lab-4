import requests
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve API key from environment variables
API_KEY = "GkboEiiLSYkak5RbcZY5qB2HPaCVGJGp"

def get_location_key(city_name):
    url = f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={API_KEY}&q={city_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['Key']
    return None

def get_weather(location_key):
    url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            # Extract only the relevant information
            weather_info = {
                'WeatherText': data[0]['WeatherText'],
                'Temperature': data[0]['Temperature']['Metric']['Value'],
                'Unit': data[0]['Temperature']['Metric']['Unit']  # To include unit of temperature
            }
            return weather_info
    return None

if __name__ == "__main__":
    city_name = input("Enter a city name: ")
    location_key = get_location_key(city_name)
    
    if location_key:
        weather = get_weather(location_key)
        if weather:
            print(f"Current weather in {city_name}: {weather['WeatherText']}, "
                  f"{weather['Temperature']}°{weather['Unit']}")
        else:
            print("Could not retrieve weather information.")
    else:
        print("City not found.")

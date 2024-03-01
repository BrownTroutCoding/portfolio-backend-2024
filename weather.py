# weather.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather_by_zip(zip_code, country_code='US'):
    # weather_key = os.getenv('OPENWEATHER_API_KEY')
    weather_key = 'f4321533f2e9adff0b2934752827dca5'
    if not weather_key:
        raise ValueError("No weather api key found.")
    
    url = f"{BASE_URL}?zip={zip_code},{country_code}&appid={weather_key}"
    response = requests.get(url)

    # check if the request was successful
    if response.status_code == 200:
        weather_data = response.json()
        print(weather_data)
        return weather_data
    else:
        response.raise_for_status()

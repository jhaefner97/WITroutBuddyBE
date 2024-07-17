import os

from dotenv import load_dotenv
from enum import Enum

load_dotenv()

class WeatherAPI(Enum):
    base_url = "http://api.weatherapi.com/v1"
    forecast_endpoint = "/forecast"
    json_response = ".json"
    api_key = WeatherAPIKey = os.getenv("weather_api_key")

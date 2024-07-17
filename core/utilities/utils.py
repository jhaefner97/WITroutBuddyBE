import os

from dotenv import load_dotenv
from enum import Enum

load_dotenv()

class WeatherAPI(Enum):
    base_url = "http://api.weatherapi.com/v1"
    forecast_endpoint = "/forecast"
    json_response = ".json"
    api_key = WeatherAPIKey = os.getenv("weather_api_key")


class USGSStreamData(Enum):
    base_url = "https://waterservices.usgs.gov/nwis/iv/"
    flow_data_code = "00060"
    gauge_height_data_code = "00065"
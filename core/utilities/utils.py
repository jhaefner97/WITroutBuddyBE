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

class DatabaseConfig(Enum):
    db_user = os.getenv("db_username")
    db_password = os.getenv("db_password")
    db_host = os.getenv("db_host")
    db_port = os.getenv("db_port")
    db_name = os.getenv("db_database")
    db_ssl_mode = os.getenv("db_ssl_mode")


class APIStatus(Enum):
    success = "Success"
    error = "Error"
    no_data = "No data found"
    db_error = "Error saving data to database"
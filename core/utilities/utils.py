import logging
import logging.handlers
import os

from dotenv import load_dotenv
from enum import Enum
from pathlib import Path

load_dotenv()

class Paths():

    def __init__(self):
        self.project_root = Path(__file__).resolve().parents[2]
        self.logging_dir = self.project_root / "logs"

        if not self.logging_dir.exists():
            self.logging_dir.mkdir(parents=True, exist_ok=True)

def create_logger(logger_name):
    paths = Paths()
    log_file = paths.logging_dir / f"{logger_name}.log"

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=1000000, backupCount=5)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger

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
import requests

from core.data_models.weather_api_model import Model
from core.utilities.utils import WeatherAPI

def get_7_day_forecast(zip_code: str, days:int=7) -> Model:
    url = f"{WeatherAPI.base_url.value}{WeatherAPI.forecast_endpoint.value}{WeatherAPI.json_response.value}"
    params = {
        "key": WeatherAPI.api_key.value,
        "q": zip_code,
        "days": days
    }
    response = requests.get(url=url, params=params)
    return response.json()
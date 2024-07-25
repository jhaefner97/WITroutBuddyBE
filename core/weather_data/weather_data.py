import requests

from core.data_models.weather_api_model import Model
from core.utilities.utils import WeatherAPI
from dataclasses import dataclass, field

@dataclass 
class LocationData:
    name: str
    lat: float
    lon: float

@dataclass
class CurrentWeather:
    temperature: float
    wind_speed: float
    wind_direction: str
    humidity: float
    pressure: float
    feels_like: float
    wind_chill: float
    gust_speed: float

@dataclass
class Condition:
    text: str
    icon: str
    code: int

@dataclass
class HourlyForecast:
    time: str
    temp: float
    wind_speed: float
    wind_direction: str
    humidity: float
    pressure: float
    feels_like: float
    wind_chill: float
    gust_speed: float
    condition: Condition

@dataclass
class DailyForecast:
    date: str
    max_temp: float
    min_temp: float
    avg_temp: float
    max_wind_speed: float
    total_precipitation: float
    avg_humidity: float
    condition: Condition
    hourly_conditions: list[HourlyForecast]
    
@dataclass
class ResponsePayload:
    location: LocationData| None = None
    current: CurrentWeather| None = None
    forecast: list[DailyForecast] = field(default_factory=list)

def get_7_day_forecast(zip_code: str, days:int=1) -> Model:
    url = f"{WeatherAPI.base_url.value}{WeatherAPI.forecast_endpoint.value}{WeatherAPI.json_response.value}"
    params = {
        "key": WeatherAPI.api_key.value,
        "q": zip_code,
        "days": days
    }
    response = requests.get(url=url, params=params)
    weather_data = Model(**response.json())

    response = ResponsePayload()

    response.current = CurrentWeather(
        temperature=weather_data.current.temp_f,
        wind_speed=weather_data.current.wind_mph,
        wind_direction=weather_data.current.wind_dir,
        humidity=weather_data.current.humidity,
        pressure=weather_data.current.pressure_in,
        feels_like=weather_data.current.feelslike_f,
        wind_chill=weather_data.current.windchill_f,
        gust_speed=weather_data.current.gust_mph
    )

    response.location = LocationData(
        name=weather_data.location.name,
        lat=weather_data.location.lat,
        lon=weather_data.location.lon
    )

    for day in weather_data.forecast.forecastday:
        daily_forecast = DailyForecast(
            date=day.date,
            max_temp=day.day.maxtemp_f,
            min_temp=day.day.mintemp_f,
            avg_temp=day.day.avgtemp_f,
            max_wind_speed=day.day.maxwind_mph,
            total_precipitation=day.day.totalprecip_in,
            avg_humidity=day.day.avghumidity,
            condition=Condition(
                text=day.day.condition.text,
                icon=day.day.condition.icon,
                code=day.day.condition.code
            ),
            hourly_conditions=[]
        )

        for hour in day.hour:
            daily_forecast.hourly_conditions.append(
                HourlyForecast(
                    time=hour.time,
                    temp=hour.temp_f,
                    wind_speed=hour.wind_mph,
                    wind_direction=hour.wind_dir,
                    humidity=hour.humidity,
                    pressure=hour.pressure_in,
                    feels_like=hour.feelslike_f,
                    wind_chill=hour.windchill_f,
                    gust_speed=hour.gust_mph,
                    condition=Condition(
                        text=hour.condition.text,
                        icon=hour.condition.icon,
                        code=hour.condition.code
                    )
                )
            )
        response.forecast.append(daily_forecast)



    return response
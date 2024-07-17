from fastapi import APIRouter
from core.weather_data.weather_data import get_7_day_forecast

router = APIRouter(prefix="/weather", tags=["weather"])

@router.get("/")
async def root():
    return {"Test": "Weather Router Is Running"}

@router.get("/7day_forecast")
async def get_seven_day_forecast_zip(zip_code: int):
    return get_7_day_forecast(zip_code=zip_code)
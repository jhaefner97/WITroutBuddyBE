import uvicorn
from fastapi import FastAPI

from core.routes.gets.usgs import router as usgs_router
from core.routes.gets.weather_data import router as weather_router
from core.utilities.log import get_logger

app = FastAPI()
app.include_router(usgs_router)
app.include_router(weather_router)
logger = get_logger()

logger.info("Starting the application")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
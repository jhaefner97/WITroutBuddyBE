from fastapi import APIRouter
from core.usgs_data.usgs_data import get_stream_data_by_site

router = APIRouter(prefix="/geo", tags=["usgs"])

@router.get("/")
async def root():
    return {"Test": "Geo Router Is Running"}

@router.get("/stream_data")
async def get_stream_data(site_number: str):
    return get_stream_data_by_site(site_number=site_number)

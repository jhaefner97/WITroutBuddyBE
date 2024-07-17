from fastapi import APIRouter

router = APIRouter(prefix="/geo", tags=["usgs"])

@router.get("/")
async def root():
    return {"Test": "Geo Router Is Running"}
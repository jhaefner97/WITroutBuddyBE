import json
import requests

from core.data_models.stream_data import Model
from core.data_models.sql.site_data import SiteData
from core.utilities.utils import USGSStreamData, APIStatus
from core.utilities.db import session
from core.utilities.log import get_logger
from datetime import datetime, UTC

logger = get_logger()

def get_stream_data_by_site(site_number: str) -> Model:

    current_utc_datetime = datetime.now(UTC)

    url = USGSStreamData.base_url.value
    params = {
        "sites": site_number,
        "format": "json",
        "parameterCd": f"{USGSStreamData.flow_data_code.value},{USGSStreamData.gauge_height_data_code.value}"
    }
    response = requests.get(url=url, params=params).json()
    usgs_data = Model(**response)
    data = usgs_data.value.timeSeries
    if data != []:

        #  Format API response
        api_response = {}
        api_response["Site Name"] = data[0].sourceInfo.siteName
        api_response["Site Code"] = data[0].sourceInfo.siteCode[0].value
        api_response["Stream Flow Unit"] = data[0].variable.unit.unitCode
        api_response["Stream Flow Value"] = data[0].values[0].value[0].value
        api_response["Guage Height Unit"] = data[1].variable.unit.unitCode
        api_response["Guage Height Value"] = data[1].values[0].value[0].value
        api_response["Message"] = APIStatus.success.value

        #  Save the data to the database
        site_data = SiteData(
            site_code=api_response["Site Code"],
            stream_flow_unit=api_response["Stream Flow Unit"],
            stream_flow_value=api_response["Stream Flow Value"],
            guage_height_unit=api_response["Guage Height Unit"],
            guage_height_value=api_response["Guage Height Value"],
            timestamp=current_utc_datetime
        )

        try:
            session.add(site_data)
            session.commit()
            logger.info("Data saved to the database")
        except Exception as e:
            session.rollback()
            api_response["Message"] = APIStatus.db_error.value + f": {str(e)}"
            logger.error(f"Error saving data to the database: {str(e)}")

    else:
        api_response["Message"] = APIStatus.no_data.value

    logger.info(f"API response: {json.dumps(api_response)}")
    return api_response
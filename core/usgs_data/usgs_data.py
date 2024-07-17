import requests

from core.data_models.stream_data import Model
from core.utilities.utils import USGSStreamData

def get_stream_data_by_site(site_number: str) -> Model:
    url = USGSStreamData.base_url.value
    params = {
        "sites": site_number,
        "format": "json",
        "parameterCd": f"{USGSStreamData.flow_data_code.value},{USGSStreamData.gauge_height_data_code.value}"
    }
    response = requests.get(url=url, params=params)
    return response.json()
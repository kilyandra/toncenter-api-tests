import httpx
from src.schemas import APIError, AddressState

BASE_URL = "https://toncenter.com/api/v2"


def check_address_state(address):
    req = httpx.get(url=BASE_URL + "/getAddressState", params={"address": address})
    r = req.json()

    if r['ok'] is True:
        validated = AddressState.model_validate(r)
        return validated.result

    else:
        error = APIError.model_validate(r)
        raise ValueError(f"{error.code}: {error.error}")
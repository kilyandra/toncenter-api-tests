import httpx, os
from dotenv import load_dotenv
from src.schemas import APIError, AddressStateResponse, DetectAddressResponse, DetectHashResponse

BASE_URL = "https://toncenter.com/api/v2"

load_dotenv()
API_KEY = os.getenv("TON_API_KEY")


def make_request(endpoint, params):
    req = httpx.get(
        url=BASE_URL + endpoint,
        params=params,
        headers={"X-API-Key": API_KEY}
    )
    r = req.json()

    if r['ok'] is True:
        return r
    else:
        error = APIError.model_validate(r)
        raise ValueError(f"{error.code}: {error.error}")

def get_address_state(address):
    r = make_request("/getAddressState", {"address": address})
    return AddressStateResponse.model_validate(r).result

def detect_address(address):
    r = make_request("/detectAddress", {"address": address})
    return DetectAddressResponse.model_validate(r).result

def detect_hash(_hash):
    r = make_request("/detectHash", {"hash": _hash})
    return DetectHashResponse.model_validate(r).result

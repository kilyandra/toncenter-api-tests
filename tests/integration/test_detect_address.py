import pytest
from tonsdk.utils import Address
from src.client import detect_address
from src.exceptions import APIRequestError
from tests.conftest import ADDRESS_RAW, ADDRESS_BOUNCEABLE, ADDRESS_NON_BOUNCEABLE



@pytest.mark.parametrize("address, given_type", [
    (ADDRESS_RAW, "raw_form"),
    (ADDRESS_BOUNCEABLE, "friendly_bounceable"),
    (ADDRESS_NON_BOUNCEABLE, "friendly_non_bounceable"),
], ids=["raw", "bounceable", "non_bounceable"])
def test_detect_address_formats(address, given_type):
    r = detect_address(address)
    assert r.given_type == given_type
    assert Address(r.raw_form).to_buffer() == Address(address).to_buffer()
    assert Address(r.bounceable.b64).to_buffer() == Address(address).to_buffer()
    assert Address(r.bounceable.b64url).to_buffer() == Address(address).to_buffer()
    assert Address(r.non_bounceable.b64).to_buffer() == Address(address).to_buffer()
    assert Address(r.non_bounceable.b64url).to_buffer() == Address(address).to_buffer()

def test_detect_address_testnet(address_testnet):
    r = detect_address(address_testnet)
    assert r.test_only is True

def test_detect_address_invalid(address_invalid):
    with pytest.raises(APIRequestError) as exc:
        detect_address(address_invalid)

    assert exc.value.status_code == 422
    assert exc.value.api_code == 422

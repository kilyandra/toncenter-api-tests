import pytest
from src.client import detect_address
from tonsdk.utils import Address
from tests.conftest import RAW_ADDRESS, BOUNCEABLE_ADDRESS, NON_BOUNCEABLE_ADDRESS


@pytest.mark.parametrize("address, given_type", [
    (RAW_ADDRESS, "raw_form"),
    (BOUNCEABLE_ADDRESS, "friendly_bounceable"),
    (NON_BOUNCEABLE_ADDRESS, "friendly_non_bounceable"),
], ids=["raw", "bounceable", "non_bounceable"])
def test_detect_address_formats(address, given_type):
    r = detect_address(address)
    assert r.given_type == given_type
    assert Address(r.raw_form).to_buffer() == Address(address).to_buffer()
    assert Address(r.bounceable.b64).to_buffer() == Address(address).to_buffer()
    assert Address(r.bounceable.b64url).to_buffer() == Address(address).to_buffer()
    assert Address(r.non_bounceable.b64).to_buffer() == Address(address).to_buffer()
    assert Address(r.non_bounceable.b64url).to_buffer() == Address(address).to_buffer()

def test_detect_address_testnet(testnet_address):
    r = detect_address(testnet_address)
    assert r.test_only is True

def test_detect_address_invalid(invalid_address):
    with pytest.raises(ValueError):
        detect_address(invalid_address)

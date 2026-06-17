import pytest
from tonsdk.utils import Address
from src.client import unpack_address
from src.exceptions import APIRequestError
from tests.conftest import ADDRESS_BOUNCEABLE, ADDRESS_NON_BOUNCEABLE


@pytest.mark.parametrize("address", [
    ADDRESS_BOUNCEABLE,
    ADDRESS_NON_BOUNCEABLE,
], ids=["bounceable", "non_bounceable"])
def test_unpack_address_friendly(address):
    address_unpacked = Address(address).to_string(False)
    assert unpack_address(address_unpacked).lower() == address_unpacked

def test_unpack_address_raw(address_raw):
    assert unpack_address(address_raw).lower() == address_raw

def test_unpack_address_invalid(address_invalid):
    with pytest.raises(APIRequestError) as exc:
        unpack_address(address_invalid)

    assert exc.value.status_code == 422
    assert exc.value.api_code == 422

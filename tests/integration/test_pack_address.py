import pytest
from tonsdk.utils import Address
from src.client import pack_address
from src.exceptions import APIRequestError
from tests.conftest import ADDRESS_BOUNCEABLE, ADDRESS_NON_BOUNCEABLE


@pytest.mark.parametrize("address", [
    ADDRESS_BOUNCEABLE,
    ADDRESS_NON_BOUNCEABLE,
], ids=["bounceable", "non_bounceable"])
def test_pack_address_friendly(address):
    assert pack_address(address) == address

def test_pack_address_raw(address_raw):
    address_packed = Address(address_raw).to_string(is_user_friendly=True, is_bounceable=True, is_url_safe=True)
    assert pack_address(address_raw) == address_packed

def test_pack_address_invalid(address_invalid):
    with pytest.raises(APIRequestError) as exc:
        pack_address(address_invalid)

    assert exc.value.status_code == 422
    assert exc.value.api_code == 422

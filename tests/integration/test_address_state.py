import pytest
from src.client import get_address_state
from src.exceptions import APIRequestError


def test_get_address_state_active(address_active):
    assert get_address_state(address_active) == "active"

def test_get_address_state_uninitialized(address_uninitialized):
    assert get_address_state(address_uninitialized) == "uninitialized"

def test_get_address_state_invalid_address(address_invalid):
    with pytest.raises(APIRequestError) as exc:
        get_address_state(address_invalid)

    assert exc.value.status_code == 422
    assert exc.value.api_code == 422

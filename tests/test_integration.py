import pytest
from src.client import check_address_state


def test_get_address_state_active(active_address):
    assert check_address_state(active_address) == "active"

def test_get_address_state_uninitialized(uninitialized_address):
    assert check_address_state(uninitialized_address) == "uninitialized"

def test_get_address_state_invalid_address(invalid_address):
    with pytest.raises(ValueError):
        check_address_state(invalid_address)
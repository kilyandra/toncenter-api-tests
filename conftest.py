import pytest


@pytest.fixture
def active_address():
    return "UQD-IS_-dhjmD0r8q-1H4xtpBJK_d-LoLxkNxXOTCJeGSQyV"

@pytest.fixture
def uninitialized_address():
    return "UQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJKZ"

@pytest.fixture
def invalid_address():
    return "abcde"
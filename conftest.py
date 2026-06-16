import pytest
from time import sleep

@pytest.fixture(autouse=True)
def rate_limit():
    yield
    sleep(0.1)

RAW_ADDRESS = "0:fe212ffe7618e60f4afcabed47e31b690492bf77e2e82f190dc5739308978649"
BOUNCEABLE_ADDRESS = "EQD-IS_-dhjmD0r8q-1H4xtpBJK_d-LoLxkNxXOTCJeGSVFQ"
NON_BOUNCEABLE_ADDRESS = "UQD-IS_-dhjmD0r8q-1H4xtpBJK_d-LoLxkNxXOTCJeGSQyV"
UNINITIALIZED_ADDRESS = "UQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJKZ"
TESTNET_ADDRESS = "0QBjdZoPHQq-HgQIT610n31y8Sq0GDRz-SClAaJd_d1LT2Dg"
INVALID_ADDRESS = "abcde"


@pytest.fixture
def raw_address():
    return RAW_ADDRESS

@pytest.fixture
def bounceable_address():
    return BOUNCEABLE_ADDRESS

@pytest.fixture
def active_address():
    return NON_BOUNCEABLE_ADDRESS

@pytest.fixture
def testnet_address():
    return TESTNET_ADDRESS


@pytest.fixture
def nonbounceable_address():
    return NON_BOUNCEABLE_ADDRESS

@pytest.fixture
def uninitialized_address():
    return UNINITIALIZED_ADDRESS

@pytest.fixture
def invalid_address():
    return INVALID_ADDRESS
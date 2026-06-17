import pytest
from time import sleep


@pytest.fixture(autouse=True)
def rate_limit():
    yield
    sleep(0.1)


ADDRESS_RAW = "0:5f696ae8fe14acd382246b299a469c12f755b3d16d3b8aa0975ba230bcc90944"
ADDRESS_BOUNCEABLE = "EQD-IS_-dhjmD0r8q-1H4xtpBJK_d-LoLxkNxXOTCJeGSVFQ"
ADDRESS_NON_BOUNCEABLE = "UQCn7XyU6Tbh6jJXsfm6unW-7FRaU7UAOS0dSNkEtGxOeJXS"
ADDRESS_UNINITIALIZED = "UQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJKZ"
ADDRESS_TESTNET = "0QBjdZoPHQq-HgQIT610n31y8Sq0GDRz-SClAaJd_d1LT2Dg"
ADDRESS_INVALID = "abcde"

HASH_B64 = "1Trph6GtHxuj74nRLzUTlomcD1OGt2ie25A8hv3YQAg="
HASH_B64URL = "a9-wBUBr4QlHypx3k5o12BrFyIpUO-3cVhjE5OfT2e0"
HASH_HEX = "ce34b8b97810c036082454106bcfacf4143b8ad1aa60c82a9aec72be4e57c166"
HASH_INVALID = "asdfg"


@pytest.fixture
def address_raw():
    return ADDRESS_RAW

@pytest.fixture
def address_bounceable():
    return ADDRESS_BOUNCEABLE

@pytest.fixture
def address_active():
    return ADDRESS_NON_BOUNCEABLE

@pytest.fixture
def address_testnet():
    return ADDRESS_TESTNET


@pytest.fixture
def address_nonbounceable():
    return ADDRESS_NON_BOUNCEABLE

@pytest.fixture
def address_uninitialized():
    return ADDRESS_UNINITIALIZED

@pytest.fixture
def address_invalid():
    return ADDRESS_INVALID

@pytest.fixture
def hash_b64():
    return HASH_B64

@pytest.fixture
def hash_b64url():
    return HASH_B64URL

@pytest.fixture
def hash_hex():
    return HASH_HEX

@pytest.fixture
def hash_invalid():
    return HASH_INVALID
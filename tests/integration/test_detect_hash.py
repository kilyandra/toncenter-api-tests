import pytest, base64
from src.client import detect_hash
from src.exceptions import APIRequestError
from tests.conftest import HASH_B64, HASH_B64URL, HASH_HEX


@pytest.mark.parametrize("_hash, given_type", [
    (HASH_B64, "b64"),
    (HASH_B64URL, "b64url"),
    (HASH_HEX, "hex"),
], ids=["b64", "b64url", "hex"])
def test_detect_hash(_hash, given_type):
    r = detect_hash(_hash)

    r_hash = getattr(r, given_type)
    assert _hash == r_hash

    b64_to_hex = base64.b64decode(r.b64).hex()
    padded = r.b64url + '=' * (-len(r.b64url) % 4)
    b64url_to_hex = base64.urlsafe_b64decode(padded).hex()
    assert b64_to_hex == b64url_to_hex == r.hex

def test_detect_hash_invalid(hash_invalid):
    with pytest.raises(APIRequestError) as exc:
        detect_hash(hash_invalid)

    assert exc.value.status_code == 422
    assert exc.value.api_code == 422

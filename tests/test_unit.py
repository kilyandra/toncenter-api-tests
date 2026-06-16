import httpx
from src.client import check_address_state


def test_get_address_state_frozen(monkeypatch):
    class MockFrozenResponse:
        @staticmethod
        def json():
            return {"ok": True,
                    "result": "frozen"}

    def mock_get(*args, **kwargs):
        return MockFrozenResponse()

    monkeypatch.setattr(httpx, "get", mock_get)

    result = check_address_state("mock_frozen_address")
    assert result == "frozen"
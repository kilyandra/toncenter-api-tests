from pydantic import BaseModel, field_validator
from tonsdk.utils import Address


class UnpackAddressResponse(BaseModel):
    ok: bool
    result: str

    @field_validator('result')
    def validate_result(cls, v):
        addr = Address(v)
        if addr.is_user_friendly:
            raise ValueError(f"Expected non-user-friendly address, got: {v}")
        return v

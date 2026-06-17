from pydantic import BaseModel, field_validator
from tonsdk.utils import Address


class PackAddressResponse(BaseModel):
    ok: bool
    result: str

    @field_validator('result')
    def validate_result(cls, v):
        addr = Address(v)
        if not addr.is_user_friendly:
            raise ValueError(f"Expected user-friendly address, got: {v}")
        return v

from pydantic import BaseModel, field_validator
from tonsdk.utils import Address


class BounceableVariant(BaseModel):
    b64: str
    b64url: str

    @field_validator('b64')
    def validate_b64(cls, v):
        addr = Address(v)
        if not (addr.is_bounceable and not addr.is_url_safe and addr.is_user_friendly):
            raise ValueError(f"Expected bounceable non-url-safe user-friendly address, got: {v}")
        return v

    @field_validator('b64url')
    def validate_b64url(cls, v):
        addr = Address(v)
        if not (addr.is_bounceable and addr.is_url_safe and addr.is_user_friendly):
            raise ValueError(f"Expected bounceable url-safe user-friendly address, got: {v}")
        return v

class NonBounceableVariant(BaseModel):
    b64: str
    b64url: str

    @field_validator('b64')
    def validate_b64(cls, v):
        addr = Address(v)
        if not (not addr.is_bounceable and not addr.is_url_safe and addr.is_user_friendly):
            raise ValueError(f"Expected nonbounceable non-url-safe user-friendly address, got: {v}")
        return v

    @field_validator('b64url')
    def validate_b64url(cls, v):
        addr = Address(v)
        if not (not addr.is_bounceable and addr.is_url_safe and addr.is_user_friendly):
            raise ValueError(f"Expected nonbounceable url-safe user-friendly address, got: {v}")
        return v

class DetectAddressResult(BaseModel):
    raw_form: str
    bounceable: BounceableVariant
    non_bounceable: NonBounceableVariant
    given_type: str
    test_only: bool

    @field_validator('raw_form')
    def validate_raw_form(cls, v):
        addr = Address(v)
        if addr.is_user_friendly:
            raise ValueError(f"Expected non-user-friendly address, got: {v}")
        return v

class DetectAddressResponse(BaseModel):
    ok: bool
    result: DetectAddressResult

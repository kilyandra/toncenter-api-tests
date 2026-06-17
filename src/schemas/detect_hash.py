from pydantic import BaseModel, field_validator
import base64


class DetectHashResult(BaseModel):
    b64: str
    b64url: str
    hex: str

    @field_validator('b64')
    def validate_b64(cls, v):
        padded = v + '=' * (-len(v) % 4)
        if len(base64.b64decode(padded).hex()) != 64:
            raise ValueError(f"Expected 64 bytes, got {len(v)}")
        return v

    @field_validator('b64url')
    def validate_b64url(cls, v):
        if '+' in v or '/' in v or '=' in v:
            raise ValueError(f"Expected url-safe base64, got: {v}")
        padded = v + '=' * (-len(v) % 4)
        if len(base64.urlsafe_b64decode(padded).hex()) != 64:
            raise ValueError(f"Expected 64 bytes, got {len(v)}")
        return v

    @field_validator('hex')
    def validate_hex(cls, v):
        if len(v) != 64:
            raise ValueError(f"Expected 64 bytes (256 bits), got {len(v)}")
        return v

class DetectHashResponse(BaseModel):
    ok: bool
    result: DetectHashResult

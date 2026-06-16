from pydantic import BaseModel


class APIError(BaseModel):
    ok: bool
    error: str
    code: int

class AddressState(BaseModel):
    ok: bool
    result: str

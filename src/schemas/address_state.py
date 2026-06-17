from pydantic import BaseModel


class AddressStateResponse(BaseModel):
    ok: bool
    result: str
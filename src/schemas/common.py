from pydantic import BaseModel


class APIError(BaseModel):
    ok: bool
    error: str
    code: int

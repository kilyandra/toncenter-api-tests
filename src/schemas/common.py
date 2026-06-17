from pydantic import BaseModel


class APIErrorResponse(BaseModel):
    ok: bool
    error: str
    code: int

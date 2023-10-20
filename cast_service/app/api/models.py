from pydantic import BaseModel
from typing import Optional

class CastIn(BaseModel):
    name: str
    country: str


class CastOut(CastIn):
    id: int


class CastUpdate(CastIn):
    name: Optional[str] = None
    country: Optional[str] = None
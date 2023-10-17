from pydantic import BaseModel, EmailStr
from typing import List, Optional


class CastIn(BaseModel):
    name: str
    country: str
    email: EmailStr


class CastOut(CastIn):
    id: int


class Castupdate(CastIn):
    name: Optional[str] = None
    country: Optional[str] = 'IND'
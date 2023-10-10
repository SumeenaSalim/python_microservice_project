from typing import List, Optional
from pydantic import BaseModel

class MovieIn(BaseModel):
    title: str
    description: str
    type: List[str]
    casts: List[str]
    year: int

class MovieOut(MovieIn):
    id: int

class MovieUpdate(MovieIn):
    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[List[str]] = None
    casts: Optional[List[str]] = None
    year: Optional[int] = None

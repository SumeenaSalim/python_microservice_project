from typing import List
from pydantic import BaseModel

class Movies(BaseModel):
    title: str
    description: str
    type: List[str]
    casts: List[str]
    year: int

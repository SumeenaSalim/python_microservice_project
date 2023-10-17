from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import CastOut, CastIn
from app.api.db_api import get_cast, add_cast

casts = APIRouter()

@casts.get('/{id}', response_model=CastOut)
async def get_cast(id: int):
    cast = await get_cast(id)
    if not cast:
        raise HTTPException(status_code=404, detail=f"Cast with {id} not found")
    return {
        "message": "success",
        "data": cast
    }


@casts.post('/')
async def create_cast(payload: CastIn):
    cast_id = await add_cast(payload)
    return {
        "message": "success",
        "data": {
            "id": cast_id,
            "name": payload.name,
            "country": payload.country,
            "email": payload.email,
        }        
    }
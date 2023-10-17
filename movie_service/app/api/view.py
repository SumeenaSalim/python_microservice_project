from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import MovieOut, MovieIn
from app.api.db_api import get_all_movies, fetch_movie, add_movie, edit_movie, delete_movie
from app.api.service import is_cast_present


movie = APIRouter()


@movie.get('/', response_model=List[MovieOut])
async def get_movies():
    resp = await get_all_movies()
    if not resp:
        raise HTTPException(status_code=404, detail="Connection failed")
    return {
        "message": "success",
        "data": resp
    }


@movie.get('/{id}', response_model=MovieOut)
async def get_movie_by_id(id: int):
    movie = await fetch_movie(id)
    print("\n\n\n", movie)
    if not movie:
        raise HTTPException(status_code=404, detail=f"Movie with given id {id} not found")
    return {
        "message": "success",
        "data": movie
    }


@movie.post('/', status_code=201)
async def create_movie(payload: MovieIn):
    for c_id in payload.casts_id:
        if not is_cast_present(c_id):
            raise HTTPException(status_code=404, detail=f"Cast with id:{c_id} does not exist")

    movie_id = await add_movie(payload)
    return {
        "message": "success",
        "data": {
            "id": movie_id,
            "title": payload.title,
            "description": payload.description,
            "type": payload.type,
            "casts": payload.casts,
            "year": payload.year,
        }        
    }


@movie.put('/{id}')
async def update_movie(id: int, payload: MovieIn):
    movie = await fetch_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail=f"Movie with given id {id} does not exist")
    
    if 'casts_id' in payload:
        for c_id in payload.casts_id:
            if not is_cast_present(c_id):
                raise HTTPException(status_code=404, detail=f"Cast with given id:{c_id} does not exist")

    movie_id = await edit_movie(id, payload)
    return {
        "message": "success",
        "data": {
            "id": movie_id,
            "title": payload.title,
            "description": payload.description,
            "type": payload.type,
            "casts": payload.casts,
            "year": payload.year,
        }        
    }    
    

@movie.delete('/{id}')
async def remove_movie(id: int):
    found = await fetch_movie(id)
    if not found:
        raise HTTPException(status_code=404, detail=f"Movie with given id {id} does not exist")

    await delete_movie(id)
    return {
        "message": "success",
        "data": {
            "id": id,
            "deleted": True
        }
    }


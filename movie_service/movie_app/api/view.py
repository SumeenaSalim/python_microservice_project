from fastapi import APIRouter, HTTPException
from typing import List

from movie_app.api.models import MovieOut, MovieIn, MovieUpdate
from movie_app.api import db_api

movie = APIRouter()


@movie.get('/', response_model=List[MovieOut])
async def get_movie():
    return await db_api.get_movies()


@movie.post('/', status_code=201)
async def add_movie(payload: MovieIn):
    movie_id = await db_api.add_movie(payload)
    return {'id': movie_id, **payload.dict()}


@movie.put('/{id}')
async def update_movie(id: int, payload: MovieIn):
    movie = await db_api.get_movie(id)
    if movie:
        update_data = payload.dict(exclude_unset=True)
        movie_in_db = MovieIn(**movie)

        updated_movie = movie_in_db.copy(update=update_data)
        return await db_api.update_movie(id, updated_movie)
    else:
        raise HTTPException(status_code=404, detail="Movie with given id not found")
    

@movie.delete('/{id}')
async def delete_movie(id: int):
    found = await db_api.get_movie(id)
    if not found:
        raise HTTPException(status_code=404, detail="Movie with given id not found")
    return await db_api.delete_movie(id)

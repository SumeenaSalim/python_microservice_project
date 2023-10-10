from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import MovieOut, MovieIn
from app.api.db_api import get_movies, get_movie, add_movie, update_movie, delete_movie

movie = APIRouter()


@movie.get('/', response_model=List[MovieOut])
async def get_movie():
    return await get_movies()


@movie.post('/', status_code=201)
async def add_movie(payload: MovieIn):
    movie_id = await add_movie(payload)
    return {'id': movie_id, **payload.model_dump()}


@movie.put('/{id}')
async def update_movie(id: int, payload: MovieIn):
    movie = await get_movie(id)
    if movie:
        update_data = payload.model_dump(exclude_unset=True)
        movie_in_db = MovieIn(**movie)

        updated_movie = movie_in_db.model_copy(update=update_data)
        return await update_movie(id, updated_movie)
    else:
        raise HTTPException(status_code=404, detail="Movie with given id not found")
    

@movie.delete('/{id}')
async def delete_movie(id: int):
    found = await get_movie(id)
    if not found:
        raise HTTPException(status_code=404, detail="Movie with given id not found")
    return await delete_movie(id)

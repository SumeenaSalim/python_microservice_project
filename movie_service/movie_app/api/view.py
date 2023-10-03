from fastapi import APIRouter, HTTPException
from typing import List

from movie_app.api.models import Movies

movie = APIRouter()

movie_list = [
    {
        'title': 'Khushi',
        'description': 'Feel good movie',
        'type': ['Romance', 'Family'],
        'casts': ['VD', 'Samantha'],
        'year': 2023
    }
]

@movie.get('/', response_model=List[Movies])
async def get_movie():
    return movie_list

@movie.post('/', status_code=201)
async def add_movie(payload: Movies):
    movie = payload.dict()
    movie_list.append(movie)
    return {'id': len(movie_list) - 1}

@movie.put('/{id}')
async def update_movie(id: int, payload: Movies):
    movie = payload.dict()
    movies_length = len(movie_list)
    if 0 <= id <= movies_length:
        movie_list[id] = movie
        return None
    raise HTTPException(status_code=404, detail="Movie with given id not found")

@movie.delete('/{id}')
async def delete_movie(id: int):
    movies_length = len(movie_list)
    if 0 <= id <= movies_length:
        del movie_list[id]
        return None
    raise HTTPException(status_code=404, detail="Movie with given id not found")
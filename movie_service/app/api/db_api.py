from fastapi import HTTPException
from app.api.models import MovieIn
from app.api.db import database, movies


async def get_movies():
    query = movies.select()
    return await database.fetch_all(query=query)


async def add_movie(data: MovieIn):
    if data:
        query = movies.insert().values(**data)
        return await database.execute(query=query)
    else:
        raise HTTPException(status_code=400, detail='Invalid data')
    
    
async def get_movie(id: int):
    query = movies.select(movies.c.id == id)
    return await database.fetch_one(query=query)

    
async def update_movie(id: int, data: MovieIn):
    query = movies.update().where(movies.c.id == id).values(**data)
    return await database.execute(query=query)

async def delete_movie(id: int):
    query = movies.delete().where(movies.c.id == id)
    return await database.execute(query=query)

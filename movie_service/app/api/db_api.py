from fastapi import HTTPException
from app.api.models import MovieIn
from app.api.db import database, movies

async def get_all_movies():
    query = movies.select()
    return await database.fetch_all(query=query)

async def add_movie(data: MovieIn):
    if data:
        title_check_query = movies.select(movies.c.title==data.title)
        title_result = await database.fetch_one(query=title_check_query)
        if not title_result:
            insert_query = movies.insert().values(**data.dict())
            print(insert_query, "\n*", type(insert_query))
            return await database.execute(query=insert_query)
        else:
            raise HTTPException(status_code=400, detail=f"Movie with name {data.title} already exists")
    else:
        raise HTTPException(status_code=400, detail="Invalid data")

async def fetch_movie(id: int):
    query = movies.select(movies.c.id==id)
    return await database.fetch_one(query=query)

async def edit_movie(id: int, data: MovieIn):
    query = movies.update().where(movies.c.id==id).values(
        title=data.title,
        description=data.description,
        type=data.type,
        casts_id=data.casts_id,
        year=data.year
    ).returning(movies.c.id)
    return await database.execute(query=query)

async def delete_movie(id: int):
    query = movies.delete().where(movies.c.id==id)
    return await database.execute(query=query)
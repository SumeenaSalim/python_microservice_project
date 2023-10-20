from app.api.models import CastIn
from app.api.db import casts, database

async def get_cast_from_db(id):
    query = casts.select(casts.c.id==id)
    return await database.fetch_one(query=query)

async def add_cast(payload: CastIn):
    query = casts.insert().values(name=payload.name, country=payload.country)
    return await database.execute(query=query)
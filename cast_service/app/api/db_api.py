from app.api.models import CastIn, CastOut, Castupdate
from app.api.db import casts, Database

async def get_cast(id):
    query = casts.select(casts.c.id == id)
    return await Database.fetch_one(query=query)

async def add_cast(payload: CastIn):
    query = casts.insert().values(name=payload.name, country=payload.country, email=payload.email)
    return await Database.execute(query=query)
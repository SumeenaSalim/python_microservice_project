from fastapi import FastAPI

from app.api.db import database, metadata, engine
from app.api.view import casts

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(casts, prefix='/casts', tags=['casts'])
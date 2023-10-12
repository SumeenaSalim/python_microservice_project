import os
from sqlalchemy import (
    Column,
    MetaData,
    Table,
    create_engine,
    ARRAY,
    String,
    Integer,
)
from databases import Database

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)

metadata = MetaData()

movies = Table(
    "movies",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(50)),
    Column('description', String(250)),
    Column('type', ARRAY(String)),
    Column('casts', ARRAY(String)),
    Column('year', Integer)
)

database = Database(DATABASE_URL)

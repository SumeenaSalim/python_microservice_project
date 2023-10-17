import os

from sqlalchemy import (
    create_engine,
    String,
    Integer,
    MetaData,
    Column,
    Table
)
from pydantic import EmailStr
from typing import List
from databases import Database

DATABASE_URl = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URl)

metadata = MetaData()

casts = Table(
    "casts",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50), nullable=False),
    Column('country', String(50)),
    Column('email', String(100), unique=True, nullable=False)
)

database = Database(DATABASE_URl)
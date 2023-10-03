from fastapi import FastAPI

from movie_app.api.view import movie

app = FastAPI()

app.include_router(movie)
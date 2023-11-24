import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from spacelog.db import init as init_db
from spacelog.schemas import LogInput
from spacelog.api import api_v1
from spacelog.frontend import front

app = FastAPI()
static = os.path.join(os.path.dirname(__file__), 'frontend', 'static')
print(static)
init_db(app)

app.include_router(api_v1, prefix='/api/v1', tags=['v1', 'api'])
app.include_router(front, tags=['v1', 'front'])

app.mount("/static", StaticFiles(directory=static), name="static")


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

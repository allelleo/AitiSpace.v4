import random

import sentry_sdk
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis import asyncio as aioredis

from app import config
from app.api import api_v1
from app.db import init as init_db
from app.logger import logger, get_logger
from app.oauth import oauth_v1

app = FastAPI(
    title=config.app_title,
    description=config.app_description,
    version=config.app_version
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.allow_origins,
    allow_credentials=config.allow_credentials,
    allow_methods=config.allow_methods,
    allow_headers=config.allow_headers,
)

sentry_sdk.init(
    dsn=config.dsn,
    traces_sample_rate=config.traces_sample_rate,
    profiles_sample_rate=config.profiles_sample_rate,
)

redis = aioredis.from_url(config.redis_url)

init_db(app)

app.include_router(oauth_v1, prefix='/oauth/v1', tags=['oauth v1', 'auth'])
app.include_router(api_v1, prefix='/api/v1', tags=['v1', 'api'])


@app.on_event('startup')
async def startup():
    from app.models import AuthTypeProvider
    if not await AuthTypeProvider.exists(title='default'):
        await AuthTypeProvider.create(title='default')
    print('StartUp')


@app.on_event("shutdown")
async def shutdown():
    print('ShutDown')


logger = get_logger()


@app.get('/1')
async def get(value: str):
    for i in range(3):
        for j in range(random.randint(1, 10)):
            logger.CRITICAL()


@app.get('/2')
async def set(key: str):
    await redis.set(key, '{"func": "send_email","params": ["user@eer.ua", "18462"]}')

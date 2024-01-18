from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from starlette.middleware.cors import CORSMiddleware

from core.config import settings, logger

from apps import router as apps_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(
        f"redis://{settings.redis_host}:{settings.redis_port}",
        encoding="utf-8",
        decode_response=True,
    )
    logger.info(f"Cache via redis connected to {settings.redis_host}")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


app = FastAPI(title="FastAPI Shop", lifespan=lifespan)

app.include_router(apps_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=settings.credentials,
    allow_methods=settings.methods,
    allow_headers=settings.headers,
)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

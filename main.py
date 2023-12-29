from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from starlette.middleware.cors import CORSMiddleware

from core.config import settings

from apps import router as apps_router
from core.models import Base
from core.test_database import test_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(
        f"redis://{settings.redis_host}:{settings.redis_port}",
        encoding="utf-8",
        decode_response=True,
    )
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    async with test_database.test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with test_database.test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


app = FastAPI(title="FastAPI Shop", lifespan=lifespan)
# TODO: удалить apps/users
app.include_router(apps_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["GET", "PUT", "POST", "PATCH", "OPTION", "DELETE"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

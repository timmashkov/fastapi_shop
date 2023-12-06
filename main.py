import uvicorn
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from apps import router as apps_router


app = FastAPI(title="Learning FastAPI")
#TODO: удалить apps/users
app.include_router(apps_router)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost", encoding='utf-8', decode_response=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

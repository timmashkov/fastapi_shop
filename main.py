import uvicorn
from fastapi import FastAPI, Request
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from starlette.middleware.cors import CORSMiddleware

from core.config import settings

from apps import router as apps_router
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI(title="Learning FastAPI")
#TODO: удалить apps/users
app.include_router(apps_router)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


app.add_middleware(CORSMiddleware,
                   allow_origins=settings.origins,
                   allow_credentials=True,
                   allow_methods=["GET", "PUT", "POST", "PATCH", "OPTION", "DELETE"],
                   allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
                                  "Access-Control-Allow-Origin", "Authorization"])


@app.get("/items")
async def read_item(request: Request):
    return templates.TemplateResponse("users.html", {"request": request})


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost", encoding='utf-8', decode_response=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

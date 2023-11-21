from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from items_views import router as items_router
from users.views import router as users_router
from api_v1 import router as router_v1

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Создал функцию для асинхронного создания БД
    UPD. Вместо создания БД через скрипт, заюзал Alembic
    """
    yield


app = FastAPI(title="Learning FastAPI", lifespan=lifespan)

app.include_router(router_v1, tags=["API_V1"])
app.include_router(items_router, tags=["Items"])
app.include_router(users_router, tags=["Users"])

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

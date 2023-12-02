from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from apps import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Создал функцию для асинхронного создания БД
    UPD. Вместо создания БД через скрипт, заюзал Alembic
    """
    yield


app = FastAPI(title="Learning FastAPI", lifespan=lifespan)

app.include_router(router_v1, tags=["APPS"])


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

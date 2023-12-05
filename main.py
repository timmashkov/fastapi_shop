from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from apps import router as apps_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Создал функцию для асинхронного создания БД
    UPD. Вместо создания БД через скрипт, заюзал Alembic
    """
    yield


app = FastAPI(title="Learning FastAPI", lifespan=lifespan)
#TODO: удалить apps/users
app.include_router(apps_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

#!/usr/bin/env bash

WORKDIR /fastapi_shop

alembic upgrade head

CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000

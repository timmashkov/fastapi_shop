#!/usr/bin/bash

alembic upgrade 9d074f183e58

uvicorn main:app --host 0.0.0.0 --port 8000 --reload

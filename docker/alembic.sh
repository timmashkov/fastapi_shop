#! /bin/sh
alembic init alembic
alembic upgrade HEAD
exec "$@"
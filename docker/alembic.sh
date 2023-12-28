#! /bin/sh
alembic init alembic
alembic upgrade head
exec "$@"
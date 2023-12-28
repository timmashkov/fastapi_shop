#! /bin/sh
celery --app=apps.tasks.mail:celery worker -l INFO
celery --app=apps.tasks.mail:celery flower
exec "$@"
#! /bin/sh

if [[ "${1}" == "celery" ]]; then
  celery --app=apps.tasks.mail:celery worker -l INFO
elif [[ "${1}" == "flower" ]]; then
  celery --app=apps.tasks.mail:celery flower
 fi
 exec "$@"
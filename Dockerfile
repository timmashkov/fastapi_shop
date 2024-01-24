FROM python:3.12

RUN mkdir /fastapi_shop

WORKDIR /fastapi_shop

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /fastapi_shop

RUN apt-get update && apt-get install -y postgresql-client

COPY docker/migration.sh ./

ENTRYPOINT ["docker/migration.sh"]

#COPY docker/celery.sh ./

#ENTRYPOINT ["docker/celery.sh"]

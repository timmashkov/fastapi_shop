FROM python:3.12

RUN mkdir /fastapi_shop

WORKDIR /fastapi_shop

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /fastapi_shop

CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000

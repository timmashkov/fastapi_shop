FROM python:3.12

RUN mkdir /fastapi_shop

WORKDIR /fastapi_shop

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

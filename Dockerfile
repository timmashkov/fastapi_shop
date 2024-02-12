FROM python:3.12

WORKDIR /fastapi_shop

COPY requirements.txt /fastapi_shop/
RUN pip install --upgrade pip; pip install  -r /fastapi_shop/requirements.txt

COPY . .

FROM python:alpine

WORKDIR /app

COPY . .

RUN pip3 install --upgrade setuptools --no-cache
RUN pip3 install -r requirements.txt

CMD ["python", "main.py"]

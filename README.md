# FastAPI-Shop

[![python](https://img.shields.io/badge/python-3.12_-blue?style=flat-square)](https://www.python.org/)
[![fastapi](https://img.shields.io/badge/fastapi-0.104.1-critical?style=flat-square)](https://fastapi.tiangolo.com/)
[![pytest](https://img.shields.io/badge/pytest-passed-brightgreen)](https://docs.pytest.org/en/7.4.x/)
[![sqlalchemy](https://img.shields.io/badge/sqlalchemy-2.0.23-critical?style=flat-square)](https://www.sqlalchemy.org//)
[![alembic](https://img.shields.io/badge/alembic-1.13.0_-violet?style=flat-square)](https://alembic.sqlalchemy.org//)


## Описание

<details>
<summary><b>ЗАДАНИЕ:</b></summary>

1. Данный проект является выпускной работой студента GeekBrains.

    Технологии:
     - Python 3.12   
     - FastAPI 0.104.1
     - SQLAlchemy 2.0.23
     - Alembic 1.12.1
     - Uvicorn 0.24.0.post1
     - Asyncpg 0.29.0
     - Websockets
     - Celery  
   
    Библиотеки:
     - FastApi-Users[SQLAlchemy]
     - FastAPI-Mail
     - FastAPI-Cache2[redis]

    Реализовано:
      - Создать пользователя, авторизовать его с помощью JWT
      - Сбросить пароль, запросить токен, разлогиниться
      - Создать товар, изменить данные о нем, поиск по товару, удалить его
      - Создать профиль, привязанный к юзеру
      - Создать корзину с товарами, привязанную к юзеру
      - Фоновая отправка письма с благодарностью(через celery)
      - Отправка письма при регистрации
      - Отправка обычного email, отправка файла
      - Чат с юзерами(через websockets)

  
</details>



### Как запустить проект локально:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/timmashkov/fastapi_shop
```

```
cd fastapi_shop
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python -m pip install --upgrade pip
```
### Для запуска в докере:
#### "docker compose up --build"

### Для запуска в локально:
Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
alembic upgrade head
```

Запустить проект:

```
uvicorn main:app run --reload
или запустить main.py
```
Запустить сваггер:
```
http://127.0.0.1:8000/docs
```


### Автор:
Тимур Машков

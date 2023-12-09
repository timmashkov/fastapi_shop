<div id="header" align="'center">
    <img src="https://camo.githubusercontent.com/9eb3fdcaa648566c6a055c75fc17dbaf3849b11ede8019397a30d2092fdcd3be/68747470733a2f2f7374617469632e7769787374617469632e636f6d2f6d656469612f3262653163655f38363435363739303038343534313865626664363165323937363337343634647e6d76322e676966">
</div>
Разработка модуля микро-приложения магазина на fastAPI

# Micro-Store  
##### Описание проекта 
Micro-Store  - это минималистичный интернет магазин. 
##### Основные возможности:
* Создать пользователя, авторизовать его с помощью JWT
* Сбросить пароль, запросить токен, разлогиниться
* Создать товар, изменить данные о нем, поиск по товару, удалить его
* Создать профиль, привязанный к юзеру
* Создать корзину с товарами, привязанную к юзеру
* Фоновая отправка письма с благодарностью(через celery)
* Отправка письма при регистрации
* Отправка обычного email, отправка файла
* Чат с юзерами(через websockets)

###### Все эндпоинты, связанные с выдачей результатов(получение данных по id/name, получение всех значений) кэшируются в редис

##### Технологии 
  
 - Python 3.12   
 - FastAPI 0.104.1
 - SQLAlchemy 2.0.23
 - Alembic 1.12.1
 - Uvicorn 0.24.0.post1
 - Asyncpg 0.29.0
 - Websockets
 - Celery

##### Библиотеки

 - FastApi-Users[SQLAlchemy]
 - FastAPI-Mail
 - FastAPI-Cache[redis]
  
### Как запустить проект:

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

### Примеры запросов API:
* Создание нового пользователя:
  
  - apps/users/create
```
    {
      "username": "string"
    }

``` 
* Получение списка всех юзеров: 

  - apps/users
```
[
  {
    "username": "string",
    "id": 0
  }
]

``` 

* Получить отдельную публикацию: 

  - apps/post/get_post

```
    {
        "id": 0,
        "title": "string",
        "body": "string",
        "user_id": 0
    }    

```

* Все доступные запросы можно посмотреть в сваггере

### Автор:
Тимур Машков

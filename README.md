# Скрипт для загрузки таможенных деклараций Elektronik Ticaret Gümrük Beyannamesi (ETGB) для продавцов из Турции.

## Требования перед запуском:

- Используй Poetry (или другую библиотеку) для установки зависимостей;
```python
poetry install
```
- Для работы на локальной машине должен быть установлен [Docker](https://www.docker.com)
- Необходимо заполнить файл .env по примеру в файле .env_example

Поднимаем базу с помощью Docker:
```
docker-compose up
```
## Описание 
- Скрипт script.py обращается к API OZON-SELLER, и загружает данные о ETGB за последние 4 дня в докерезированную базу Clickhouse.
- Endpoint к базе реализован на FastAPi.

Для запуска скрипта:
````
python3 scrip.py
````

Для доступа к endpoint:
````
uvicorn main:app
````


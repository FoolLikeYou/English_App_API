# English_App_API
Это API  с админ-панелью в браузере для приложения по изучению английского языка.
http://<HOST>/api/v1/test_api/<api_method>/<id>

Инструкция для локального запуска без контейнера:

Запустить команду в своем виртуальном окружении 
pip install -r requirements.txt
pip install Pillow 

Установить переменные окружения:
DJANGO_ALLOWED_HOSTS = ...  хосты с которых работает приложение (через пробел)
SECRET_KEY = ... 
API_SECRET =...
или 
API_SECRET = '' для менеджмента секретов (header:  secret) из админ-панели

1)для хранения медиа файлов локально 
DEBUG = 1

2)для хранения медиа файлов удаленно(AWS https://aws.amazon.com/s3/)
DEBUG = 0
AWS_ACCESS_KEY_ID = ...
AWS_SECRET_ACCESS_KEY = ...
AWS_STORAGE_BUCKET_NAME = ... 

В корне проекта выполнить команды:

python manage.py makemigrations
python manage.py migrate

эти две команды выполнять миграцию в sqlite, дефолтную бд для django
При необходимости сменить бд, измените настройку DATABASE в файле settings.py (https://docs.djangoproject.com/en/3.0/ref/settings/#databases)

создайте админ-пользователя для работы с админ-панелью 
python manage.py createsuperuser  

запустите сервер 
python manage.py runserver


Инструкция для локального запуска в контейнере:

Установить переменные окружения:
Создать файл web.env и добавить:
DEBUG=0
SECRET_KEY = ...
API_SECRET = ... ( или API_SECRET="")
DOCKER_LOCAL=1
DJANGO_ALLOWED_HOSTS = ...
DJANGO_SETTINGS_MODULE = test_api.settings
SQL_ENGINE = django.db.backends.postgresql
SQL_DATABASE = (1)
SQL_USER = (2)
SQL_PASSWORD = test_api
SQL_HOST = db
SQL_PORT = 5432
AWS_ACCESS_KEY_ID = ...
AWS_SECRET_ACCESS_KEY = ...
AWS_STORAGE_BUCKET_NAME = ...

Создать файл db.env и добавить:
POSTGRES_DB =  (1)
POSTGRES_USER = (2)
POSTGRES_PASSWORD = (3)


собираем докер: 
docker-compose build 

создайте админ-пользователя для работы с админ-панелью:
docker exec -it <container_id> python manage.py createsuperuser

запускаем:
docker-compose up -d


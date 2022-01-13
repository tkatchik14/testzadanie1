# Тестовое задание 
## Настройка БД
* Изменить настройки подключения к БД на свои в **settings.py**

   
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'nsi',
            'USER': 'nsi_user',
            'PASSWORD': 'nsi',
            'HOST': '192.168.218.159',
            'PORT': '5454',
        }
    }

* Для создания БД надо выполнить **script_db.sql**
* Для создания таблиц и наполнения тестовыми данными выполнить **tables.sql**
* Выполнить миграции

## Описание API
* По адресу  http://127.0.0.1:8000/api/dictionaries будет доступен список справочников
* По адресу http://127.0.0.1:8000/api/dictionaries/?format=api&date=2022-01-1 (параметр date) будет доступен список справочников, актуальных на указанную дату
* По адресу http://127.0.0.1:8000/api/dictionaryitem/?format=api&id=GENDER
(параметр id, значения: GENDER/ SOCSTATUS/ TEST1) будет доступен список элементов заданного справочника текущей версии
* По адресу http://127.0.0.1:8000/api/dictionaryitem/?format=api&id=GENDER&version=1.0
(параметры id, version) будет доступен список элементов заданного справочника указанной версии



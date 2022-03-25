Для установки установите все зависимости из файла requirements.txt
```pip install -r requirements.txt```

После чего произвести первоначальную настройку проекта
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Перейдите по ардресу http://127.0.0.1:8000/ в своём браузере
# django-rest
Simple Django Rest Framework Example

# How To Use

Firstly, you should install **django** and **djangorestframework**
```
pip install django
```
```
pip install djangorestframework
```

After installation download the project files and migrate. Don't forget to going project directory before migration.

```
python manage.py migrate
```

Then create a superuser for using API functions
```
python manage.py createsuperuser --email admin@admin.com --username admin
```

Finally, run server.
```
python manage.py runserver
```


You can see the sample drivers at http://127.0.0.1:8000/drivers/

Also you can create, read, update and delete drivers. 

For delete and update functions you should go to the specific drivers link, for example: http://127.0.0.1:8000/drivers/1/

# install

OS : Windows10

```bash
> python -m venv venv
> venv\Scripts\activate

(venv)> pip install django
(venv)> pip install django-crontab
(venv)> pip freeze > requirements.txt
```

# settings

```bash
(venv)> django-admin startproject source
(venv)> cd source
(venv)> django-admin startapp app
```

# execute

```bash
(venv)> python manage.py crontab add

(venv)> python mangge.py runserver
or 
(venv)> 
```
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

- linux local

    ```bash
    (venv)> python manage.py crontab add
    (venv)> python mangge.py runserver
    ```

- docker

    ```bash
    (venv)> docker-compose -f docker-compose.yml up -d --build
    ```
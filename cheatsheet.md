# Cheat Sheet

## Capistrano

Run cap

    bundle exec cap production deploy

## Server

Kill processes by name

    sudo pkill gunicorn

Restart a service

    sudo systemctl restart gunicorn

## Gunicorn

Add log file (gunicorn.conf)

    ExecStart=/bin/sh -c "/usr/local/bin/gunicorn -w 3 djangotodo.wsgi --log-file=/home/django/project/gunicorn.log --log-level=error"

## Django

Check configuration

    python3 manage.py check --deploy

Define admin super user

    python3 manage.py createsuperuser
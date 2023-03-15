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

## Misc

ruby net-ssh on Windows use Pageant as ssh-agent, it should be installed on the local computer if deployment is started from Windows (git bash for example).
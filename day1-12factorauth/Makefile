run:
    python manage.py runserver

migrations:
    python manage.py makemigrations

migrate:
    python manage.py migrate

deploy:
    pip install -r requirements/production.txt
    python manage.py migrate
    python manage.py collectstatic --noinput
    gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
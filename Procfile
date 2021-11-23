release: python manage.py migrate --no-input
web: gunicorn academy.wsgi:application --log-file -

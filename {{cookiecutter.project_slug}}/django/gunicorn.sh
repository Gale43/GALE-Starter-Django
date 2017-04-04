#!/bin/sh
#
# uncomment depending on your project
#
# python /app/manage.py collectstatic --noinput
# python /app/manage.py migrate --noinput

if [ -z "$DJANGO_DEBUG" ] && [ "$DJANGO_DEBUG" == "true" ]; then
    /usr/local/bin/gunicorn config.wsgi -w 4 -b 0.0.0.0:5000 --chdir=/app --reload
else
    /usr/local/bin/gunicorn config.wsgi -w 4 -b 0.0.0.0:5000 --chdir=/app
fi

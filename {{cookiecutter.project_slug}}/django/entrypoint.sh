#!/bin/bash
set -e
cmd="$@"

if [ -z "$REDIS_URL" ]; then
    export REDIS_URL=redis://redis:6379
fi

if [ -z "$DATABASE_URL" ]; then
    export DATABASE_URL=postgres://postgres:postgres@postgres:5432/postgres
fi

function postgres_ready(){
python << END
import sys
import psycopg2
try:
    conn = psycopg2.connect("$DATABASE_URL")
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing..."

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

# Useful for debugging
# exec $cmd

#!/bin/bash
set -e
cmd="$@"

if [ -z "$REDIS_URL" ]; then
    export REDIS_URL=redis://redis:6379
fi

if [ -z "$DATABASE_URL" ]; then
    export DATABASE_URL=postgres://postgres:postgres@postgres:5432/postgres
fi

{% if cookiecutter.use_tasks == 'y' %}
export CELERY_BROKER_URL=$REDIS_URL/0
{% endif %}


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
exec $cmd

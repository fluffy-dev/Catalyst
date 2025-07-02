#!/bin/sh

echo "Celery worker waiting for postgres..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 0.1
done
echo "PostgreSQL started for Celery worker"

exec "$@"
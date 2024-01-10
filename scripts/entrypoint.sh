#!/usr/bin/env bash

set -env

RUN_MANAGE_PY="poetry run python src/manage.py"

echo 'Collecting static files...'
$RUN_MANAGE_PY collectstatic --no-input

echo  'Running migration...'
$RUN_MANAGE_PY migrate --no-input

exec poetry run src.config.wsgi:application -p 8000 -b 0.0.0.0

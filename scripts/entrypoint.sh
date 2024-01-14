#!/usr/bin/env bash

set -e

RUN_MANAGE_PY="poetry run python src/manage.py"

echo 'Collecting static files...'
$RUN_MANAGE_PY collectstatic --no-input

echo  'Running migration...'
$RUN_MANAGE_PY migrate --no-input
$RUN_MANAGE_PY makemigrations --no-input

$RUN_MANAGE_PY runserver 0.0.0.0:8000

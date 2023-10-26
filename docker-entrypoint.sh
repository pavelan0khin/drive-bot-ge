#!/bin/sh
set -e
set -x

export PYTHONUNBUFFERED=0


case "$1" in
    web)
        poetry run python src/manage.py migrate --noinput
        poetry run python src/manage.py collectstatic --noinput
        gunicorn --env DJANGO_SETTINGS_MODULE=drive.app.settings \
          drive.app.wsgi --preload \
          -b 0.0.0.0:8000 -t60 -w "${CONCURRENCY:-5}"
    ;;
    grpc)
        python -m drive.server_grpc.server
    ;;
    celery_worker)
        poetry run celery -A drive.app worker -l INFO --concurrency=1
    ;;
    celery_beat)
        poetry run celery -A drive.app beat -l INFO -s /tmp/celerybeat-schedule
    ;;
    flower)
        poetry run celery -A drive.app flower --address=0.0.0.0 --basic-auth="$FLOWER_USER_LOGIN":"$FLOWER_USER_PASSWORD"
    ;;
    *)
        exec $@
    ;;
esac

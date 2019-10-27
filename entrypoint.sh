#!/bin/bash

set -e

show_help() {
    echo """
Usage: docker run <imagename> COMMAND
Commands
dev     : Start a normal Django development server.
lint    : Run pylint.
manage  : Start manage.py
prod    : Run uwsgi server.
test    : Run tests
help    : Show this message
"""
}

prepare() {
    until nc -z "$MYSQL_HOST" "$MYSQL_PORT"; do sleep 1; done;
}

# Run
case "$1" in
    dev)
        prepare
        make migrate
        python3 manage.py runserver 0.0.0.0:8000
    ;;
    lint)
        make lint
    ;;
    test)
        make test
    ;;
    manage)
        python3 manage.py "${@:2}"
    ;;
    prod)
        uwsgi --ini uwsgi.ini
    ;;
    celery)
        prepare
        celery -A notify worker
    ;;
    *)
        "$@"
    ;;
esac

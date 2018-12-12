#!/usr/bin/env bash
# export APP_ENV="local"
export APP_ENV="stag"
# export APP_ENV="prod"

function start () {
    source .venv/python3/bin/activate
    gunicorn -b 127.0.0.1:5000 --reload app.main:application
}

function stop () {
    ps -ef | grep gunicorn | awk '{print $2}' | xargs kill -9
}

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    *)
    echo "Usage: run.sh {start|stop}"
    exit 1
esac

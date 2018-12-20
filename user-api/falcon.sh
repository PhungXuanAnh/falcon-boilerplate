#!/usr/bin/env bash
export APP_ENV="local"
# export APP_ENV="stag"
# export APP_ENV="prod"

function start () {
    gunicorn -b 127.0.0.1:5000 --reload app.main:application
}

function stop () {
    ps -ef | grep gunicorn | awk '{print $2}' | xargs kill -9
}

function db() {
    case "$2" in
        migrate)
            if [[ $3 == '' ]]
            then
                echo 'Usage: falcon.sh migrate "some messages"'
                exit 1
            fi        
            alembic revision --autogenerate -m $3
            ;;
        make-migrations)
            alembic upgrade head
            ;;
        *)
        echo "Usage: falcon.sh db {migrate|make-migrations}"
        exit 1
    esac
}

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    db)
        db $@
        ;;
    *)
    echo "Usage: falcon.sh {start|stop|db}"
    exit 1
esac

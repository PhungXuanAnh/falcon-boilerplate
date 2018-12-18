from logging.config import dictConfig
from celery import Celery
from config import RABBITMQ_HOST, WORKER_QUEUE, LOGGING

# dictConfig(LOGGING)

NAME = 'user-api'
BROKER_URL = 'amqp://guest@{rabittmq_host}//'.format(rabittmq_host=RABBITMQ_HOST)

app = Celery(NAME, broker=BROKER_URL)

app.conf.update(
    task_default_queue=WORKER_QUEUE,
    task_queue_max_priority=10,
    worker_prefetch_multiplier=4,
    task_acks_late=True,
    enable_utc=True,
    imports=['utils.tasks',],
)

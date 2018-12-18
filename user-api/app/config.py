# -*- coding: utf-8 -*-

import os
import configparser


BRAND_NAME = 'Falcon REST API Template'

SECRET_KEY = 'xs4G5ZD9SwNME6nWRWrK_aq6Yb9H8VJpdwCzkTErFPw='
UUID_LEN = 10
UUID_ALPHABET = ''.join(map(chr, range(48, 58)))
TOKEN_EXPIRES = 3600

# ==================== DATABASE ===========================================
POSTGRES_HOST = os.getenv('POSTGRES_HOST', '127.0.0.1')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'my_database1')
POSTGRES_USER = os.getenv('POSTGRES_USER', 'root')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', '123456')
DATABASE_ECHO = os.getenv('DATABASE_ECHO', 'yes')

DATABASE_URL = "postgresql+psycopg2://{user}:{password}@{host}/{database}".format(
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    database=POSTGRES_DB
)
DB_ECHO = True if DATABASE_ECHO == 'yes' else False
DB_AUTOCOMMIT = True

# ==================== RABBITMQ ===========================================
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', '127.0.0.1')
RABBITMQ_PORT = os.getenv('RABBITMQ_PORT', 5672)
PUBLIC_EVENT_QUEUE = os.getenv('PUBLIC_EVENT_QUEUE', 'public_event')
WORKER_QUEUE = os.getenv('WORKER_QUEUE', 'worker')

# ==================== RABBITMQ ===========================================
REDIS_HOST = os.getenv('REDIS_URL', '127.0.0.1')
REDIS_PORT = os.getenv('REDIS_URL', 6379)
REDIS_URL = "redis://{host}:{port}".format(host=REDIS_HOST, port=REDIS_PORT)

# ==================== LOGGING ============================================
LOG_LEVEL = os.getenv('LOGGING_LEVEL', 'DEBUG')
# TODO: add slack api key below
LOGGING_SLACK_API_KEY = ""
LOGGING_SLACK_CHANNEL = "#general"
LOG_DIR = 'log'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] [%(module)s.%(funcName)s:%(lineno)d] %(levelname)s: %(message)s"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'app.DEBUG': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': LOG_DIR + '/app.DEBUG.log',
            'maxBytes': 5 * 1024 * 1024,  # 1Kb       #100 * 1024 * 1024,  # 100Mb
            'backupCount': 3,
        },
        'app.INFO': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': LOG_DIR + '/app.INFO.log',
            'maxBytes': 5 * 1024 * 1024,  # 1Kb       #100 * 1024 * 1024,  # 100Mb
            'backupCount': 3,
        },
        'app.ERROR': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': LOG_DIR + '/app.ERROR.log',
            'maxBytes': 5 * 1024 * 1024,  # 1Kb       #100 * 1024 * 1024,  # 100Mb
            'backupCount': 3,
        },
        'slack.ERROR': {
            'level': 'ERROR',
            'api_key': LOGGING_SLACK_API_KEY,
            'class': 'slacker_log_handler.SlackerLogHandler',
            'channel': LOGGING_SLACK_CHANNEL
        },
    },
    'loggers': {
        'app': {
            'handlers': ['app.INFO', 'slack.ERROR'] if LOG_LEVEL == 'INFO' else ['console', 'app.DEBUG', 'app.INFO', 'app.ERROR', 'slack.ERROR'],
            'propagate': False,
            'level': 'INFO',
        },
    }
}

# -*- coding: utf-8 -*-

import os
import configparser


BRAND_NAME = 'Falcon REST API Template'

SECRET_KEY = 'xs4G5ZD9SwNME6nWRWrK_aq6Yb9H8VJpdwCzkTErFPw='
UUID_LEN = 10
UUID_ALPHABET = ''.join(map(chr, range(48, 58)))
TOKEN_EXPIRES = 3600

# ==================== READ CONFIG FILE ===================================
APP_ENV = os.environ.get('APP_ENV', 'stag')
if APP_ENV == "local":
    INI_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                            '../../conf/{}.ini'.format(APP_ENV))
else:                           
    INI_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                            '../conf/{}.ini'.format(APP_ENV))

CONFIG = configparser.ConfigParser()
CONFIG.read(INI_FILE)

# ==================== DATABASE ===========================================
POSTGRES = CONFIG['postgres']
DB_CONFIG = (POSTGRES['user'], POSTGRES['password'], POSTGRES['host'], POSTGRES['database'])
DATABASE_URL = "postgresql+psycopg2://%s:%s@%s/%s" % DB_CONFIG
DB_ECHO = True if CONFIG['database']['echo'] == 'yes' else False
DB_AUTOCOMMIT = True

# ==================== LOGGING ============================================
LOG_LEVEL = CONFIG['logging']['level']
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

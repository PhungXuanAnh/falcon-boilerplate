# -*- coding: utf-8 -*-

import logging
from app import config

logging.config.dictConfig(config.LOGGING)
LOG = logging.getLogger('app')


def init():
    from app.api import API
    from app.utils.database import db_session, init_session
    from app.middleware import AuthHandler, JSONTranslator, DatabaseSessionManager

    init_session()
    middleware = [AuthHandler(), JSONTranslator(), DatabaseSessionManager(db_session)]
    application = API(middleware=middleware)

    LOG.info('API Server is starting')

    return application


application = init()

if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server('127.0.0.1', 5000, application)
    httpd.serve_forever()

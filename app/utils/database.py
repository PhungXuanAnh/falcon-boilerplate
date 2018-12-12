# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import DeclarativeMeta

import json
import time
import datetime

from app import log
from app import config

LOG = log.get_logger()


def get_engine(uri):
    LOG.info('Connecting to database..')
    options = {
        'pool_recycle': 3600,
        'pool_size': 10,
        'pool_timeout': 30,
        'max_overflow': 30,
        'echo': config.DB_ECHO,
        'execution_options': {
            'autocommit': config.DB_AUTOCOMMIT
        }
    }
    return create_engine(uri, **options)


db_session = scoped_session(sessionmaker())
engine = get_engine(config.DATABASE_URL)


def init_session():
    db_session.configure(bind=engine)

    from app.model import Base
    Base.metadata.create_all(engine)


def new_alchemy_encoder():
    # http://stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json
    _visited_objs = []

    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                # don't re-visit self
                if obj in _visited_objs:
                    return None
                _visited_objs.append(obj)

                # an SQLAlchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                    fields[field] = obj.__getattribute__(field)
                # a json-encodable dict
                return fields

            return json.JSONEncoder.default(self, obj)
    return AlchemyEncoder


def passby(data):
    return data


def datetime_to_timestamp(date):
    if isinstance(date, datetime.date):
        return int(time.mktime(date.timetuple()))
    else:
        return None

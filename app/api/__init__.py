# -*- coding: utf-8 -*-

import falcon
import logging
from .common import BaseResource
from .v1 import *
from app.api.common import base
from app.api.v1 import users
from app.errors import AppError

LOG = logging.getLogger('app')


class API(falcon.API):

    def __init__(self, *args, **kwargs):
        super(API, self).__init__(*args, **kwargs)

        self.add_route('/', base.BaseResource())
        self.add_route('/v1/users', users.Collection())
        self.add_route('/v1/users/{user_id}', users.Item())
        self.add_route('/v1/users/self/login', users.Self())

        self.add_error_handler(AppError, AppError.handle)

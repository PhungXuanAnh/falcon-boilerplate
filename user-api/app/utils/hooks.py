# -*- coding: utf-8 -*-

import falcon
from app.utils.errors import UnauthorizedError
from cerberus import Validator, ValidationError
from app.utils.errors import InvalidParameterError


FIELDS = {
    'username': {
        'type': 'string',
        'required': True,
        'minlength': 4,
        'maxlength': 20
    },
    'email': {
        'type': 'string',
        'regex': '[a-zA-Z0-9._-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,4}',
        'required': True,
        'maxlength': 320
    },
    'password': {
        'type': 'string',
        'regex': '[0-9a-zA-Z]\w{3,14}',
        'required': True,
        'minlength': 8,
        'maxlength': 64
    },
    'info': {
        'type': 'dict',
        'required': False
    }
}


def validate_user_create(req, res, resource, params):
    schema = {
        'username': FIELDS['username'],
        'email': FIELDS['email'],
        'password': FIELDS['password'],
        'info': FIELDS['info']
    }

    v = Validator(schema)
    try:
        if not v.validate(req.context['data']):
            raise InvalidParameterError(v.errors)
    except ValidationError:
        raise InvalidParameterError('Invalid Request %s' % req.context)


def auth_required(req, resp, resource, params):
    if req.context['auth_user'] is None:
        raise UnauthorizedError()

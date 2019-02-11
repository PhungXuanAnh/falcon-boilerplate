from falcon_auth import TokenAuthBackend, JWTAuthBackend

SECRET_KEY_for_JWT = 'secret_key_123'
user_for_test = {
    'id': 123456789,
    'username': 'name123',
    'password': 'password123'
}


def user_loader_basic(username, password):
    print('Basic auth: server received username: {} and password: {}'.format(username, password))
    return user_for_test


def user_loader_token(token):
    print('Token auth: server received token: {}'.format(token))
    return user_for_test


def user_loader_jw_token(payload):
    print('JWT auth: server received jwt token: {}'.format(payload))
    return user_for_test


class Item1(object):
    def on_get(self, req, resp):
        resp.body = 'This api does not require authentication'


class Item2(object):
    def on_get(self, req, resp):
        user = req.context['user']
        resp.body = "This api uses Basic authentication, return user: {}".format(user) +\
                    "\nCheck servers logs for detail how to get Auth information"


class Item3(object):
    auth = {
        'backend': TokenAuthBackend(user_loader_token),
        'exempt_methods': ['POST']
    }

    def on_get(self, req, resp):
        user = req.context['user']
        resp.body = "This api use Token authentication, return user: {}".format(user) +\
                    "\nCheck servers logs for detail how to get Auth information"

    def on_post(self, req, resp):
        resp.body = "This api doesn't use token authentication"


class Item4(object):
    auth = {
        'backend': JWTAuthBackend(user_loader_jw_token, SECRET_KEY_for_JWT)
    }

    def on_get(self, req, resp):
        user = req.context['user']
        resp.body = "This api use jwt token authentication, return user: {}".format(user) +\
                    "\nCheck servers logs for detail how to get Auth information"


class Item5(object):
    auth = {
        'auth_disabled': True
    }

    def on_get(self, req, resp):
        resp.body = 'This api disabled authentication'

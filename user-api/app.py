import falcon
import users
from falcon_auth import FalconAuthMiddleware, BasicAuthBackend


auth_backend = BasicAuthBackend(users.user_loader_basic)
auth_middleware = FalconAuthMiddleware(auth_backend,
                                       exempt_routes=['/item1'])

api = falcon.API(middleware=auth_middleware)
api.add_route('/item1', users.Item1())
api.add_route('/item2', users.Item2())
api.add_route('/item3', users.Item3())
api.add_route('/item4', users.Item4())
api.add_route('/item5', users.Item5())

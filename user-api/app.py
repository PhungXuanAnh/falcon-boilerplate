import falcon
import users

api = falcon.API()
api.add_route('/users', users.Collection())

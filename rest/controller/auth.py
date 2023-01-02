from flask.views import MethodView
from flask_smorest import Blueprint

from rest.schema.auth import AccessTokenSchema, UserSchemaLogin
from rest.schema.message import MessageSchemaOK
from rest.service.AuthService import get_access_token
from rest.service.UserService import createUser

blp = Blueprint('auth', __name__, description='Registration and login endpoints')


@blp.route('/signup')
class SignUpBlueprint(MethodView):

    @blp.arguments(UserSchemaLogin)
    @blp.response(201, MessageSchemaOK)
    def post(self, user):
        createUser(user)
        return {'status': 'OK'}


@blp.route('/login')
class LoginBlueprint(MethodView):

    @blp.arguments(UserSchemaLogin)
    @blp.response(201, AccessTokenSchema)
    def post(self, user):
        return get_access_token(user)

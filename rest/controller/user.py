from flask.views import MethodView
from flask_smorest import Blueprint

from rest.schema.user import UserSchema
from rest.schema.message import MessageSchemaOK
from rest.service.UserService import createUser

blp = Blueprint('user', __name__, url_prefix='users', description='Operations on User')


@blp.route('/')
class UserBlueprint(MethodView):

    @blp.arguments(UserSchema)
    @blp.response(201, MessageSchemaOK)
    def post(self, user):
        createUser(user)
        return {'status': 'OK'}

from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from rest.schema.auth import UserSchema
from rest.service.UserService import getAllUsers

blp = Blueprint('user', __name__, url_prefix='users', description='Operations on User')


@blp.route('/')
class UserBlueprint(MethodView):

    @jwt_required()
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return getAllUsers()

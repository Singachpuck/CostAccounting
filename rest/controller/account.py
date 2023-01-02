from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_smorest import Blueprint, abort

from rest.schema.account import AccountSchema
from rest.schema.message import MessageSchemaOK
from rest.service.AccountService import getAllAccounts, createAccount
from rest.service.UserService import getUserById

blp = Blueprint('account', __name__, url_prefix='accounts', description='Operations on Account')


@blp.route('/')
class AccountBlueprint(MethodView):

    @jwt_required()
    @blp.response(200, AccountSchema(many=True))
    def get(self):
        return getAllAccounts()

    @jwt_required()
    @blp.arguments(AccountSchema)
    @blp.response(201, MessageSchemaOK)
    def post(self, account):
        user = getUserById(get_jwt_identity())
        if user.id != account['user']:
            abort(403, message=f'You can\'t create account for user {account["user"]}')
        createAccount(account)
        return {'status': 'OK'}

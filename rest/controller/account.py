from flask.views import MethodView
from flask_smorest import Blueprint

from rest.schema.account import AccountSchema
from rest.schema.message import MessageSchemaOK
from rest.service.AccountService import getAllAccounts, createAccount

blp = Blueprint('account', __name__, url_prefix='accounts', description='Operations on Account')


@blp.route('/')
class AccountBlueprint(MethodView):

    @blp.response(200, AccountSchema(many=True))
    def get(self):
        return getAllAccounts()

    @blp.arguments(AccountSchema)
    @blp.response(201, MessageSchemaOK)
    def post(self, account):
        createAccount(account)
        return {'status': 'OK'}

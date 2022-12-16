from flask.views import MethodView
from flask_smorest import Blueprint, abort

from rest.schema.category import CategoryQuerySchema
from rest.schema.message import MessageSchemaOK
from rest.schema.transaction import TransactionSchema
from rest.service.TransactionService import createTransaction, getTransactionsByUserIdAndCategory, \
    getTransactionsByUserId

blp = Blueprint('transaction', __name__, description='Operations on transactions')


@blp.route('/transactions')
class TransactionBlueprint(MethodView):

    @blp.arguments(TransactionSchema)
    @blp.response(201, MessageSchemaOK)
    def post(self, transaction):
        try:
            createTransaction(transaction)
        except AttributeError as e:
            abort(400, message=e.args[0])

        return {'status': 'OK'}


@blp.route('/users/<int:user_id>/transactions')
class UserTransactionBlueprint(MethodView):

    @blp.arguments(CategoryQuerySchema, location='query', as_kwargs=True)
    @blp.response(200, TransactionSchema(many=True))
    def get(self, **kwargs):
        user_id = kwargs['user_id']
        try:
            if 'category' in kwargs:
                getTransactionsByUserIdAndCategory(user_id, kwargs['category'])
        except AttributeError as e:
            abort(400, message=e.args[0])

        return getTransactionsByUserId(user_id)

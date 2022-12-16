from flask.views import MethodView
from flask_smorest import Blueprint

from rest.schema.category import CategorySchema
from rest.schema.message import MessageSchemaOK
from rest.service.CategoryService import getAllCategories, createCategory

blp = Blueprint('category', __name__, url_prefix='/categories', description='Operations on category')


@blp.route('/')
class CategoryBlueprint(MethodView):

    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return getAllCategories()

    @blp.arguments(CategorySchema)
    @blp.response(201, MessageSchemaOK)
    def post(self, category):
        createCategory(category)
        return {'status': 'OK'}

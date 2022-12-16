from rest import db
from rest.dao.CategoryDao import CategoryDao
from rest.model.Category import Category


class CategoryDaoORM(CategoryDao):

    def getCategories(self) -> list[Category]:
        return db.session.query(Category).all()

    def getCategoryByName(self, name) -> Category:
        return db.session.query(Category).filter_by(name=name).first()

    def getCategoryById(self, id) -> Category:
        return db.session.query(Category).get(id)

    def createCategory(self, category: Category) -> None:
        db.session.add(category)
        db.session.commit()

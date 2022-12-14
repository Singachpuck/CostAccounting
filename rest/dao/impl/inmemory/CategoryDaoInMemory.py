from rest.dao.CategoryDao import CategoryDao
from rest.model.Category import Category

categories = [
    Category(1, "Grocery"),
    Category(2, "Tourism"),
    Category(3, "Education"),
    Category(4, "Entertainment"),
    Category(5, "Sport")
]


class CategoryDaoInMemory(CategoryDao):

    def __generateId(self):
        return max(categories, key=lambda category: category.id).id + 1

    def getCategories(self) -> list[Category]:
        return list(categories)

    def getCategoryByName(self, name) -> Category:
        for category in categories:
            if category.name == name:
                return category

        raise AttributeError(f'Category {name} doesn\'t exist')

    def getCategoryById(self, id) -> Category:
        for category in categories:
            if category.id == id:
                return category

        raise AttributeError(f'Category with id {id} doesn\'t exist')

    def createCategory(self, category: Category) -> None:
        if category.id is None:
            category.id = self.__generateId()
        elif category.id in [c.id for c in categories]:
            raise AttributeError(f'Category with id {category.id} already exists')

        categories.append(category)

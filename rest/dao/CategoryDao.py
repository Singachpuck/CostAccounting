from rest.model.Category import Category


class CategoryDao:

    def getCategories(self) -> list[Category]:
        raise NotImplementedError()

    def getCategoryByName(self, name) -> Category:
        raise NotImplementedError()

    def getCategoryById(self, id) -> Category:
        raise NotImplementedError()

    def createCategory(self, category: Category) -> None:
        raise NotImplementedError()

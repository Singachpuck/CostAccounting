from rest.dao.impl.orm.CategoryDaoORM import CategoryDaoORM
from rest.model.Category import Category

categoryDao = CategoryDaoORM()


def getAllCategories():
    return list(map(lambda category: category.to_dict(), categoryDao.getCategories()))


def getCategoryByName(name):
    return categoryDao.getCategoryByName(name)


def getCategoryById(id):
    return categoryDao.getCategoryById(id)


def createCategory(data):
    newCategory = Category(name=data['name'])
    categoryDao.createCategory(newCategory)

from rest.dao.CategoryDao import getCategories, getCategoryByName as getByName, createCategory as create, \
    getCategoryById as getById
from rest.model.Category import Category


def getAllCategories():
    return list(map(lambda category: category.__dict__, getCategories()))


def getCategoryByName(name):
    return getByName(name)


def getCategoryById(id):
    return getById(id)


def createCategory(data):
    newCategory = Category(name=data['name'])
    create(newCategory)

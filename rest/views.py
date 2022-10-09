from flask import jsonify, request

from rest import app
from rest.service.CategoryService import getAllCategories, createCategory as createCategoryService
from rest.service.TransactionService import getTransactionsByUserId, getTransactionsByUserIdAndCategory, createTransaction as createTransactionService
from rest.service.UserService import createUser as createUserService

BASE_URL = '/api/v1'


@app.route(BASE_URL + '/categories')
def getCategories():
    return jsonify(getAllCategories())


@app.route(BASE_URL + '/users/<int:userId>/transactions')
def getUserTransactions(userId):
    try:
        if 'category' in request.args:
            return jsonify(getTransactionsByUserIdAndCategory(userId, request.args['category']))
    except AttributeError as e:
        return {'status': 'KO', 'message': e.args[0]}, 400
    return jsonify(getTransactionsByUserId(userId))


@app.route(BASE_URL + '/transactions', methods=['POST'])
def createTransaction():
    data = request.get_json()
    if data is None or 'userId' not in data or 'categoryId' not in data or 'amount' not in data:
        return {'status': 'KO', 'message': 'Bad Request'}, 400
    try:
        createTransactionService(data)
    except AttributeError as e:
        return {'status': 'KO', 'message': e.args[0]}, 400
    return {'status': 'OK'}, 201


@app.route(BASE_URL + '/users', methods=['POST'])
def createUser():
    data = request.get_json()
    if data is None or 'name' not in data:
        return {'status': 'KO', 'message': 'Bad Request'}, 400
    createUserService(data)
    return {'status': 'OK'}, 201


@app.route(BASE_URL + '/categories', methods=['POST'])
def createCategory():
    data = request.get_json()
    if data is None or 'name' not in data:
        return {'status': 'KO', 'message': 'Bad Request'}, 400
    createCategoryService(data)
    return {'status': 'OK'}, 201

from flask import Blueprint, jsonify, abort, request
from db import update_record, create_record

app_test = Blueprint('test', __name__)
test_set = [
    {
        "Id": 1,
        "Name": 'Проверка входных данных',
        "IsImportant": True
    },
    {
        "Id": 2,
        "Name": 'Проверка выходных данных',
        "IsImportant": True
    },
    {
        "Id": 3,
        "Name": 'Классы входных данных',
        "IsImportant": True
    },
    {
        "Id": 4,
        "Name": 'Классы выходных данных',
        "IsImportant": True
    },
    {
        "Id": 5,
        "Name": 'Тестирование времени работы',
        "IsImportant": False
    }
]
test_class = {
    'Id': int,
    'Name': str,
    'IsImportant': bool
}

@app_test.route('/', methods=['GET'])
def get_test_set():
    return jsonify(test_set)

@app_test.route('/', methods=['POST'])
def create_test():
    if not request.json:
        abort(400)
    test = { 'Id': test_set[-1]['Id'] + 1 if len(test_set) else 1 }
    create_record(test_class, request, test)
    test_set.append(test)
    return jsonify(test), 201

@app_test.route('/<int:test_id>', methods = ['GET'])
def get_test(test_id):
    tests = list(filter(lambda t: t['Id'] == test_id, test_set))
    if len(tests) == 0:
        abort(404)
    return jsonify(tests[0])

@app_test.route('/<int:test_id>', methods=['PUT'])
def update_test(test_id):
    tests = [test for test in test_set if test['Id'] == test_id]
    if len(tests) == 0 or not request.json:
        abort(404)
    test = tests[0]
    update_record(test_class, request, test)
    return jsonify(test)

@app_test.route('/<int:test_id>', methods=['DELETE'])
def delete_test(test_id):
    tests = [test for test in test_set if test['Id'] == test_id]
    if len(tests) == 0:
        abort(404)
    test_set.remove(tests[0])
    return jsonify({'Result': True})

from flask import Blueprint, jsonify, abort, request, make_response, url_for

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

@app_test.route('/', methods=['GET'])
def get_test_set():
    return jsonify({'test': test_set})

@app_test.route('/', methods=['POST'])
def create_test():
    if not request.json or not 'title' in request.json:
        abort(400)
    test = {
        'Id': test_set[-1]['Id'] + 1,
        'Name': request.json['Name'],
        'IsImportant': request.json['IsImportant']
    }
    test_set.append(test)
    return jsonify({'test': test}), 201

@app_test.route('/<int:test_id>', methods = ['GET'])
def get_test(test_id):
    tests = list(filter(lambda t: t['Id'] == test_id, test_set))
    if len(tests) == 0:
        abort(404)
    return jsonify( { 'test': tests[0] } )

@app_test.route('/<int:test_id>', methods=['PUT'])
def update_test(test_id):
    tests = [test for test in test_set if test['Id'] == test_id]
    if len(tests) == 0 or not request.json:
        abort(404)
    test = tests[0]
    test['Name'] = request.json.get('Name', test['Name'])
    test['IsImportant'] = request.json.get('IsImportant', test['IsImportant'])
    return jsonify({'test': test})

@app_test.route('/<int:test_id>', methods=['DELETE'])
def delete_test(test_id):
    tests = [test for test in test_set if test['Id'] == test_id]
    if len(tests) == 0:
        abort(404)
    test_set.remove(tests[0])
    return jsonify({'result': True})

from flask import Blueprint, jsonify, abort, request
from db import update_record, create_record

app_manager = Blueprint('manager', __name__)
manager_set = [
    {
        "Id": 1,
        "Name": 'Алексей',
        "Budget": 5000,
        "PassedDays": 5,
        "ProjectId": 1
    },
    {
        "Id": 2,
        "Name": 'Тестер',
        "Budget": 1000,
        "PassedDays": 15,
        "ProjectId": 1
    }
]
manager_class = {
    "Id": int,
    "Name": str,
    "Budget": int,
    "PassedDays": int,
    "ProjectId": int
}

@app_manager.route('/', methods=['GET'])
def get_manager_set():
    return jsonify(manager_set)

@app_manager.route('/', methods=['POST'])
def create_manager():
    if not request.json:
        abort(400)
    manager = { 'Id': manager_set[-1]['Id'] + 1 if len(manager_set) else 1 }
    create_record(manager_class, request, manager)
    manager_set.append(manager)
    return jsonify(manager), 201

@app_manager.route('/<int:manager_id>', methods = ['GET'])
def get_manager(manager_id):
    managers = list(filter(lambda t: t['Id'] == manager_id, manager_set))
    if len(managers) == 0:
        abort(404)
    return jsonify(managers[0])

@app_manager.route('/<int:manager_id>', methods=['PUT'])
def update_manager(manager_id):
    managers = [manager for manager in manager_set if manager['Id'] == manager_id]
    if len(managers) == 0 or not request.json:
        abort(404)
    manager = managers[0]
    update_record(manager_class, request, manager)
    return jsonify(manager)

@app_manager.route('/<int:manager_id>', methods=['DELETE'])
def delete_manager(manager_id):
    managers = [manager for manager in manager_set if manager['Id'] == manager_id]
    if len(managers) == 0:
        abort(404)
    manager_set.remove(managers[0])
    return jsonify({'Result': True})

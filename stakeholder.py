from flask import Blueprint, jsonify, abort, request
from db import update_record, create_record

app_stakeholder = Blueprint('stakeholder', __name__)
stakeholder_set = [
    {
        "Id": 1,
        "Name": 'Заказчик',
        "Type": 'Client',
        "IsMain": True
    },
    {
        "Id": 2,
        "Name": 'Заказчик',
        "Type": 'Client',
        "IsMain": True
    },
    {
        "Id": 3,
        "Name": 'Пользователи',
        "Type": 'Users',
        "IsMain": True
    }
]
stakeholder_class = {
    "Id": int,
    "Name": str,
    "Type": str,
    "IsMain": bool
}

@app_stakeholder.route('/', methods=['GET'])
def get_stakeholder_set():
    return jsonify(stakeholder_set)

@app_stakeholder.route('/', methods=['POST'])
def create_stakeholder():
    if not request.json:
        abort(400)
    stakeholder = { 'Id': stakeholder_set[-1]['Id'] + 1 if len(stakeholder_set) else 1 }
    create_record(stakeholder_class, request, stakeholder)
    stakeholder_set.append(stakeholder)
    return jsonify(stakeholder), 201

@app_stakeholder.route('/<int:stakeholder_id>', methods = ['GET'])
def get_stakeholder(stakeholder_id):
    stakeholders = list(filter(lambda t: t['Id'] == stakeholder_id, stakeholder_set))
    if len(stakeholders) == 0:
        abort(404)
    return jsonify(stakeholders[0])

@app_stakeholder.route('/<int:stakeholder_id>', methods=['PUT'])
def update_stakeholder(stakeholder_id):
    stakeholders = [stakeholder for stakeholder in stakeholder_set if stakeholder['Id'] == stakeholder_id]
    if len(stakeholders) == 0 or not request.json:
        abort(404)
    stakeholder = stakeholders[0]
    update_record(stakeholder_class, request, stakeholder)
    return jsonify(stakeholder)

@app_stakeholder.route('/<int:stakeholder_id>', methods=['DELETE'])
def delete_stakeholder(stakeholder_id):
    stakeholders = [stakeholder for stakeholder in stakeholder_set if stakeholder['Id'] == stakeholder_id]
    if len(stakeholders) == 0:
        abort(404)
    stakeholder_set.remove(stakeholders[0])
    return jsonify({'Result': True})

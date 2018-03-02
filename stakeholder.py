from flask import Blueprint, jsonify, abort, request, make_response, url_for

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

@app_stakeholder.route('/', methods=['GET'])
def get_stakeholder_set():
    return jsonify({'stakeholder': stakeholder_set})

@app_stakeholder.route('/', methods=['POST'])
def create_stakeholder():
    if not request.json or not 'title' in request.json:
        abort(400)
    stakeholder = {
        'Id': stakeholder_set[-1]['Id'] + 1,
        'Name': request.json['Time'],
        'Type': request.json['Type'],
        'IsMain': request.json['IsMain']
    }
    stakeholder_set.append(stakeholder)
    return jsonify({'stakeholder': stakeholder}), 201

@app_stakeholder.route('/<int:stakeholder_id>', methods = ['GET'])
def get_stakeholder(stakeholder_id):
    stakeholders = list(filter(lambda t: t['Id'] == stakeholder_id, stakeholder_set))
    if len(stakeholders) == 0:
        abort(404)
    return jsonify( { 'stakeholder': stakeholders[0] } )

@app_stakeholder.route('/<int:stakeholder_id>', methods=['PUT'])
def update_stakeholder(stakeholder_id):
    stakeholders = [stakeholder for stakeholder in stakeholder_set if stakeholder['Id'] == stakeholder_id]
    if len(stakeholders) == 0 or not request.json:
        abort(404)
    stakeholder = stakeholders[0]
    stakeholder['Name'] = request.json.get('Name', stakeholder['Name'])
    stakeholder['Type'] = request.json.get('Type', stakeholder['Type'])
    stakeholder['IsMain'] = request.json.get('IsMain', stakeholder['IsMain'])
    return jsonify({'stakeholder': stakeholder})

@app_stakeholder.route('/<int:stakeholder_id>', methods=['DELETE'])
def delete_stakeholder(stakeholder_id):
    stakeholders = [stakeholder for stakeholder in stakeholder_set if stakeholder['Id'] == stakeholder_id]
    if len(stakeholders) == 0:
        abort(404)
    stakeholder_set.remove(stakeholders[0])
    return jsonify({'result': True})

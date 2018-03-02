from flask import Blueprint, jsonify, abort, request, make_response, url_for

app_user = Blueprint('user', __name__)

user_set = [
    {
        "Id": 1,
        "Name": 'Алексей',
        "Budget": 5000,
        "Days": 5
    }
]

@app_user.route('/', methods=['GET'])
def get_user_set():
    return jsonify({'user': user_set})

@app_user.route('/', methods=['POST'])
def create_user():
    if not request.json or not 'title' in request.json:
        abort(400)
    user = {
        'Id': user_set[-1]['Id'] + 1,
        'Name': request.json['Name'],
        'Budget': request.json['Budget'],
        'Days': request.json['Days']
    }
    user_set.append(user)
    return jsonify({'user': user}), 201

@app_user.route('/<int:user_id>', methods = ['GET'])
def get_user(user_id):
    users = list(filter(lambda t: t['Id'] == user_id, user_set))
    if len(users) == 0:
        abort(404)
    return jsonify( { 'user': users[0] } )

@app_user.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    users = [user for user in user_set if user['Id'] == user_id]
    if len(users) == 0 or not request.json:
        abort(404)
    user = users[0]
    user['Name'] = request.json.get('Name', user['Name'])
    user['Budget'] = request.json.get('Budget', user['Budget'])
    user['Days'] = request.json.get('Days', user['Days'])
    return jsonify({'user': user})

@app_user.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    users = [user for user in user_set if user['Id'] == user_id]
    if len(users) == 0:
        abort(404)
    user_set.remove(users[0])
    return jsonify({'result': True})

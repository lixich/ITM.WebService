from flask import Blueprint, jsonify, abort, request, make_response, url_for

app_employee = Blueprint('employee', __name__)

employee_set = [
    {
        "Id": 1,
        "Name": 'Алексей',
        "AnalystSkill": 0,
        "AnalystCapacity": 0,
        "DeveloperSkill": 0,
        "DeveloperCapacity": 0,
        "TesterSkill": 0,
        "TesterCapacity": 0,
        "Salary": 0
    }
]

@app_employee.route('/', methods=['GET'])
def get_employee_set():
    return jsonify({'employee': employee_set})

@app_employee.route('/', methods=['POST'])
def create_employee():
    if not request.json or not 'title' in request.json:
        abort(400)
    employee = {
        'Id': employee_set[-1]['Id'] + 1,
        'Name': request.json['Time'],
        'AnalystSkill': request.json['AnalystSkill'],
        'AnalystCapacity': request.json['AnalystCapacity'],
        'DeveloperSkill': request.json['AnalystSkill'],
        'DeveloperCapacity': request.json['AnalystCapacity'],
        'TesterSkill': request.json['AnalystSkill'],
        'TesterCapacity': request.json['AnalystCapacity'],
        'Salary': request.json['AnalystSkill']
    }
    employee_set.append(employee)
    return jsonify({'employee': employee}), 201

@app_employee.route('/<int:employee_id>', methods = ['GET'])
def get_employee(employee_id):
    employees = list(filter(lambda t: t['Id'] == employee_id, employee_set))
    if len(employees) == 0:
        abort(404)
    return jsonify( { 'employee': employees[0] } )

@app_employee.route('/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    employees = [employee for employee in employee_set if employee['Id'] == employee_id]
    if len(employees) == 0 or not request.json:
        abort(404)
    employee = employees[0]
    employee['Name'] = request.json.get('Name', employee['Name'])
    employee['Type'] = request.json.get('Type', employee['Type'])
    employee['AnalystSkill'] = request.json.get('AnalystSkill', employee['AnalystSkill'])
    employee['AnalystCapacity'] = request.json.get('AnalystCapacity', employee['AnalystCapacity'])
    employee['DeveloperSkill'] = request.json.get('DeveloperSkill', employee['DeveloperSkill'])
    employee['DeveloperCapacity'] = request.json.get('DeveloperCapacity', employee['DeveloperCapacity'])
    employee['TesterSkill'] = request.json.get('TesterSkill', employee['TesterSkill'])
    employee['TesterCapacity'] = request.json.get('TesterCapacity', employee['TesterCapacity'])
    employee['Salary'] = request.json.get('Salary', employee['Salary'])
    return jsonify({'employee': employee})

@app_employee.route('/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    employees = [employee for employee in employee_set if employee['Id'] == employee_id]
    if len(employees) == 0:
        abort(404)
    employee_set.remove(employees[0])
    return jsonify({'result': True})

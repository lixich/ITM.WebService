from flask import Blueprint, jsonify, abort, request
from db import update_record, create_record

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
    },
    {
        "Id": 2,
        "Name": 'Андрей',
        "AnalystSkill": 0,
        "AnalystCapacity": 0,
        "DeveloperSkill": 0,
        "DeveloperCapacity": 0,
        "TesterSkill": 0,
        "TesterCapacity": 0,
        "Salary": 0
    },
    {
        "Id": 3,
        "Name": 'Александр',
        "AnalystSkill": 0,
        "AnalystCapacity": 0,
        "DeveloperSkill": 0,
        "DeveloperCapacity": 0,
        "TesterSkill": 0,
        "TesterCapacity": 0,
        "Salary": 0
    },
]
employee_class = {
    "Id": int,
    "Name": str,
    "AnalystSkill": int,
    "AnalystCapacity": int,
    "DeveloperSkill": int,
    "DeveloperCapacity": int,
    "TesterSkill": int,
    "TesterCapacity": int,
    "Salary": int
}

@app_employee.route('/', methods=['GET'])
def get_employee_set():
    return jsonify({'Employee': employee_set})

@app_employee.route('/', methods=['POST'])
def create_employee():
    if not request.json:
        abort(400)
    employee = { 'Id': employee_set[-1]['Id'] + 1 if len(employee_set) else 1 }
    create_record(employee_class, request, employee)
    employee_set.append(employee)
    return jsonify({'Employee': employee}), 201

@app_employee.route('/<int:employee_id>', methods = ['GET'])
def get_employee(employee_id):
    employees = list(filter(lambda t: t['Id'] == employee_id, employee_set))
    if len(employees) == 0:
        abort(404)
    return jsonify({'Employee': employees[0]})

@app_employee.route('/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    employees = [employee for employee in employee_set if employee['Id'] == employee_id]
    if len(employees) == 0 or not request.json:
        abort(404)
    employee = employees[0]
    update_record(employee_class, request, employee)
    return jsonify({'Employee': employee})

@app_employee.route('/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    employees = [employee for employee in employee_set if employee['Id'] == employee_id]
    if len(employees) == 0:
        abort(404)
    employee_set.remove(employees[0])
    return jsonify({'Result': True})

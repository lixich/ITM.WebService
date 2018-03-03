from flask import Blueprint, jsonify, abort, request
from db import update_record, create_record

app_requirement = Blueprint('requirement', __name__)
requirement_set = [
    {
        "Id": 1,
        "Name": 'Сумма А и В',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "IsImportant": True,
        "IsFound": True,
        "ContentId": 1,
        "StakeholderId": 1,
        "MainRequirementId": None
    },
    {
        "Id": 2,
        "Name": 'Ввод a, b',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "IsImportant": True,
        "IsFound": False,
        "ContentId": 1,
        "StakeholderId": 1,
        "MainRequirementId": 1
    },
    {
        "Id": 3,
        "Name": 'Ввод целых числе a, b',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 2,
        "IsImportant": True,
        "IsFound": False,
        "ContentId": 1,
        "StakeholderId": 1,
        "MainRequirementId": 2
    },
    {
        "Id": 4,
        "Name": 'Ввод вещественных чисел a, b',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 3,
        "IsImportant": True,
        "IsFound": False,
        "ContentId": 1,
        "StakeholderId": 1,
        "MainRequirementId": 2
    }
]
requirement_class = {
    "Id": int,
    "Name": str,
    "MinimumSkill": int,
    "DetectionIterationNumber": int,
    "IsImportant": bool,
    "IsFound": bool,
    "ContentId": int,
    "StakeholderId": int,
    "MainRequirementId": int
}

@app_requirement.route('/', methods=['GET'])
def get_requirement_set():
    return jsonify({'Requirement': requirement_set})

@app_requirement.route('/', methods=['POST'])
def create_requirement():
    if not request.json:
        abort(400)
    requirement = { 'Id': requirement_set[-1]['Id'] + 1 if len(requirement_set) else 1 }
    create_record(requirement_class, request, requirement)
    requirement_set.append(requirement)
    return jsonify({'Requirement': requirement}), 201

@app_requirement.route('/<int:requirement_id>', methods = ['GET'])
def get_requirement(requirement_id):
    requirements = list(filter(lambda t: t['Id'] == requirement_id, requirement_set))
    if len(requirements) == 0:
        abort(404)
    return jsonify({'Requirement': requirements[0]})

@app_requirement.route('/<int:requirement_id>', methods=['PUT'])
def update_requirement(requirement_id):
    requirements = [requirement for requirement in requirement_set if requirement['Id'] == requirement_id]
    if len(requirements) == 0 or not request.json:
        abort(404)
    requirement = requirements[0]
    update_record(requirement_class, request, requirement)
    return jsonify({'Requirement': requirement})

@app_requirement.route('/<int:requirement_id>', methods=['DELETE'])
def delete_requirement(requirement_id):
    requirements = [requirement for requirement in requirement_set if requirement['Id'] == requirement_id]
    if len(requirements) == 0:
        abort(404)
    requirement_set.remove(requirements[0])
    return jsonify({'Result': True})

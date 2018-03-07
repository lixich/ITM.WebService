from flask import Blueprint, jsonify, abort, request
from db import update_record, create_record

app_requirement = Blueprint('requirement', __name__)
requirement_set = [
    {
        "Id": 1,
        "Name": 'Сумма А и В',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 8,
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
        "ImportantIndex": 7,
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
        "ImportantIndex": 8,
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
        "ImportantIndex": 6,
        "IsFound": False,
        "ContentId": 1,
        "StakeholderId": 1,
        "MainRequirementId": 2
    },
    {
        "Id": 5,
        "Name": 'Вычисление квадратного уравнения',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": True,
        "ContentId": 2,
        "StakeholderId": 2,
        "MainRequirementId": None
    },
    {
        "Id": 6,
        "Name": 'Ввод a, b, c',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 8,
        "IsFound": True,
        "ContentId": 2,
        "StakeholderId": 2,
        "MainRequirementId": 5
    },
    {
        "Id": 7,
        "Name": 'Ввод целых чисел a, b, c',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 7,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 3,
        "MainRequirementId": 6
    },
    {
        "Id": 8,
        "Name": 'Ввод вещественных чисел a, b, c',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 3,
        "ImportantIndex": 5,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 3,
        "MainRequirementId": 7
    },
    {
        "Id": 9,
        "Name": 'Решение квадратного уравнения',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 2,
        "MainRequirementId": 5
    },
    {
        "Id": 10,
        "Name": 'Решение квадратного неравенства',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 4,
        "ImportantIndex": 4,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 2,
        "MainRequirementId": 5
    },
    {
        "Id": 11,
        "Name": 'Проверка решения пользователя',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 9,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 2,
        "MainRequirementId": None
    },
    {
        "Id": 12,
        "Name": 'Таймер (время на решение)',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 2,
        "MainRequirementId": 11
    },
    {
        "Id": 13,
        "Name": '10 мин',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 3,
        "MainRequirementId": 12
    },
    {
        "Id": 14,
        "Name": '20 мин',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 3,
        "MainRequirementId": 12
    },
    {
        "Id": 15,
        "Name": 'Отключение таймера',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 0,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 3,
        "MainRequirementId": 12
    },
    {
        "Id": 16,
        "Name": 'Отображение ответа',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 9,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 2,
        "MainRequirementId": 11
    },
    {
        "Id": 17,
        "Name": 'С помощью графика',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 3,
        "ImportantIndex": 5,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 3,
        "MainRequirementId": 16
    },
    {
        "Id": 18,
        "Name": 'С помощью формулы',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 3,
        "ImportantIndex": 5,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 3,
        "MainRequirementId": 16
    },
    {
        "Id": 19,
        "Name": 'Голосовое сообщение',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 3,
        "ImportantIndex": 0,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 3,
        "MainRequirementId": 16
    },
    {
        "Id": 20,
        "Name": 'Отображение решения',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 2,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 2,
        "MainRequirementId": 11
    },
    {
        "Id": 21,
        "Name": 'Статистика пользователей',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 5,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 2,
        "MainRequirementId": None
    },
    {
        "Id": 22,
        "Name": 'Среднее время решения',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 0,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 3,
        "MainRequirementId": 21
    },
    {
        "Id": 23,
        "Name": 'Кол-во решенных примеров',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 0,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 2,
        "MainRequirementId": 21
    },
    {
        "Id": 24,
        "Name": 'Процент решенных примеров',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 4,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 3,
        "MainRequirementId": 21
    }
]
requirement_class = {
    "Id": int,
    "Name": str,
    "MinimumSkill": int,
    "DetectionIterationNumber": int,
    "ImportantIndex": int,
    "IsFound": bool,
    "ContentId": int,
    "StakeholderId": int,
    "MainRequirementId": int
}

@app_requirement.route('/', methods=['GET'])
def get_requirement_set():
    return jsonify(requirement_set)

@app_requirement.route('/', methods=['POST'])
def create_requirement():
    if not request.json:
        abort(400)
    requirement = { 'Id': requirement_set[-1]['Id'] + 1 if len(requirement_set) else 1 }
    create_record(requirement_class, request, requirement)
    requirement_set.append(requirement)
    return jsonify(requirement), 201

@app_requirement.route('/<int:requirement_id>', methods = ['GET'])
def get_requirement(requirement_id):
    requirements = list(filter(lambda t: t['Id'] == requirement_id, requirement_set))
    if len(requirements) == 0:
        abort(404)
    return jsonify(requirements[0])

@app_requirement.route('/<int:requirement_id>', methods=['PUT'])
def update_requirement(requirement_id):
    requirements = [requirement for requirement in requirement_set if requirement['Id'] == requirement_id]
    if len(requirements) == 0 or not request.json:
        abort(404)
    requirement = requirements[0]
    update_record(requirement_class, request, requirement)
    return jsonify( requirement)

@app_requirement.route('/<int:requirement_id>', methods=['DELETE'])
def delete_requirement(requirement_id):
    requirements = [requirement for requirement in requirement_set if requirement['Id'] == requirement_id]
    if len(requirements) == 0:
        abort(404)
    requirement_set.remove(requirements[0])
    return jsonify({'Result': True})

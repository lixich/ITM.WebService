from flask import Blueprint, jsonify, abort, request
from db import update_record, create_record
from requirement import requirement_set
from stakeholder import stakeholder_set
from module import module_set

app_content = Blueprint('content', __name__)
content_set = [
    {
        "Id": 1,
        "Budget": 7000,
        "Time": 8,
        "IterationTime": 4,
        "ProjectTitle": "Сумма А и В",
        "ProjectDescription": "Реализовать калькулятор для сложения А и В.",
        "ProjectTask": "Необходимо создать программу-кальулятор."
    },
    {
        "Id": 2,
        "Budget": 40000,
        "Time": 55,
        "IterationTime": 11,
        "ProjectTitle": "Квадратное уравнение",
        "ProjectDescription": "Директор школы хочет повысить успеваемость школьников по математике. По словам учителя математики, основная проблема – это объем примеров, которые решают школьники. Задачники предлагают малое количество примеров по решению квадратного уравнения. Составлять вручную примеры слишком трудозатратное занятие.",
        "ProjectTask": "Необходимо создать программу, генерирующую примеры для решения квадратного уравнения."
    },
    {
        "Id": 3,
        "Budget": 1,
        "Time": 1,
        "IterationTime": 1,
        "ProjectTitle": "Тест",
        "ProjectDescription": " Тест",
        "ProjectTask": "Тест"
    }
]
content_class = {
    "Id": int,
    "Budget": int,
    "Time": int,
    "IterationTime": int,
    "ProjectTitle": str,
    "ProjectDescription": str,
    "ProjectTask": str
}

@app_content.route('/', methods=['GET'])
def get_content_set():
    return jsonify(content_set)

@app_content.route('/', methods=['POST'])
def create_content():
    if not request.json:
        abort(400)
    content = { 'Id': content_set[-1]['Id'] + 1 if len(content_set) else 1 }
    create_record(content_class, request, content)
    content_set.append(content)
    return jsonify(content), 201

@app_content.route('/<int:content_id>', methods = ['GET'])
def get_full_content(content_id):
    contents = list(filter(lambda t: t['Id'] == content_id, content_set))
    if len(contents) == 0:
        abort(404)
    return jsonify( contents[0])

@app_content.route('_full/<int:content_id>', methods = ['GET'])
def get_content(content_id):
    contents = list(filter(lambda t: t['Id'] == content_id, content_set))
    if len(contents) == 0:
        abort(404)
    content = contents[0].copy()

    requirements = list(filter(lambda t: t['ContentId'] == content_id, requirement_set))

    stakeholders_id = set(req['StakeholderId'] for req in requirements)
    stakeholders = list(filter(lambda s: s['Id'] in stakeholders_id , stakeholder_set))

    requirements_id = set(req['Id'] for req in requirements)
    modules = list(filter(lambda mod: mod['RequirementId'] in requirements_id , module_set))

    return jsonify({'Content': content,
                    'Requirements':requirements,
                    'Stakeholders':stakeholders,
                    'Modules':modules})

@app_content.route('/<int:content_id>', methods=['PUT'])
def update_content(content_id):
    contents = [content for content in content_set if content['Id'] == content_id]
    if len(contents) == 0 or not request.json:
        abort(404)
    content = contents[0]
    update_record(content_class, request, content)
    return jsonify(content)

@app_content.route('/<int:content_id>', methods=['DELETE'])
def delete_content(content_id):
    contents = [content for content in content_set if content['Id'] == content_id]
    if len(contents) == 0:
        abort(404)
    content_set.remove(contents[0])
    return jsonify({'Result': True})

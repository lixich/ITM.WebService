from flask import Blueprint, jsonify, abort, request
from db import update_record, create_record

app_content = Blueprint('content', __name__)
content_set = [
    {
        "Id": 1,
        "Budget": 10000,
        "Time": 14,
        "IterationTime": 7,
        "ProjectTitle": "Сумма А и В",
        "ProjectDescription": "Реализовать калькулятор для сложения А и В.",
        "Projectcontent": "Необходимо создать программу-кальулятор."
    },
    {
        "Id": 2,
        "Budget": 100000,
        "Time": 60,
        "IterationTime": 14,
        "ProjectTitle": "Квадратное уравнение",
        "ProjectDescription": "Директор школы хочет повысить успеваемость школьников по математике. По словам учителя математики, основная проблема – это объем примеров, которые решают школьники. Задачники предлагают малое количество примеров по решению квадратного уравнения. Составлять вручную примеры слишком трудозатратное занятие.",
        "Projectcontent": "Необходимо создать программу, генерирующую примеры для решения квадратного уравнения."
    }
]
content_class = {
    "Id": int,
    "Budget": int,
    "Time": int,
    "IterationTime": int,
    "ProjectTitle": str,
    "ProjectDescription": str,
    "Projectcontent": str
}

@app_content.route('/', methods=['GET'])
def get_content_set():
    return jsonify({'content': content_set})

@app_content.route('/', methods=['POST'])
def create_content():
    if not request.json:
        abort(400)
    content = { 'Id': content_set[-1]['Id'] + 1 if len(content_set) else 1 }
    create_record(content_class, request, content)
    content_set.append(content)
    return jsonify({'content': content}), 201

@app_content.route('/<int:content_id>', methods = ['GET'])
def get_content(content_id):
    contents = list(filter(lambda t: t['Id'] == content_id, content_set))
    if len(contents) == 0:
        abort(404)
    return jsonify({'content': contents[0]})

@app_content.route('/<int:content_id>', methods=['PUT'])
def update_content(content_id):
    contents = [content for content in content_set if content['Id'] == content_id]
    if len(contents) == 0 or not request.json:
        abort(404)
    content = contents[0]
    update_record(content_class, request, content)
    return jsonify({'content': content})

@app_content.route('/<int:content_id>', methods=['DELETE'])
def delete_content(content_id):
    contents = [content for content in content_set if content['Id'] == content_id]
    if len(contents) == 0:
        abort(404)
    content_set.remove(contents[0])
    return jsonify({'result': True})

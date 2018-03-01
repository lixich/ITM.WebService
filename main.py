# -*- coding: utf-8 -*-
#!flask/bin/python
from flask import Flask, jsonify, make_response, request, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

contents = [
    {
        "Id": 1,
        "Budget": 10000,
        "Time": 14,
        "IterationTime": 7,
        "ProjectTitle": "Сумма А и В",
        "ProjectDescription": "Реализовать калькулятор для сложения А и В.",
        "ProjectTask": "Необходимо создать программу-кальулятор."
    },
    {
        "Id": 2,
        "Budget": 100000,
        "Time": 60,
        "IterationTime": 14,
        "ProjectTitle": "Квадратное уравнение",
        "ProjectDescription": "Директор школы хочет повысить успеваемость школьников по математике. По словам учителя математики, основная проблема – это объем примеров, которые решают школьники. Задачники предлагают малое количество примеров по решению квадратного уравнения. Составлять вручную примеры слишком трудозатратное занятие.",
        "ProjectTask": "Необходимо создать программу, генерирующую примеры для решения квадратного уравнения."
    }
]

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/content', methods=['GET'])
def get_contentset():
    return jsonify({'content': contents})


if __name__ == '__main__':
    app.run(debug=True)

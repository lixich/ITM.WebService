from flask import Blueprint, jsonify, abort, request
from db import update_record, create_record

app_module = Blueprint('module', __name__)
module_set = [
    {
        "Id": 1,
        "Name": 'Sum(a, b)',
        "CodeLinesNumber": 50,
        "ImportantIndex": 10,
        "RequirementId": 1,
        "MainModuleId": None
    },
    {
        "Id": 2,
        "Name": 'Input(a,b)',
        "CodeLinesNumber": 97,
        "ImportantIndex": 10,
        "RequirementId": 2,
        "MainModuleId": None
    },
    {
        "Id": 3,
        "Name": 'Input(int a, int b)',
        "CodeLinesNumber": 88,
        "ImportantIndex": 10,
        "RequirementId": 3,
        "MainModuleId": None
    },
    {
        "Id": 4,
        "Name": 'Input(real a, real b)',
        "CodeLinesNumber": 150,
        "ImportantIndex": 10,
        "RequirementId": 4,
        "MainModuleId": None
    },
    {
        "Id": 5,
        "Name": 'Input(a,b,c)',
        "CodeLinesNumber": 97,
        "ImportantIndex": 10,
        "RequirementId": 6,
        "MainModuleId": None
    },
    {
        "Id": 6,
        "Name": 'Input(int a, int b, int c)',
        "CodeLinesNumber": 98,
        "ImportantIndex": 10,
        "RequirementId": 7,
        "MainModuleId": None
    },
    {
        "Id": 7,
        "Name": 'Input(double a, double b, double c)',
        "CodeLinesNumber": 150,
        "ImportantIndex": 10,
        "RequirementId": 8,
        "MainModuleId": None
    },
    {
        "Id": 8,
        "Name": 'SolveEquation()',
        "CodeLinesNumber": 250,
        "ImportantIndex": 10,
        "RequirementId": 9,
        "MainModuleId": None
    },
    {
        "Id": 9,
        "Name": 'Sum()',
        "CodeLinesNumber": 50,
        "ImportantIndex": 10,
        "RequirementId": 9,
        "MainModuleId": None
    },
    {
        "Id": 10,
        "Name": 'Deduct()',
        "CodeLinesNumber": 75,
        "ImportantIndex": 10,
        "RequirementId": 9,
        "MainModuleId": None
    },
    {
        "Id": 11,
        "Name": 'Mod()',
        "CodeLinesNumber": 80,
        "ImportantIndex": 10,
        "RequirementId": 9,
        "MainModuleId": None
    },
    {
        "Id": 12,
        "Name": 'Div()',
        "CodeLinesNumber": 80,
        "ImportantIndex": 10,
        "RequirementId": 9,
        "MainModuleId": None
    },
    {
        "Id": 13,
        "Name": 'Multiply()',
        "CodeLinesNumber": 230,
        "ImportantIndex": 10,
        "RequirementId": 9,
        "MainModuleId": None
    },
    {
        "Id": 14,
        "Name": 'Sqrt()',
        "CodeLinesNumber": 200,
        "ImportantIndex": 10,
        "RequirementId": 9,
        "MainModuleId": None
    },
    {
        "Id": 15,
        "Name": 'Pow()',
        "CodeLinesNumber": 150,
        "ImportantIndex": 10,
        "RequirementId": 9,
        "MainModuleId": None
    },
    {
        "Id": 16,
        "Name": 'SolveInequality()',
        "CodeLinesNumber": 93,
        "ImportantIndex": 10,
        "RequirementId": 9,
        "MainModuleId": None
    },
    {
        "Id": 17,
        "Name": 'Sum()',
        "CodeLinesNumber": 60,
        "ImportantIndex": 10,
        "RequirementId": 10,
        "MainModuleId": None
    },
    {
        "Id": 18,
        "Name": 'Deduct()',
        "CodeLinesNumber": 80,
        "ImportantIndex": 10,
        "RequirementId": 10,
        "MainModuleId": None
    },
    {
        "Name": 'Mod()',
        "CodeLinesNumber": 90,
        "ImportantIndex": 10,
        "RequirementId": 10,
        "MainModuleId": None
    },
    {
        "Id": 20,
        "Name": 'Div()',
        "CodeLinesNumber": 95,
        "ImportantIndex": 10,
        "RequirementId": 10,
        "MainModuleId": None
    },
    {
        "Id": 21,
        "Name": 'Multiply()',
        "CodeLinesNumber": 250,
        "ImportantIndex": 10,
        "RequirementId": 10,
        "MainModuleId": None
    },
    {
        "Id": 22,
        "Name": 'Sqrt()',
        "CodeLinesNumber": 150,
        "ImportantIndex": 10,
        "RequirementId": 10,
        "MainModuleId": None
    },
    {
        "Id": 23,
        "Name": 'Pow()',
        "CodeLinesNumber": 160,
        "ImportantIndex": 10,
        "RequirementId": 10,
        "MainModuleId": None
    },
    {
        "Id": 24,
        "Name": 'Decision()',
        "CodeLinesNumber": 100,
        "ImportantIndex": 10,
        "RequirementId": 20,
        "MainModuleId": None
    },
    {
        "Id": 25,
        "Name": 'Timer()',
        "CodeLinesNumber": 120,
        "ImportantIndex": 10,
        "RequirementId": 12,
        "MainModuleId": None
    },
    {
        "Id": 26,
        "Name": 'TimerRun(int 10)',
        "CodeLinesNumber": 80,
        "ImportantIndex": 0,
        "RequirementId": 13,
        "MainModuleId": None
    },
    {
        "Id": 27,
        "Name": 'TimerRun(int 20)',
        "CodeLinesNumber": 130,
        "ImportantIndex": 0,
        "RequirementId": 14,
        "MainModuleId": None
    },
    {
        "Id": 28,
        "Name": 'TimerOff()',
        "CodeLinesNumber": 250,
        "ImportantIndex": 0,
        "RequirementId": 15,
        "MainModuleId": None
    },
    {
        "Id": 29,
        "Name": 'Answer()',
        "CodeLinesNumber": 150,
        "ImportantIndex": 10,
        "RequirementId": 16,
        "MainModuleId": None
    },
    {
        "Id": 26,
        "Name": 'ShowChart()',
        "CodeLinesNumber": 110,
        "ImportantIndex": 10,
        "RequirementId": 17,
        "MainModuleId": None
    },
    {
        "Id": 27,
        "Name": 'ShowFormula()',
        "CodeLinesNumber": 130,
        "ImportantIndex": 10,
        "RequirementId": 18,
        "MainModuleId": None
    },
    {
        "Id": 28,
        "Name": 'VoiceAnswer()',
        "CodeLinesNumber": 115,
        "ImportantIndex": 10,
        "RequirementId": 19,
        "MainModuleId": None
    },
    {
        "Id": 29,
        "Name": 'AverageSolving()',
        "CodeLinesNumber": 70,
        "ImportantIndex": 10,
        "RequirementId": 22,
        "MainModuleId": None
    },
    {
        "Id": 30,
        "Name": 'SuccessResult()',
        "CodeLinesNumber": 50,
        "ImportantIndex": 10,
        "RequirementId": 23,
        "MainModuleId": None
    },
    {
        "Id": 31,
        "Name": 'ProcentSuccessResult()',
        "CodeLinesNumber": 60,
        "ImportantIndex": 10,
        "RequirementId": 24,
        "MainModuleId": None
    }
]
module_class = {
    "Id": int,
    "Name": str,
    "CodeLinesNumber": int,
    "ImportantIndex": int,
    "RequirementId": int,
    "MainModuleId": int
}

@app_module.route('/', methods=['GET'])
def get_module_set():
    return jsonify(module_set)

@app_module.route('/', methods=['POST'])
def create_module():
    if not request.json:
        abort(400)
    module = { 'Id': module_set[-1]['Id'] + 1 if len(module_set) else 1 }
    create_record(module_class, request, module)
    module_set.append(module)
    return jsonify(module), 201

@app_module.route('/<int:module_id>', methods = ['GET'])
def get_module(module_id):
    modules = list(filter(lambda t: t['Id'] == module_id, module_set))
    if len(modules) == 0:
        abort(404)
    return jsonify(modules[0])

@app_module.route('/<int:module_id>', methods=['PUT'])
def update_module(module_id):
    modules = [module for module in module_set if module['Id'] == module_id]
    if len(modules) == 0 or not request.json:
        abort(404)
    module = modules[0]
    update_record(module_class, request, module)
    return jsonify(module)

@app_module.route('/<int:module_id>', methods=['DELETE'])
def delete_module(module_id):
    modules = [module for module in module_set if module['Id'] == module_id]
    if len(modules) == 0:
        abort(404)
    module_set.remove(modules[0])
    return jsonify({'Result': True})

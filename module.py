from flask import Blueprint, jsonify, abort, request
from db import update_record, create_record

app_module = Blueprint('module', __name__)
module_set = [
    {
        "Id": 1,
        "Name": 'Sum(a, b)',
        "CodeLinesNumber": 50,
        "IsImportant": True,
        "RequirementId": 1,
        "MainModuleId": None
    },
    {
        "Id": 2,
        "Name": 'Input(a,b)',
        "CodeLinesNumber": 97,
        "IsImportant": True,
        "RequirementId": 2,
        "MainModuleId": None
    },
    {
        "Id": 3,
        "Name": 'Input(int a, int b)',
        "CodeLinesNumber": 88,
        "IsImportant": True,
        "RequirementId": 3,
        "MainModuleId": None
    },
    {
        "Id": 4,
        "Name": 'Input(real a, real b)',
        "CodeLinesNumber": 150,
        "IsImportant": True,
        "RequirementId": 4,
        "MainModuleId": None
    }
]
module_class = {
    "Id": int,
    "Name": str,
    "CodeLinesNumber": int,
    "IsImportant": bool,
    "RequirementId": int,
    "MainModuleId": int
}

@app_module.route('/', methods=['GET'])
def get_module_set():
    return jsonify({'Module': module_set})

@app_module.route('/', methods=['POST'])
def create_module():
    if not request.json:
        abort(400)
    module = { 'Id': module_set[-1]['Id'] + 1 if len(module_set) else 1 }
    create_record(module_class, request, module)
    module_set.append(module)
    return jsonify({'Module': module}), 201

@app_module.route('/<int:module_id>', methods = ['GET'])
def get_module(module_id):
    modules = list(filter(lambda t: t['Id'] == module_id, module_set))
    if len(modules) == 0:
        abort(404)
    return jsonify({'Module': modules[0]})

@app_module.route('/<int:module_id>', methods=['PUT'])
def update_module(module_id):
    modules = [module for module in module_set if module['Id'] == module_id]
    if len(modules) == 0 or not request.json:
        abort(404)
    module = modules[0]
    update_record(module_class, request, module)
    return jsonify({'Module': module})

@app_module.route('/<int:module_id>', methods=['DELETE'])
def delete_module(module_id):
    modules = [module for module in module_set if module['Id'] == module_id]
    if len(modules) == 0:
        abort(404)
    module_set.remove(modules[0])
    return jsonify({'Result': True})

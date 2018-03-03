from flask import request

def create_record(_class, _request, _record):
    for _field in _class.keys():
        if _field not in _record.keys():
            _record[_field] = request.json.get(_field, '')

def update_record(_class, _request, _record):
    for _field in _class.keys():
        if _field in request.json:
            _record[_field] = request.json[_field]

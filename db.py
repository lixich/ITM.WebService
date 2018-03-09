from flask import request

def create_record(_class, _request, _record):
    for _field in _class.keys():
        # _record is empty, only Ids
        if _field not in _record.keys():
            if _field in request.json and str(request.json[_field]) == 'null':
                _record[_field] = None
            else:
                _record[_field] = _class[_field](request.json.get(_field, _class[_field]()))

def update_record(_class, _request, _record):
    for _field in _class.keys():
        if _field in request.json:
            if str(request.json[_field]) == 'null':
                _record[_field] = None
            else:
                _record[_field] = _class[_field](request.json[_field])

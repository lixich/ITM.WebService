def create_record(_class, _request, _record):
    for _field in _class.keys():
        # _record is empty, only Ids
        if _field not in _record.keys():
            _record[_field] = _request.json.get(_field, _class[_field]())

def update_record(_class, _request, _record):
    for _field in _class.keys():
        if _field in _request.json:
            _record[_field] = _request.json[_field]

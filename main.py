# -*- coding: utf-8 -*-
#!flask/bin/python
from flask import Flask, Blueprint, jsonify, make_response, request, abort
from flask_cors import CORS
from content import app_content
from stakeholder import app_stakeholder
from user import app_user
from test import app_test
from employee import app_employee

app = Flask(__name__)
app.register_blueprint(app_content, url_prefix='/content')
app.register_blueprint(app_stakeholder, url_prefix='/stakeholder')
app.register_blueprint(app_user, url_prefix='/user')
app.register_blueprint(app_test, url_prefix='/test')
app.register_blueprint(app_employee, url_prefix='/employee')
CORS(app, supports_credentials=True)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)

# -*- coding: utf-8 -*-
#!flask/bin/python
from flask import Flask, Blueprint, jsonify, make_response, request, abort, Response
from flask_cors import CORS
from time import sleep
from middleware import setup_metrics
from content import app_content
from employee import app_employee
from stakeholder import app_stakeholder
from requirement import app_requirement
from module import app_module
from test import app_test
from manager import app_manager
from metrics import app_metrics

app = Flask(__name__)
setup_metrics(app)
app.register_blueprint(app_content, url_prefix='/content')
app.register_blueprint(app_employee, url_prefix='/employee')
app.register_blueprint(app_stakeholder, url_prefix='/stakeholder')
app.register_blueprint(app_requirement, url_prefix='/requirement')
app.register_blueprint(app_module, url_prefix='/module')
app.register_blueprint(app_test, url_prefix='/test')
app.register_blueprint(app_manager, url_prefix='/manager')
app.register_blueprint(app_metrics, url_prefix='/metrics')
CORS(app, supports_credentials=True)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Error': 'Not found'}), 404)

@app.route('/')
def home():
    sleep(10)
    return jsonify({'Hello': 'My friend'})

if __name__ == '__main__':
    app.run(debug=True)

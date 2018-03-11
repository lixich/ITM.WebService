from flask import Blueprint, jsonify, abort, request
import time
from middleware import log_set, active_requests

app_metrics = Blueprint('metrics', __name__)

@app_metrics.route('/')
def metrics():
    return jsonify(log_set)

@app_metrics.route('/<float:seconds>', methods = ['GET'])
def metrics_seconds(seconds):
    now_time = time.time()
    logs = list(filter(lambda log: log['StartTime'] >= now_time - seconds, log_set))
    average_response_time = 0.0
    if len(logs) != 0:
        average_response_time = round(sum([log['ResponseTime'] for log in logs]) / len(logs), 5)
    return jsonify({
        'Count' : len(logs),
        'AverageResponseTime': average_response_time,
        'ActiveRequests' : active_requests
    })

@app_metrics.route('/', methods = ['DELETE'])
def delete_metrics():
    log_set.clear()
    return jsonify({'Result': True})

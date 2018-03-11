from flask import request
import time
import sys

log_set = [
    {
        "Method": "GET",
        "Path": "/metrics/",
        "ResponseTime": 0.0,
        "StartCtime": "Sun Mar 11 13:00:18 2018",
        "StartTime": 1520755218.7541325,
        "StatusCode": 200
    }
]

active_requests = 0

def start_timer():
    global active_requests
    active_requests += 1
    request.start_time = time.time()

def stop_timer(response):
    global active_requests
    active_requests -= 1
    resp_time = time.time() - request.start_time
    #sys.stderr.write("Response time: %ss\n" % resp_time)
    #sys.stderr.write("Request path: %s Request method: %s Response status: %s\n" % (request.path, request.method, response.status_code))
    log_set.append({
        'Method': request.method,
        'Path' : request.path,
        'ResponseTime' : resp_time,
        'StartCtime' : time.ctime(request.start_time),
        'StartTime' : request.start_time,
        'StatusCode': response.status_code
    })
    return response

def setup_metrics(app):
    app.before_request(start_timer)
    app.after_request(stop_timer)

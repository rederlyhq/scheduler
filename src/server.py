#!/usr/bin/python3
from flask import Flask, request
from waitress import serve
import worker
import json
import os

server_port = os.environ.get('SERVER_PORT') or 3003

app = Flask(__name__)

@app.route('/set_job/', methods=['POST'])
def set_job():
    worker.set_job(request.json)
    return 'created'

@app.route('/delete_job/', methods=['POST'])
def delete_job():
    worker.delete_job(request.json["id"])
    return 'deleted'

@app.route('/list_scheduled_jobs/', methods=['GET'])
def get_event_list():
    result = str(worker.list_scheduled_jobs())
    # print(result)
    return result

@app.route('/list_failed_jobs/', methods=['GET'])
def get_failed_jobs():
    result = str(worker.list_failed_jobs())
    # print(result)
    return result

@app.route('/get_job/', methods=['GET'])
def get_job():
    # result = json.dumps(worker.get_job(request.args.get('id')))
    result = str(worker.get_job(request.args.get('id')))
    # print(result)
    return result

def start_server():
    serve(app, port = server_port)
    # app.run(host='::', port=3000)
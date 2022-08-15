
from flask import Flask
from flask import request
from flask import jsonify
import json
import logging

from dool import app,now

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/echoJSON', methods=['POST','GET'])
def echoJSON():
    if request.method=='POST':
        data = request.json
        logging.info(f"{now()}:{data}")
        return jsonify(data)
    else:
        return jsonify(json.loads('{"dool": "dool"}'))
        logging.info("Kos sher zadan")


@app.route('/whatsMyIP', methods=['GET', 'POST'])
def index():
    ip = 'Unknown Visitor'
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy
    stmt=f'<html><body><h1>Hello</h1></body></html> {ip}'
    return stmt


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

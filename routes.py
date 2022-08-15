
from flask import Flask
from flask import request
from flask import jsonify
import json

from dool import app

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/echoJSON', methods=['POST','GET'])
def echoJSON():
    if request.method=='POST':
        data = request.json
        data['Quantity']=data['Quantity']+66
        return jsonify(data)
    else:
        return jsonify(json.loads('{"dool": "dool"}'))

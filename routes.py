
#sysport
from flask import Flask
from flask import request
from flask import jsonify
import json
import logging
from flask import send_file

#userport
from dool import app,now
from qr_cls import dool_qr

# from koon import serve_pil_image

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

@app.route('/qrIP', methods=['GET','POST'])
def qrIP():
    ip = 'Unknown Visitor'
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy
    from qr_cls import dool_qr
    file_name=dool_qr(data=ip).qr()
    return f"<html>{file_name}</html>"

@app.route('/qrs',methods=['GET','POST'])
def qr():
    import glob
    qrlist=glob.glob('*.jpg')
    return f"<html>{qrlist}</html>"

# @app.route('/qrSHOW',methods=['GET','POST'])
# def qrSHOW():
#     # from flask import send_file
#     # import pathlib
#     # p=pathlib.Path().resolve()
#     #
#     # qrlist=list(p.glob('*.jpg'))
#     # return send_file(qrlist[0])
#
#
#
#     # if request.args.get('show_qr') == '1':
#     #     ret = dool_qr(data=ip).qr()
#     # else:
#     #     pass
#     # qr_image = dool_qr().qr(data=file_)
#     # return serve_pil_image(dool_qr(data=ip).qr())

#! /home/c/Code/Shell/Conf1/vconf1/bin/python3

#dool.py


from flask import Flask
import logging
app = Flask(__name__)



from routes import *

if __name__=="__main__":
    logging.basicConfig(filename='dool.log', encoding='utf-8', level=logging.DEBUG)
    app.run()

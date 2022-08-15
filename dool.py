#! /home/c/Code/Shell/Conf1/vconf1/bin/python3

#dool.py


from flask import Flask
import logging
from datetime import datetime
app = Flask(__name__)
now=datetime.now



from routes import *

if __name__=="__main__":
    logging.basicConfig(filename='dool.log', level=logging.DEBUG)

    logging.info(f"start: {now()}\n")
    app.run()
    logging.info(f"end:{now()}")

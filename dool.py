#! /home/c/Code/Shell/Conf1/vconf1/bin/python3

#dool.py

from conf import Conf
from flask import Flask
import logging
from datetime import datetime
app = Flask('Zortom')
app.config.from_object(Conf)
now=datetime.now



from routes import *

if __name__=="__main__":
    logging.basicConfig(filename='dool.log', level=logging.DEBUG)

    logging.info(f"start: {now()}\n")
    app.run()
    logging.info(f"end:{now()}")

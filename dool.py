#! /home/c/Code/Shell/Conf1/vconf1/bin/python3

#dool.py

from conf import Conf
from flask import Flask
import logging
from datetime import datetime
now=datetime.now

logging.basicConfig(filename='dool.log', level=logging.DEBUG)


app = Flask('Dool')
app.config.from_object('conf.Conf')
from routes import *

if __name__=="__main__":
    logging.info(f"start: {now()}\n")
    run_time_config=app.config
    logging.info(run_time_config)
    app.run()
    logging.info(f"end:{now()}")

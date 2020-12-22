# Nospace

from flask import Flask,render_template,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc,func,exc

from apscheduler.schedulers.background import BackgroundScheduler
import pandas as pd
import argparse
import multiprocessing


# quello che fa funzionare 
from tqdm import tnrange, tqdm_notebook
from tqdm import tqdm
from time import sleep
import datetime
import math

from datetime import timedelta
import datetime

import hashlib
import os
import random
import pickle
import json
import copy 
import io
import base64
import sys
import inspect
import itertools
import time

# service postgresql@10-main restart

from modules.db import *
from modules.rens import rens

APP_DIR = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__, static_url_path='/static')

re_inst = rens("system")
user_id = 1223124

@app.route('/')
def home():

    return 'Live'

# questa e' la risoluzione 
@app.route('/products', methods=['GET'])
def products():
    global re_inst

    products_list_json = re_inst.products_list()

    return jsonify(products_list_json)

# questa e' la risoluzione 
@app.route('/product/<product_id>/<problem_id>', methods=['GET'])
def product_section(product_id,problem_id):
    global re_inst,user_id

    resolution_id = re_inst.resolution(product_id,user_id,problem_id)

    resolution_json = re_inst.select_resolution(product_id,resolution_id[0])

    return jsonify(resolution_json)



# questa e' la risoluzione 
@app.route('/product/<product_id>/<problem_id>/<response_id>', methods=['GET'])
def feedback_section(product_id,problem_id,response_id):
    global re_inst,user_id

    feedback_status = re_inst.feedback(product_id,user_id,problem_id,response_id)

    return jsonify(feedback_status)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='App')
    parser.add_argument('-e','--env', help='system enviroment', required=False,default='Dev')
    args = vars(parser.parse_args())

    print('############ Check ############')


    print('############ Background processing ############')

    #application_inst.research()

    # scheduler per far partire il processo in background di gioco
    scheduler = BackgroundScheduler()

    scheduler.start()

    if args['env'] != "Prod":
        app.run(port=5000,host="0.0.0.0",debug=True,use_reloader=True)
    else:
        app.run(port=5000,host="0.0.0.0",debug=False,use_reloader=False)

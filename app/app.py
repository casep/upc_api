from flask import Flask
from flask import request
import pandas as pd
import json
from sqlalchemy import create_engine

app = Flask(__name__)

# GET endpoint
@app.route('/', methods=['GET'])
def get_tasks():
    return "App OK"
@app.get('/api/get/<id>')
def get_record(id):
    try:
        disk_engine=create_engine('sqlite:///my_lite_store.db')
        upc_corpus=pd.read_sql_query('SELECT * FROM ean WHERE ean = '+id,disk_engine)
        item = upc_corpus['name'][0] + "\n"
        returnJson = json.dumps(item)
        return returnJson
    except:
        return("Not valid code\n")


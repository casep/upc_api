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
    result = {
    }
    try:
        disk_engine=create_engine('sqlite:///my_lite_store.db')
        upc_corpus=pd.read_sql_query('SELECT * FROM ean WHERE ean = '+id,disk_engine)
        result.update({"Found":True,"Name":upc_corpus['name'][0],"Code":id})
        returnJson = json.dumps(result)
        return returnJson
    except:
        result.update({"Found":False,"Code":id})
        nonValid = json.dumps(result)
        return(nonValid)


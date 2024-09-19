from flask import Flask
from flask import request
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

# GET endpoint
@app.get('/api/get/<id>')
def get_record(id):
    disk_engine=create_engine('sqlite:///my_lite_store.db')
    upc_corpus=pd.read_sql_query('SELECT * FROM ean WHERE ean = '+id,disk_engine)
    return upc_corpus['name'][0]


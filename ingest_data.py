"""Loading old UPC data into a sqllite db"""
import pandas as pd
from sqlalchemy import create_engine

disk_engine=create_engine('sqlite:///data/my_lite_store.db')
upc_corpus=pd.read_csv('data/upc_corpus.csv',dtype={"ean": "string", "name": "string"})
upc_corpus.to_sql('ean', disk_engine, if_exists='replace')


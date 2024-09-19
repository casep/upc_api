"""Loading old UPC data into a sqllite db"""
import pandas as pd
from sqlalchemy import create_engine

disk_engine=create_engine('sqlite:///data/my_lite_store.db')

upc_corpus=pd.read_sql_query('SELECT * FROM ean WHERE ean = 8001630003968',disk_engine)
print(upc_corpus['name'][0])

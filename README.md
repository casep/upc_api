# upc_api
Simple flask server to query UPC data

# build image
```
docker build . -t upc_api
```

# Load data
```
pip3 install --user -r requirements.txt 
rm -rf data/my_lite_store.db
python3 ingest_data.py
```

# run image
```
docker run --rm -p 5000:5000 upc_api
```

# query data
```
curl http://localhost:5000/api/get/8852023003078
```
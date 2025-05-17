from fastapi import FastAPI
from app.ingestion import sending_product_datas

app = FastAPI()


@app.get('/sending-data/dtdd')
def insert_data_dtdd():
    return sending_product_datas()
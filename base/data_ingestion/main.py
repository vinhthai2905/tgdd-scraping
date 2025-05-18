from fastapi import FastAPI
from app.ingestion import sending_phone_datas

app = FastAPI()


@app.get('/sending-data/dtdd')
def insert_data_dtdd():
    return sending_phone_datas()
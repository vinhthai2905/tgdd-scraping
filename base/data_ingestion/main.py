from fastapi import FastAPI
from app.ingestion import sending_phone_datas, sending_laptop_datas

app = FastAPI()


@app.get('/sending-data/phone')
def send_data_phone():
    return sending_phone_datas()

@app.get('/sending-data/laptop')
def send_data_laptop():
    return sending_laptop_datas()
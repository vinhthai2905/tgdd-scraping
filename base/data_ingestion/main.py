from fastapi import FastAPI
from app.ingestion import sending_phone_datas, sending_laptop_datas

app = FastAPI()


@app.get('/sending-data/phone')
async def send_data_phone():
    return await sending_phone_datas()

@app.get('/sending-data/laptop')
async def send_data_laptop():
    return await sending_laptop_datas()
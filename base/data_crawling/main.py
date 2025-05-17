import requests
from fastapi import FastAPI
from threading import Thread
from app.crawler import phone_crawling
from app.scheduler import schedule_phone_crawling

app = FastAPI()


@app.on_event("startup")
def start_scheduler():
    thread = Thread(target=schedule_phone_crawling)
    thread.daemon = True
    thread.start()


@app.get('/crawling/dtdd/')
def datas_crawling():
    message = phone_crawling()
    try:
        respone = requests.get('http://127.0.0.1:8002/sending-data/dtdd')
    except Exception as e:
        print(e)
    return {'Message': message, 
            'Request Insertion': respone.status_code}
import requests
from fastapi import FastAPI
from pprint import pprint
from threading import Thread
from app.crawler import phone_crawling, laptop_crawling
from app.scheduler import schedule_phone_crawling, schedule_laptop_crawling

app = FastAPI()


@app.on_event('startup')
def start_all_schedulers():
    # phone_thread = Thread(target=schedule_phone_crawling, daemon=True)
    laptop_thread = Thread(target=schedule_laptop_crawling, daemon=True)
    # phone_thread.start()
    laptop_thread.start()


@app.get('/crawling/dtdd/')
def dtdd_crawling():
    message = phone_crawling()
    pprint(message)
    return {'Message': message}

@app.get('/crawling/laptop')
def laptops_crawling():
    message = laptop_crawling()
    pprint(message)
    return {'Message': message}
              
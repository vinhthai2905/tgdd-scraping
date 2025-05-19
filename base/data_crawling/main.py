import requests
import asyncio
from fastapi import FastAPI
from pprint import pprint
from threading import Thread
from app.crawler import phone_crawling, laptop_crawling
from app.scheduler import schedule_phone_crawling, schedule_laptop_crawling

app = FastAPI()


@app.on_event('startup')
async def start_all_schedulers():
    # asyncio.create_task(schedule_laptop_crawling())
    asyncio.create_task(schedule_phone_crawling())
    # # phone_thread = Thread(target=schedule_phone_crawling, daemon=True)
    # laptop_thread = Thread(target=schedule_laptop_crawling, daemon=True)
    # # phone_thread.start()
    # laptop_thread.start()


@app.get('/crawling/dtdd/')
async def dtdd_crawling():
    message = await phone_crawling()
    pprint(message)
    return {'Message': message}

@app.get('/crawling/laptop')
async def laptops_crawling():
    message = await laptop_crawling()
    pprint(message)
    return {'Message': message}
              
from pprint import pprint
import requests
# import schedule
import asyncio
import aioschedule as schedule
import logging
from app import crawler
from schedule import every, repeat
from datetime import time, timedelta, datetime


logging.basicConfig(
    filename='./logs/crawler.log',  
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',  #
    datefmt='%Y-%m-%d %H:%M:%S'  
)

async def start_scheduler():
    async def laptop_job():
        print(f'[{datetime.now()}] Running laptop job...', flush=True)
        message = await crawler.laptop_crawling()
        pprint(message)

    async def phone_job():
        print(f'[{datetime.now()}] Running phone job...', flush=True)
        message = await crawler.phone_crawling()
        pprint(message)

    schedule.every(5).seconds.do(lambda: asyncio.create_task(laptop_job()))
    schedule.every(5).seconds.do(lambda: asyncio.create_task(phone_job()))

    while True:
        await schedule.run_pending()
        await asyncio.sleep(1)
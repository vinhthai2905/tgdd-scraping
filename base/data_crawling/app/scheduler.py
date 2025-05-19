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

async def schedule_laptop_crawling():
    async def laptop_job():
        print(f'[{datetime.now()}] Running scheduled laptop job...', flush=True)
        try:
            result = await crawler.laptop_crawling()
        except Exception as e:
            result = e
        pprint(result)
    schedule.every(5).seconds.do(laptop_job)
    while True:
        await schedule.run_pending()
        await asyncio.sleep(1)

async def schedule_phone_crawling():
    async def phone_job():
        print(f'[{datetime.now()}] Running scheduled phone job...', flush=True)
        try:
            result = await crawler.phone_crawling()
        except Exception as e:
            result = e
        pprint(result)
    schedule.every(5).seconds.do(phone_job)
    while True:
        await schedule.run_pending()
        await asyncio.sleep(1)
    
import requests
import asyncio
import aioschedule
import logging
from app import crawler
from pprint import pprint
from datetime import time, timedelta, datetime


logging.basicConfig(
    filename='./logs/crawler.log',  
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',  #
    datefmt='%Y-%m-%d %H:%M:%S'  
)

async def schedule_job(job_fn, interval_seconds: int, label: str):
    while True:
        try:
            print(f'[{datetime.now()}] Running {label} job...', flush=True)
            result = await job_fn()
            pprint(result)            
        except Exception as e:
            logging.error(f"{label} job failed: {e}")
        await asyncio.sleep(interval_seconds)

async def start_aioscheduler():
    await asyncio.gather(
        schedule_job(crawler.phone_crawling, 5, 'Phone'),
        schedule_job(crawler.laptop_crawling, 5, 'Laptop'),
    )
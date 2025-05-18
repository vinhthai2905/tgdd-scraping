from pprint import pprint
import requests
import schedule
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

def schedule_laptop_crawling():
    @repeat(every(5).seconds)
    def laptop_job():
        print(f'[{datetime.now()}] Running scheduled laptop job...', flush=True)
        try:
            crawler.laptop_crawling()
        except Exception as e:
            pprint(crawler.laptop_crawling())
        else:
            pprint(crawler.laptop_crawling())
    while True:
        schedule.run_pending()

def schedule_phone_crawling():
    @repeat(every(5).seconds)
    def phone_job():
        print(f'[{datetime.now()}] Running scheduled phone job...', flush=True)
        try:
            crawler.phone_crawling()
        except Exception as e:
            pprint(crawler.phone_crawling())
        else:
            pprint(crawler.phone_crawling())
    while True:
        schedule.run_pending()
    
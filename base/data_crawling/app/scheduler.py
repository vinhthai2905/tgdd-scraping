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

def schedule_phone_crawling():
    @repeat(every(5).seconds)
    def job():
        print(f'[{datetime.now()}] Running scheduled job...', flush=True)
        try:
            crawler.phone_crawling()
        except Exception as e:
            pprint(crawler.phone_crawling())
        else:
            pprint(crawler.phone_crawling())
    while True:
        schedule.run_pending()
    
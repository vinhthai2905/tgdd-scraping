import requests
import schedule
import time
from app import crawler
from schedule import every, repeat
from datetime import time, timedelta, datetime


def schedule_phone_crawling():
    @repeat(every(5).seconds)
    def job():
        print(f'[{datetime.now()}] Running scheduled job...')
        # try:
        crawler.phone_crawling()
        requests.get('http://127.0.0.1:8002/sending-data/dtdd')
        # except Exception as e:
        #     print(f'An error occured while crawling. Check logs for more details.')
        # else:
        #     print(f'Crawling started. Check logs for more details.')
    while True:
        schedule.run_pending()
    
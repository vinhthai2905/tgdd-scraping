from fastapi import FastAPI
from app.crawler import phone_crawling
app = FastAPI()


@app.get('/dtdd')
def datas_crawling():
    return phone_crawling()

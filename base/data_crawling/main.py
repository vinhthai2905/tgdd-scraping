from fastapi import FastAPI

app = FastAPI()


@app.get('/test')
def datas_crawling():
    return {'Test': 155}
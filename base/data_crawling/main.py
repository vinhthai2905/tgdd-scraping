import requests
import asyncio
from fastapi import FastAPI
from pprint import pprint
from contextlib import asynccontextmanager
from threading import Thread
from app.crawler import phone_crawling, laptop_crawling
from app.scheduler import start_aioscheduler


@asynccontextmanager
async def lifespan(app: FastAPI):
    import asyncio
    await asyncio.sleep(2)

    asyncio.create_task(start_aioscheduler())
    yield
    
app = FastAPI(lifespan=lifespan)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(start_aioscheduler())
#     # # phone_thread = Thread(target=schedule_phone_crawling, daemon=True)
#     # laptop_thread = Thread(target=schedule_laptop_crawling, daemon=True)
#     # # phone_thread.start()
#     # laptop_thread.start()


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
              
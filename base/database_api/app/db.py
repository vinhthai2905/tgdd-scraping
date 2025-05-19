from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL
from sqlalchemy import text
from dotenv import load_dotenv, find_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
import os
import logging

# load_dotenv(dotenv_path='D:\Projects\Python\224-CDCSDL-FinalProject\.env', override=True)

URL_OBJECT = URL.create(
    'postgresql+asyncpg',
    # username=os.getenv('USER'),
    # password=os.getenv('USER_PASSWORD'),
    # host=os.getenv('HOST'),
    # database=os.getenv('DB'),
    # port=int(os.getenv('PORT'))
    username='postgres',
    password='root',
    host='postgres_DB',
    database='tgdd_db',
    port=5432
)

# print(os.getenv('USER_PASSWORD'))

engine = create_engine(URL_OBJECT, logging_name='myengine')
async_engine = create_async_engine(URL_OBJECT, logging_name='myengine')

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
async_session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)

# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

def db_connection():
    dbCon = sessionLocal()
    try:
        yield dbCon
    finally:
        dbCon.close()

async def get_async_session():
    async with async_session() as session:
        yield session
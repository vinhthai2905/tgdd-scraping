from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL
from sqlalchemy import text
from dotenv import load_dotenv
import os
import logging

load_dotenv()

URL_OBJECT = URL.create(
    'postgresql+psycopg2',
    username=os.getenv('USER'),
    password=os.getenv('USER_PASSWORD'),
    host=os.getenv('HOST'),
    database=os.getenv('DB'),
    port=int(os.getenv('PORT'))
)


engine = create_engine(URL_OBJECT, logging_name='myengine')

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

try:
    with engine.connect() as connection:
        connection.execute('SELECT 1')
        print('Database connected successfully')
except Exception as e:
        print(e)

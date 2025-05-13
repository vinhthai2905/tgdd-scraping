from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL
import os

URL_OBJECT = URL.create(
    'postgres+psycopg2',
    username=os.getenv('USER'),
    password=os.getenv('USER_PASSWORD'),
    host=os.getenv('HOST'),
    database=os.getenv('DB'),
    port=int(os.getenv('PORT'))
)


engine = create_engine(URL_OBJECT)
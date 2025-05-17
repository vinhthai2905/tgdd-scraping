from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db import db_connection
import app.models as model
import app.schemas as schema

app = FastAPI()

@app.get('/test')
def get_product(dbCon: Session = Depends(db_connection)):
    try:
        brand = dbCon.query(model.Product).all()
        return brand
    except Exception as e:
        print(e)
        

@app.post('/insert-product/tgdd')
def insert_datas_tgdd():
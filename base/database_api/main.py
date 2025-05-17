from pprint import pprint
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
        

@app.post('/insert-product/dtdd')
def insert_datas_tgdd(productDict: dict, dbCon: Session = Depends(db_connection)):
    try:
        productInfos: dict = productDict.get('product')
        product = model.Product(
            product_name=productInfos.get('productName'),
            product_image = productInfos.get('productImage'),
            exclusive_tag = productInfos.get('exclusiveTag'),
            product_new = productInfos.get('productNew'),
            product_installment = productInfos.get('productInstallment'),
            product_tech = productInfos.get('productTech'),
            product_price = productInfos.get('productPrice'),
            old_price = productInfos.get('oldPrice'),
            gift = productInfos.get('gift'),
            sold_quantity = productInfos.get('soldQuantity'),
            star = productInfos.get('star'),
        )
        
        dbCon.add(product)
        dbCon.flush()
        
        for choice in productDict.get('choices'):
            choiceObject = model.ProductChoice(product_id=product.id, choice=choice)
            dbCon.add(choiceObject)

        dbCon.commit()
        
    except Exception as e:
        print(e)
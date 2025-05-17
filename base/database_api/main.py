from pprint import pprint
from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db import db_connection
from datetime import datetime
import app.models as model
import app.schemas as schema
import logging



logging.basicConfig(
    filename=r'D:\Projects\Python\224-CDCSDL-FinalProject\base\database_api\logs\insert.log',  
    filemode='a',
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',  
    datefmt='%Y-%m-%d %H:%M:%S',
)

app = FastAPI()

@app.get('/dtdd')
def get_product(dbCon: Session = Depends(db_connection)):
    try:
        brand = dbCon.query(model.Product).all()
        return brand
    except Exception as e:
        print(e)
        

@app.post('/insert-product/dtdd')
async def insert_datas_tgdd(productDict: dict, dbCon: Session = Depends(db_connection)):
    try:
        productInfos: dict = productDict.get('product')
        existingProduct = dbCon.query(model.Product).filter_by(product_name=productInfos['productName']).first()
        
        if existingProduct:
            message = f"[{datetime.now()}] Skipping insertion: {existingProduct.product_name} duplicated."
            print(message)
            return {'message': message}
        else:
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
        error = f'[{datetime.now()}]: Error: Check logs for more details.'
        logging.error('An error occurred: {str(e)}')
        logging.error('Traceback:', exc_info=True)
        return {"status": "error", "detail": str(e)}
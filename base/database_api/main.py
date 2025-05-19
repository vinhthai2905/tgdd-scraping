from pprint import pprint
from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db import db_connection
from datetime import datetime
import app.models as model
import app.schemas as schema
import logging
import traceback


logging.basicConfig(
    filename='./logs/insert.log',  
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
def insert_phones(productDict: dict, dbCon: Session = Depends(db_connection)):
    try:
        productInfos: dict = productDict.get('product')
        existingProduct = dbCon.query(model.Product).filter_by(product_name=productInfos['productName']).first()
        
        if existingProduct:
            message = f"[{datetime.now()}] Skipping insertion: {existingProduct.product_name} duplicated."
            print(message)
            return {
                'status': 'Duplicated product.'
            }
            
        else:
            product = model.Product(
            product_name=productInfos.get('productName'),
            product_category=productInfos.get('productCategory'),
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
        logging.error(f'An error occurred while inserting phone datas. \n {repr(e)} \n {traceback.format_exc()}')
        pprint('An error occurred while inserting phone datas. Check logs for more details.')
        
        return {'Inserting': 'An error occurred while inserting phone datas. Check logs for more details.'}
    
    else:
        logging.info(f'Phone datas being inserted into database successfully.')
        pprint('Inserting phone datas into database sucessfully.')
        
        return {'Inserting': 'Inserted phone datas into database successfully.'}
    
@app.post('/insert-product/laptop')
def insert_laptops(productDict: dict, dbCon: Session = Depends(db_connection)):
    try:
        productInfos: dict = productDict.get('product')
        
        # if not productInfos or not isinstance(productInfos, dict):
        #     logging.error("Invalid or missing 'product' key in received data.")
        #     return {'status': 'Invalid product data.'}
        
        existingProduct = dbCon.query(model.Product).filter_by(product_name=productInfos.get('productName')).first()
        
        if existingProduct:
            message = f"[{datetime.now()}] Skipping insertion: {existingProduct.product_name} duplicated."
            logging.warning(f'Skipping insertion: {existingProduct.product_name} duplicated')
            print(message)
            return {
                'status': 'Duplicated product.'
            }
            
        else:
            product = model.Product(
            product_name=productInfos.get('productName'),
            product_category = productInfos.get('productCategory'),
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

            dbCon.commit()
            
    except Exception as e:
        logging.error(f'An error occurred while inserting laptop datas. \n {repr(e)} \n {traceback.format_exc()}')
        pprint('An error occurred while inserting laptop datas. Check logs for more details.')
        
        return {'Inserting': 'An error occurred while inserting laptop datas. Check logs for more details.'}
    
    else:
        logging.info(f'Laptop datas being inserted into database successfully.')
        pprint('Inserting laptop datas into database sucessfully.')
        
        return {'Inserting': 'Inserted laptop datas into database successfully.'}
from fastapi import FastAPI, Depends, Request, Path, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy import text, or_, func
from typing import List
from app.schemas import ProductRead
from app.db import db_connection, get_async_session
from datetime import datetime
from pprint import pprint
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

    
@app.get('/site/{category}/products')
async def get_products_by_category(
    category: str = Path(..., description="Product category (e.g. 'Mobile Phone', 'Laptop')"),
    dbCon: Session = Depends(get_async_session)
):
    try:
        result = await dbCon.execute(
            select(model.Product).where(model.Product.product_category == category)
        )
        products = result.scalars().all()
        return jsonable_encoder(products)
    
    except Exception as e:
        logging.error(f"Error fetching products for category '{category}': {repr(e)}\n{traceback.format_exc()}")
        return JSONResponse(
            status_code=500,
            content={"error": f"Unable to fetch products for category '{category}'."}
        )
        
@app.get('/products')
async def get_product(dbCon: Session = Depends(get_async_session)):
    try:
        results = await dbCon.execute(select (model.Product))
        products = results.scalars().all()
        return jsonable_encoder(products)

    except Exception as e:
        print(e)
        
@app.post('/insert-product/dtdd')
async def insert_phones(productDict: dict, dbCon: Session = Depends(get_async_session)):
    try:
        productInfos: dict = productDict.get('product')
        
        result = await dbCon.execute(
            select(model.Product).
            where(model.Product.product_name == productInfos['productName']))
        
        existingProduct = result.scalars().first()
        
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
            await dbCon.flush()
            
            for choice in productDict.get('choices'):
                choiceObject = model.ProductChoice(product_id=product.id, choice=choice)
                dbCon.add(choiceObject)

            await dbCon.commit()
            
    except Exception as e:
        logging.error(f'An error occurred while inserting phone datas. \n {repr(e)} \n {traceback.format_exc()}')
        pprint('An error occurred while inserting phone datas. Check logs for more details.')
        
        return {'Inserting': 'An error occurred while inserting phone datas. Check logs for more details.'}
    
    else:
        logging.info(f'Phone datas being inserted into database successfully.')
        pprint('Inserting phone datas into database sucessfully.')
        
        return {'Inserting': 'Inserted phone datas into database successfully.'}
    
@app.post('/insert-product/laptop')
async def insert_laptops(productDict: dict, dbCon: Session = Depends(get_async_session)):
    try:
        productInfos: dict = productDict.get('product')
        
        # if not productInfos or not isinstance(productInfos, dict):
        #     logging.error("Invalid or missing 'product' key in received data.")
        #     return {'status': 'Invalid product data.'}
        result = await dbCon.execute(select(model.Product).where(model.Product.product_name == productInfos['productName']))
        existingProduct = result.scalars().first()
        
        if existingProduct:
            message = f"[{datetime.now()}] Skipping insertion: {existingProduct.product_name} duplicated."
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
            await dbCon.flush()

            await dbCon.commit()
            
    except Exception as e:
        logging.error(f'An error occurred while inserting laptop datas. \n {repr(e)} \n {traceback.format_exc()}')
        pprint('An error occurred while inserting laptop datas. Check logs for more details.')
        
        return {'Inserting': 'An error occurred while inserting laptop datas. Check logs for more details.'}
    
    else:
        logging.info(f'Laptop datas being inserted into database successfully.')
        pprint('Inserting laptop datas into database sucessfully.')
        
        return {'Inserting': 'Inserted laptop datas into database successfully.'}
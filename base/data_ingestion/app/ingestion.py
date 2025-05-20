from pprint import pprint
from datetime import datetime
import logging
import traceback
import requests
import json
import httpx
import asyncio
 
logging.basicConfig(
    filename='./logs/send_json.log',  
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',  
    datefmt='%Y-%m-%d %H:%M:%S',
) 
                
async def sending_phone_datas():
    try:
        with open('../landing_zone/phones.json', 'r', encoding='utf-8') as jsonFile:
            datas: dict = json.load(jsonFile)
    except Exception as e:
        error = f'[{datetime.now()}]: Error while processing phone json file. Check logs for more errors.'
        logging.error(f'An error occurred: \n {repr(e)} \n {traceback.format_exc()}')
        
        return error
    else:
        for i, productInfos in datas.items():
            productInfos: dict
            for productName, value in productInfos.items():
                if productName == 'productChoices':
                    values: list = value
                    productDict: dict = dict()
                    choiceList: list = list()

                    for choiceValue in values:
                        if choiceValue == '-':
                            pass
                        else:
                            choiceList.append(choiceValue)
                else:
                    pass
                
            productDict[i] = {
                'product': productInfos,
                'choices': choiceList
            }
            # test = dict()
            # test[i] = {
            #     'choices': choiceList
            # }
            try:
                async with httpx.AsyncClient(timeout=20.0) as client:
                    await client.post('http://database_api:8002/insert-product/dtdd', json=productDict[i])
            except Exception as e:
                error = f'[{datetime.now()}]: An error occurred while requesting inserting phone datas. Check logs for more details.'
                pprint(error)
                logging.error(f'An error occurred while requesting inserting  phone datas. {repr(e)} \n {traceback.format_exc()} ')
                
                return error
            
        result = f'[{datetime.now()}] - Phone datas being sent sucessfully.'
        pprint(result)
        
        return result
    
async def sending_laptop_datas():
    try:
        with open('../landing_zone/laptops.json', 'r', encoding='utf-8') as jsonFile:
            datas: dict = json.load(jsonFile)
    except Exception as e:
        error = f'[{datetime.now()}]: Error while processing laptop json file. Check logs for more errors.'
        logging.error(f'An error occurred: \n {repr(e)} \n {traceback.format_exc()}')
        return error
    else:
        for i, productInfos in datas.items():
            productDict: dict = dict()
            productInfos: dict
            
            productDict[i] = {
                'product': productInfos,
            }
            # test = dict()
            # test[i] = {
            #     'choices': choiceList
            # }
            # pprint(productDict[i])
            try:
                async with httpx.AsyncClient() as client:
                    await client.post('http://database_api:8002/insert-product/laptop', json=productDict[i])
            except Exception as e:
                error = f'[{datetime.now()}] - An error occured while requesting inserting laptop datas. Check logs for more details.'
                logging.error(f'An error occurred while requesting inserting laptop datas. \n {repr(e)} \n {traceback.format_exc()}')
                pprint(error)
                
                return error
            
        result = f'[{datetime.now()}] - Laptop datas being sent sucessfully.'
        pprint(result)
        
        return result
    
if __name__ == '__main__':
    # sending_phone_datas()
    sending_laptop_datas()                                                                                                                                                                                                                                                                                                                                                                                                               
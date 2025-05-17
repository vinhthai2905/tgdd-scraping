from pprint import pprint
from datetime import datetime
import logging
import requests
import json
import database_api.app.db as db
import database_api.app.models as models
 
logging.basicConfig(
    filename=r'D:\Projects\Python\224-CDCSDL-FinalProject\base\data_ingestion\logs\send_json.log',  
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',  
    datefmt='%Y-%m-%d %H:%M:%S',
) 
                
def sending_product_datas():
    try:
        with open(r'D:\Projects\Python\224-CDCSDL-FinalProject\base\landing_zone\phones.json', 'r', encoding='utf-8') as jsonFile:
            datas: dict = json.load(jsonFile)
    except Exception as e:
        error = f'[{datetime.now()}]: Error: Check logs for more details.'
        logging.error('An error occurred: {str(e)}')
        logging.error('Traceback:', exc_info=True)
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
                requests.post('http://127.0.0.1:8001/insert-product/dtdd', json=productDict[i])
            except Exception as e:
                error = f'[{datetime.now()}]: Error: Check logs for more details.'
                pprint(error)
                logging.error(f'An error occurred while requesting inserting datas. {repr(e)}')
                return error
            
        logging.info('Data being sent successfully.')
        result = f'[{datetime.now()}] - Data being sent sucessfully'
        pprint(result)
        return result
    
    
if __name__ == '__main__':
    sending_product_datas()
                                                                                                                                                                                                                                                                                                                                                                                                               
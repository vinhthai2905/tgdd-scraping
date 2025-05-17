import requests
import json
import database_api.app.db as db
import database_api.app.models as models
from pprint import pprint

# def ingest_phones():
#     try:
#         with open(r'D:\Projects\Python\224-CDCSDL-FinalProject\base\landing_zone\phones.json', 'r', encoding='utf-8') as jsonFile:
#             datas: dict = json.load(jsonFile)
#     except Exception as e:
#         print(e)
#     else:
#         with db.db_connection() as db_connection:
#             for i, productInfos in datas.items():
#                 productInfos: dict
#                 product = models.Product(
#                     product_name=productInfos.get('productName'),
#                     product_image = productInfos.get('productImage'),
#                     exclusive_tag = productInfos.get('exclusiveTag'),
#                     product_new = productInfos.get('productNew'),
#                     product_installment = productInfos.get('productInstallment'),
#                     product_tech = productInfos.get('productTech'),
#                     product_price = productInfos.get('productPrice'),
#                     old_price = productInfos.get('oldPrice'),
#                     gift = productInfos.get('gift'),
#                     sold_quantity = productInfos.get('soldQuantity'),
#                     star = productInfos.get('star'),
#                 )
                
#                 db_connection.add(product)
#                 db_connection.flush()
                
#                 # pprint(f'{i}: {productInfos}')
#                 # print('--------------------')
#                 for productName, value in productInfos.items():
#                     if productName == 'productChoices':
#                         values: list = value
#                         for choiceValue in values:
#                             if choiceValue == '-':
#                                 pass
#                             else:
#                                 choice_obj = models.ProductChoice(product_id=product.id, choice=choiceValue)
#                                 db_connection.add(choice_obj)
#                     else:
#                         pass
#                     # print(f'{productName}: {value}')
#             #     for productKey, value in productInfos:
#             #         if productKey == 'productChoices':
#             #             for choice in value:
#             #                 print(productKey, value)            
            
#                 db_connection.commit()
                
def sending_product_datas():
    try:
        with open(r'D:\Projects\Python\224-CDCSDL-FinalProject\base\landing_zone\phones.json', 'r', encoding='utf-8') as jsonFile:
            datas: dict = json.load(jsonFile)
    except Exception as e:
        print(e)
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
            
            try:
                requests.post('http://127.0.0.1:8000/insert-product/dtdd', json=productDict[i])
                print('Ok')
            except Exception as e:
                print(e)
        
            
            
                
if __name__ == '__main__':
    sending_product_datas()
                                                                                                                                                                                                                                                                                                                                                                                                               
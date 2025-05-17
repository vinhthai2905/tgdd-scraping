from bs4 import BeautifulSoup, Tag
from pprint import pprint
from datetime import datetime
import requests
import traceback
import json
import logging


logging.basicConfig(
    filename=r'D:\Projects\Python\224-CDCSDL-FinalProject\base\data_crawling\logs\crawler.log',  
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',  #
    datefmt='%Y-%m-%d %H:%M:%S'  
)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

datas = dict()

def phone_crawling():
    try:
        htmlText = requests.get('', headers=headers).text
        phoneSoup = BeautifulSoup(htmlText, 'lxml')
        phoneInfos = phoneSoup.find('ul', class_='listproduct')
        productChoices = str()
        itemCount = 0
        try:
            for i, product in enumerate(phoneInfos.find_all('li', class_='item ajaxed __cate_42')):
                itemCount = itemCount + 1
                productHref = product.find('a')
                productBanners = product.find('div', class_='item-img item-img_42')
                productTags = productHref.find('div', class_='item-label')
                productNew = productTags.find('span', class_='ln-new')
                productInstallment = productTags.find('img', class_='lb-tragop')
                productRatings = product.find('div', class_='rating_Compare has_compare has_quantity')
                
                productName = ' '.join(product.find('h3').getText().split())
                productTech = ' '.join(product.find('div', class_='item-compare gray-bg').getText().split())
                productPrice = product.find('strong', class_='price').text
                
                imageTags = productBanners.find_all('img')
                
                if len(imageTags) == 2:
                    productImageURL = imageTags[0].get('data-src')
                    if productImageURL == None:
                        productImageURL = imageTags[0].get('src')
                        
                    exclusiveTag = imageTags[1].get('data-src')
                    if exclusiveTag == None:
                        exclusiveTag = imageTags[1].get('src')
                else:
                    exclusiveTag = None
                    productImageURL = imageTags[0].get('data-src')
                    if productImageURL == None:
                        productImageURL = imageTags[0].get('src')
                    
                if productNew:
                    productNew = productNew.text
                    
                if productInstallment:
                    productInstallment = productInstallment.text
                
                if productHref.find('ul') == None:
                    productChoices = None
                else:
                    tempList = list()
                    for productCapacity in productHref.find('ul').find_all('li'):
                        tempList.append(productCapacity.text)

                productChoices = ' '.join(tempList)
                # if productChoicesTemp.count('-'):
                #     productChoices = productChoicesTemp.split(' - ')
                # else:
                #     productChoices = productChoicesTemp.split()
                # print(productChoices)
                # breakpoint()
                        
                if product.find('p', class_='price-old black') == None:
                    oldPrice = None
                else:
                    oldPrice = product.find('p', class_='price-old black').text
    
                if product.find('p', class_='item-gift') == None:
                    gift = None
                else:
                    gift = product.find('p', class_='item-gift').text

                if productRatings == None:
                    soldQuantity = star = None
                else:
                    soldQuantity = productRatings.find('span').text
                    star = productRatings.find('b').text
                
                                
                datas[f'Item_{i}'] = {
                    'productImage': productImageURL,
                    'exclusiveTag': exclusiveTag,
                    'productNew': productNew,
                    'productInstallment': productInstallment,
                    'productName': productName,
                    'productTech': productTech,
                    'productChoices': productChoices.split(),
                    'productPrice': productPrice,
                    'oldPrice': oldPrice,
                    'gift': gift,
                    'soldQuantity': soldQuantity,
                    'star': star    
                }
                # breakpoint()
        
        except Exception as e:
            error = f'[{datetime.now()}]: Error: Check logs for more details.'
            print(error)
            logging.error('An error occurred: {str(e)}')
            logging.error('Traceback:', exc_info=True)
            
            return error            
        else:
            with open(r'D:\Projects\Python\224-CDCSDL-FinalProject\base\landing_zone\phones.json', 'w', encoding='utf-8') as jsonFile:
                json.dump(datas, jsonFile, indent=4, ensure_ascii=False)

    except Exception as e:
        error = f'[{datetime.now()}]: Error: Check logs for more details.'
        logging.error('An error occurred: {str(e)}')
        logging.error('Traceback:', exc_info=True)
        print(error)
        
        return error
        
    else:
        currentDatetime = datetime.now()
        succeed = logging.info(f'{currentDatetime}: Scraped https://www.thegioididong.com/dtdd#c=42&o=13&pi=0 successfully. {itemCount} Total')
        
        return succeed

    

if __name__ == '__main__':
    phone_crawling()

        






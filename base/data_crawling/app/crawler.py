import time
import requests
import traceback
import json
import logging
import httpx
import asyncio
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from bs4 import BeautifulSoup, Tag
from pprint import pprint
from datetime import datetime


logging.basicConfig(
    filename=r'./logs/crawler.log',  
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',  #
    datefmt='%Y-%m-%d %H:%M:%S'  
)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

datas = dict()
# def get_fullpage(url):
#     chrome_options = Options()
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--disable-gpu')

#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get(url)
#     wait = WebDriverWait(driver, 10) 
#     while True:
#         try:
#             btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'see-more-btn')))
#             driver.execute_script("arguments[0].click();", btn)
#             time.sleep(2)
#         except (TimeoutException, ElementClickInterceptedException, NoSuchElementException):
#             break

#     html = driver.page_source
#     driver.quit()
#     return html  

async def phone_crawling():
    try:
        htmlText = requests.get('https://www.thegioididong.com/dtdd#c=42&o=13&pi=0', headers=headers).text
        phoneSoup = BeautifulSoup(htmlText, 'lxml')
        phoneInfos = phoneSoup.find('ul', class_='listproduct')
        productChoices = str()
        itemCount = 0
        try:
            for i, product in enumerate(phoneInfos.find_all('li', class_='item ajaxed __cate_42')):
                if i >= 30:
                    break
                itemCount = itemCount + 1
                productHref = product.find('a')
                productBanners = product.find('div', class_='item-img item-img_42')
                productTags = productHref.find('div', class_='item-label')
                productNew = productTags.find('span', class_='ln-new')
                productInstallment = productTags.find('img', class_='lb-tragop')
                productRatings = product.find('div', class_='rating_Compare has_compare has_quantity')
                
                productName = ' '.join(product.find('h3').getText().split())
                productTech = ' '.join(product.find('div', class_='item-compare gray-bg').getText().split())
                productPrice = product.find('strong', class_='price')
                
                if productPrice:
                    productPrice = product.find('strong', class_='price').text
                else:
                    productPrice = None
                
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
                    'productCategory': 'Mobile Phone',
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
            print(f'[{datetime.now()}]: Error while extracting phone datas after requesting sucessfully from the source: Check logs for more details.')
            logging.error(f'{repr(e)} \n {traceback.format_exc()}')
            
            return 'An error occurred while extracting phone datas after requesting sucessfully from the source. Check logs for more details.'           
        else:
            with open('../landing_zone/phones.json', 'w', encoding='utf-8') as jsonFile:
                json.dump(datas, jsonFile, indent=4, ensure_ascii=False)
            
    except Exception as e:
        print(f'[{datetime.now()}]: Error occured while requesting phone datas from the source: Check logs for more details.')
        logging.error(f'{repr(e)} \n {traceback.format_exc()}')
        
        return 'An error occured while requesting phone datas from the source: Check logs for more details.'
    
    else:
        logging.info(f'Scraped https://www.thegioididong.com/dtdd#c=42&o=13&pi=0 successfully. {itemCount} Total')
        
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                await client.get('http://0.0.0.0:8001/sending-data/phone')
        except Exception as e:
            logging.error(f'An error occurred while requesting sending data. \n {repr(e)} \n {traceback.format_exc()}')
            return {
                'Scraping': f'{datetime.now()}: Scraped https://www.thegioididong.com/dtdd#c=42&o=13&pi=0 successfully. {itemCount} Total',
                'Requesting': f'{datetime.now()}: Requesting phone datas being sent failed. Check logs for more details.'
            }
        else:
            logging.info('Requesting sending datas sucessfully.')
            
            return {
                'Scraping' : f'{datetime.now()}: Scraped https://www.thegioididong.com/dtdd#c=42&o=13&pi=0 successfully. {itemCount} Total',
                'Requesting': f'{datetime.now()}: Requesting phone datas being sent successfully. Check logs for more details.'
            }


async def laptop_crawling():
    try:
        htmlText = requests.get('https://www.thegioididong.com/laptop#c=44&o=13&pi=0', headers=headers).text
        laptopSoup = BeautifulSoup(htmlText, 'lxml')
        laptopInfos = laptopSoup.find('ul', class_='listproduct')
        itemCount = 0
        try:
            for i, product in enumerate(laptopInfos.find_all('li', class_=['item', '__cate_44'])):
                if i >= 30:
                    break
                itemCount = itemCount + 1
                
                productHref = product.find('a')
                if not productHref:
                    logging.warning(f'Missing <a> tag in product {i}, skipping.')
                    continue
                
                productBanners = product.find('div', class_='item-img item-img_44')
                productTags = productHref.find('div', class_='item-label')
                productNew = productTags.find('span', class_='ln-new')
                productInstallment = productTags.find('img', class_='lb-tragop')
                productRatings = product.find('div', class_='rating_Compare has_compare has_quantity')
                
                productName = ' '.join(product.find('h3').getText().split())
                productTech = ' '.join(product.find('div', class_='item-compare gray-bg').getText().split())
                productPrice = product.find('strong', class_='price')
                
                if productPrice:
                    productPrice = product.find('strong', class_='price').text
                else:
                    productPrice = None
                
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
                    'productCategory': 'Laptop',
                    'productTech': productTech,
                    'productPrice': productPrice,
                    'oldPrice': oldPrice,
                    'gift': gift,
                    'soldQuantity': soldQuantity,
                    'star': star    
                }
                # breakpoint()
        
        except Exception as e:
            print(f'[{datetime.now()}]: Error while extracting laptop datas after requesting sucessfully from the source: Check logs for more details.')
            logging.error(f'{repr(e)} \n {traceback.format_exc()}')
            
            return 'An error occurred while extracting datas after requesting sucessfully from the source. Check logs for more details.'           
        else:
            with open('../landing_zone/laptops.json', 'w', encoding='utf-8') as jsonFile:
                json.dump(datas, jsonFile, indent=4, ensure_ascii=False)

    except Exception as e:
        logging.error(f'{repr(e)} \n {traceback.format_exc()}')
        print('An error occured while requesting laptop datas from the source. Check logs for more details.')
        
        return 'An error occured while requesting laptop datas from the source. Check logs for more details.'
        
    else:
        logging.info(f'Scraped https://www.thegioididong.com/laptop#c=44&o=13&pi=0 successfully. {itemCount} Total')
        
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                await client.get('http://0.0.0.0:8001/sending-data/laptop')
        except Exception as e:
            logging.error(f'An error occurred while requesting sending laptop datas. \n {repr(e)} \n {traceback.format_exc()}')
            return {
                'Scraping': f'{datetime.now()}: Scraped https://www.thegioididong.com/laptop#c=44&o=13&pi=0 successfully. {itemCount} Total',
                'Requesting': f'{datetime.now()}: Requesting laptop datas being sent failed. Check logs for more details.'
            }
        else:
            logging.info('Requesting sending laptop datas sucessfully.')
            return {
                'Scraping' : f'{datetime.now()}: Scraped https://www.thegioididong.com/laptop#c=44&o=13&pi=0 successfully. {itemCount} Total',
                'Requesting': f'{datetime.now()}: Requesting laptop datas being sent successfully. Check logs for more details.'
            }

if __name__ == '__main__':
    phone_crawling()
    laptop_crawling()
    

        






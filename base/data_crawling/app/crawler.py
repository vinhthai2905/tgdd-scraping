from bs4 import BeautifulSoup, Tag
from pprint import pprint
from datetime import datetime
import requests
import traceback

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

try:
    htmlText = requests.get('https://www.thegioididong.com/dtdd#c=42&o=13&pi=0', headers=headers).text
except Exception as e:
    pprint(traceback.print_exception(type(e), e, e.__traceback__))
else:
    phoneSoup = BeautifulSoup(htmlText, 'lxml')
    phoneInfos = phoneSoup.find('ul', class_='listproduct')
    
    try:
        for i, product in enumerate(phoneInfos.find_all('li', class_='item ajaxed __cate_42')):
            productHref = product.find('a')
            productImage = product.find
            productTags = productHref.find('div', class_='item-label')
            productNew = productTags.find('span', class_='ln-new')
            productInstallment = productTags.find('span', class_='lb-tragop')
            
            if productNew:
                productNew = productNew.text
            if productInstallment:
                productInstallment = productInstallment.text
            
    except Exception as e:
        print(traceback.print_exception(type(e), e, e.__traceback__))

    try:
        with open('../templates/phone/page_1.html', 'w', encoding='utf-8') as file:
            file.write(str(phoneInfos.prettify()))
    except Exception as e:
        pprint(traceback.print_exception(type(e), e, e.__traceback__))
        
    currentDatetime = datetime.now()
    print(f'{currentDatetime}: Scraped successfully.')


    

        






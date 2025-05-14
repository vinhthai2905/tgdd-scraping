from bs4 import BeautifulSoup
import requests


htmlText = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=')

jobsSoup = BeautifulSoup(htmlText, 'lxml')

jobsSoup.find_all('div', class_='clearfix job-bx wht-shd-bx')

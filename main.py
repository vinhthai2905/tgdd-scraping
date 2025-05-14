import requests
import traceback
from pprint import pprint
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

response = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=', headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')
else:
    print(f"Failed to fetch page: {response.status_code}")
    
try:
    jobs_data = dict()
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    try:
        for i, job in enumerate(jobs):
            
            company = job.find('div', class_='d-flex d-flex-align-item')
            jobInfo = job.find('ul', class_='list-job-dtl clearfix') 
            jobEligibility = job.find('ul', class_='top-jd-dtl mt-16 clearfix')

            # companyName = ''.join(company.h3.text.split())
            companyName = ' '.join(company.h3.getText().split())
            publishedDate = ' '.join(company.span.getText().split())
            jobTitle = ' '.join(job.find('h2', class_='heading-trun').getText().split())
            jobDesc = ' '.join(jobInfo.find('li', class_='job-description__').getText().split())
            jobSkill = jobInfo.find('li', class_=False).getText().split()
                                    
            
            liElements = jobEligibility.find_all('li')
            if (len(liElements) == 3):
                location = ' '.join(liElements[0].getText().split())
                experience = liElements[1].text
                salary = liElements[2].text
            
            jobs_data[f'job_{i}'] = {
                'company': companyName,
                'publishedDate': publishedDate,
                'location': location,
                'jobTitle': jobTitle,
                'jobSkill': jobSkill,
                'description': jobDesc,
                'experience': experience,
                'salary': salary,
            }          
            
    except Exception as e:
        print(f'Couldn\'t find information about the job: {e}')
        print("Traceback details:")
        traceback.print_exc()
        
except Exception as e:
    print(f'There has been an error: {e}')
    
print(jobs_data)

FROM python

WORKDIR /base/data_crawling

COPY . /base/data_crawling

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


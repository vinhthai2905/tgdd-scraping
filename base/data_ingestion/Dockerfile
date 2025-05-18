FROM python

WORKDIR /base/data_ingestion

COPY . /base/data_ingestion

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8001"]
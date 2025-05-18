FROM python

WORKDIR /base/database_api

COPY ./ /base/database_api

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002", "--reload"]

# TGDD Scraping Documents:
A simple API built with FastAPI and PostgreSQL, containerized using Docker. The main goal is to scrape product data.

The websites from which product data is scraped:

### 🌐 Sources:

- [https://www.thegioididong.com/dtdd](https://www.thegioididong.com/dtdd)
- [https://www.thegioididong.com/laptop](https://www.thegioididong.com/laptop)

## 🛠️ How It's Made:

## #Languages & Tools**

### Programming & Markup Languages

🐍 [Python](https://www.python.org/)
🔄 [TypeScript](https://www.typescriptlang.org/)
🌐 [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
🎨 [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)

### Core Tools:

🐘 [PostgreSQL](https://www.postgresql.org/)

🐳 [Docker](https://www.docker.com/) - Used for isolating services and encapsulating necessary things for the software instead of doing it traditional ways.

### Core Packages:

⚡ [FastAPI](https://fastapi.tiangolo.com/) - Used for building microservices for scraping and data ingestion.

⚛️ [React](https://react.dev/) - Used for building dynamic front-end interfaces.

🧪 [SQLAlchemy](https://www.sqlalchemy.org/) - Used for opening connections towards the database engine and performing queries.

✅ [Pydantic](https://docs.pydantic.dev/latest/) - Used for validating incoming data through API endpoints.

### Web Scraping Packages

🍜 [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Used for parsing static html tags.

🤖 [Selenium](https://www.selenium.dev/documentation/) - Used for automated browsing and handling dynamic content.

🌐 [Requests](https://requests.readthedocs.io/en/latest/) - Used for making HTTP(or HTTPS) to certain domains. In this particular topic [Sources](#tgdd-scraping-documents).

### Minor Packages:

📝 [Logging](https://docs.python.org/3/library/logging.html) - Used for writing logs for examining the results.

## Tasks List:
- ✅ Data Crawling API Service
- ✅ Data Ingestion API Service
- ✅ Database API Service
- ✅ Web Page Service
- ✅ Database Service
- ✅ Nginx Service
- ✅ Logging
- ✅ Containerized Services
 
## 🛠️ Instructions:

### 💾 Clone the Repository

1. git clone https://github.com/vinhthai2905/TGDD_Scraping.git
2. cd TGDD_Scraping/base

### 🐳 Running with Docker Compose

3. docker-compose -f ./docker-compose.yml -p tgdd up --build

## 🔍 Examining logs

4. ### Open three terminal and type in each
 - docker attach data_crawling
 - docker attach data_ingestion
 - docker attach database_api

### 🛑 Stop the service

5. docker-compose -f./docker-compose.yml -p tgdd down

## Interactive API Docs

## 📎 Navigators

➡️ [Go to Scraping Documents](#tgdd-scraping-documents)

➡️ [Go to How It's Made](#how-its-made)

➡️ [Go to How Tasks List](#tasks-list)

➡️ [Go to Instructions](#instructions)

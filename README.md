# News Feed Scraper API with FastAPI

[![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Python](https://img.shields.io/badge/python-3.10-blue.svg)

#### Presentation

In this repo I demonstrate how to easily build your own scraping API using `FastAPI` and the `Request-html` library. And how to build a basic news feed updated in real time.
<br>
The abstracts of articles and their links have been collected from [Newswire](https://www.einpresswire.com/), an online press collector and distributor.
<br>
The information concerns the latest news from Africa by regions.

The API has been enriched with some endpoints and several search parameters accessible on the Swagger interface delivered with FastAPI

#### Prerequisites

- Python

versions`3.10` or `3.8`

##### Install and run

open a new folder with terminal

```shell
mkdir my_new_folder
```

create a virtual environment

```shell
virtualenv venv
```

... activate it

```shell
source venv/bin/activate
```

- Clone the repo
- open NewsScraper_API folder
- install dependencies

```shell
pip install -r requirements.txt
```

and run main.py with uvicorn

```shell
uvicorn main:app --reload
```

To launch the documentation interface, you can use the following endpoints:

docs: Swagger UI, which allows you to test the API and see the automatically generated documentation.
redoc: ReDoc, an alternative to Swagger UI

```
http://localhost:8000/docs
http://localhost:8000/redoc
```













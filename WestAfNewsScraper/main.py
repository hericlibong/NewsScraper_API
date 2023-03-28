
from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel
from typing import List, Union, Optional
from scraper import Scraper
from utils import regions



app = FastAPI(title='News Scraper')
news = Scraper()


class Article(BaseModel):
    region : Union[str, None] = None
    title : str
    link:str
    publication_date : str
    preview : str
    source : str    

class ArticleResponse(BaseModel):
    articles : List[Article]
    
@app.get("/")
async def start_endpoint():
    return {"message" : "Hello News Scraper"}

# get full liste scraped articles
@app.get("/articles", response_model=ArticleResponse)
async def read_full_articles(
    keyword : Optional[str] = Query(None, description="A keyword to search for in the title or preview of all the articles.")
):
    
    """
    loading all articles from all regions.
    """
    articles_list = []
    for reg in regions:
        articles = news.scraper_data(reg)
    
        articles_list.extend(articles)
    if keyword:
        articles_list = [article for article in articles_list if 'title' in article and 'preview' in article and keyword.lower() in article['title'].lower() or keyword.lower() in article['preview'].lower()]
    return {"articles":articles_list}


# get articles by region name and keyword
@app.get("/articles/{region}")
async def read_articles_by_region_and_keyword(
    region: Optional[str] = None, 
    keyword: Optional[str] = Query( None,  description= "A keyword to search for in the title or preview of the articles.")
                                
):
    """
    Retrieve articles from a specific region and containing a specific keyword in title or preview.
    """
    if region:
        if region not in regions:
            raise HTTPException(status_code=404, detail="Region not found")
        articles = news.scraper_data(region)
    else:
        articles = []
        for reg in regions:
            articles.extend(news.scraper_data(reg))
    if keyword:
        articles = [article for article in articles if 'title' in article and 'preview' in article and keyword.lower() in article['title'].lower() or keyword.lower() in article['preview'].lower()]
    return {"articles": articles}


# get articles by region name 
@app.get("/{region}", response_model=ArticleResponse, tags = regions) 
async def read_articles_by_region(
    region : str = Path(..., title = "The name of the region to retrieve articles for",
                        description="The name of the region must be one of the following: african-island-nations, central-africa, east-africa, horn-of-africa, north-africa, southern-africa, west-africa."),
      keyword: Optional[str] = None
    ):
    """
    Retrieve articles from a specific region.
    """
    if region not in regions:
        raise HTTPException(status_code=404, detail="Region not found")
    if keyword:
        articles = [article for article in articles if keyword.lower() in article.title.lower() or keyword.lower() in article.preview.lower()]
    articles = news.scraper_data(region)
    return {"articles":articles}


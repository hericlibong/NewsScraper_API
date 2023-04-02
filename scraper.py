from requests_html import HTMLSession
from utils import regions


class Scraper():
    
    def scraper_data(self, region):
        articles_count = 0
        url = f'https://world.einnews.com/region/{region}'
        session = HTMLSession()
        response =session.get(url)
        base_url = 'https://world.einnews.com/'
        container = response.html.xpath("//ul[@class='pr-feed']")[0]    
        articles = container.find('div.article-content')
        articles_items = []
        for article in articles:
            articles_count+=1
            title = article.find('h3', first=True).text.strip()
            title_link = base_url + article.find("a", first=True).attrs["href"]
            
            article_date = article.find('div.pretitle', first=True).text.strip()
            
            try: 
                article_preview = article.find('p.excerpt', first=True).text
            except Exception as e:
                article_preview = "None"
            try:
                article_source = article.find("div.channels b", first=True).text
            except  Exception as e:
                article_source = "None"
            results = {
                'region':region,
                'title':title,
                'link':title_link,
                'publication_date': article_date,
                'preview':article_preview,
                'source':article_source
                }
            articles_items.append(results)
                
        print(f"Processed {articles_count} articles in {region}")            
        return articles_items
           
        
#tests scraper       
#news = Scraper()
#for reg in regions:
#print(news.scraper_data(regions[6]))




    
    


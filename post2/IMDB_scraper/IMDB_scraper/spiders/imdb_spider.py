# to run 
# scrapy crawl imdb_spider -o movies.csv

import scrapy

class ImdbSpider(scrapy.Spider):
    name = 'imdb_spider'
    
    start_urls = ['https://www.imdb.com/title/tt1533117/']

    def parse(self, response):
        next_page = response.css("a.ipc-metadata-list-item__icon-link").attrib["href"]
        if next_page:           
            next_page=response.urljoin(next_page)
            yield scrapy.Request(next_page,callback= self.prase_full_credits)

    
    
    def prase_full_credits(self,response):
        for next_page in [a.attrib["href"] for a in response.css("td.primary_photo a")]:
            next_page=response.urljoin(next_page)
            yield scrapy.Request(next_page,callback= self.prase_actor_page)

    def prase_actor_page(self,response):
        actor_name=response.css("h1.header span.itemprop::text").get()                             
        for quote in response.css("div.filmo-row"):
            movie_or_TV_name=quote.css("b a::text").get()
            yield {"actor" : actor_name, "movie_or_TV_name" : movie_or_TV_name}
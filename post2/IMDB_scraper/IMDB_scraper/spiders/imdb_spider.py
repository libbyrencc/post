# to run 
# scrapy crawl imdb_spider -o movies.csv

import scrapy

class ImdbSpider(scrapy.Spider):
    name = 'imdb_spider'
    
    start_urls = ['https://www.imdb.com/title/tt0106145/']

    def parse(self, response):
        next_page = response.css("a.ipc-metadata-list-item__icon-link").attrib["href"]
        print(next_page)
        print("                          ")
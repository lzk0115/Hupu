import scrapy

class Text_Spider(scrapy.Spider):    
    name = "text"
    start_url = ["https://bbs.hupu.com/bxj/highlights"]


    def parse(self, response):
        

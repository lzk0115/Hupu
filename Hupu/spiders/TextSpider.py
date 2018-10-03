import scrapy
from  Hupu import items


class TextSpider(scrapy.Spider):
    name = "text"
    start_urls = ["https://bbs.hupu.com/bxj/highlights-" + str(i+1) for i in range(10000)]

    def parse(self, response):
        item = items.TextItem()

        elements = response.css('div.case')
        for e in elements:
            text = e.extract()
            item['text'] = text
            yield item

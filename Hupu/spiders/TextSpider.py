import scrapy


class TextSpider(scrapy.Spider):
    name = "text"
    start_urls = ["https://bbs.hupu.com/bxj/highlights-" + str(i+1) for i in range(100)]

    def parse(self, response):
        number = response.url.split('-')[-1]
        filename = 'hupu_page/hupu-%s.html' % number

        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('save file: %s' % filename)

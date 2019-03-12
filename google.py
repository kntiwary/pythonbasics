import scrapy


class GogleSpider(scrapy.Spider):
    name = 'gogle'

    allowed_domains = ['google.co.in']
    start_urls = ['https://www.google.co.in/?gfe_rd=cr/']

    def __init__(self, word="electronics", *args, **kwargs):
        super(GogleSpider, self).__init__(*args, **kwargs)
        self.word = word

    def parse(self, response):
        print("word:", self.word)
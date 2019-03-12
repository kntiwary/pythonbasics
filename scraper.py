import scrapy



class QuotesSpider(scrapy.Spider):
    name = 'scraper'
    # start_urls = [
    #     'http://quotes.toscrape.com/tag/humor/',
    # ]

    start_urls = [
        'http://wework.co.in/india/',

    ]
    # start_urls =[
    #     'https://www.reddit.com/r/gameofthrones/',
    # ]
    #
    def parse(self, response):
        print(response.css('div.carouselImage').extract())
        # print(response.matches('text()','wework').extractoucght())
        # print(response.xpath('div/carouselImage/style/text()').extract())
        # print(response.matches('//p[contains(text(), "wework")]').extract())
        # yield {
        #
        # }




    # def parse(self, response):
    #     for quote in response.css('div.quote'):
    #         # print("RESPONSE",response)
    #         yield {
    #             'text': quote.css('span.text::text').get(),
    #             'author': quote.xpath('span/small/text()').get(),
    #         }
    #
    # def parse(self, response):
    #     for quote in response.css('.your-class').extract_first():
    #         # print("RESPONSE",response)
    #         yield {
    #             'text': quote.css('.carouselImage::text').get(),
    #             'author': quote.xpath('span/small/text()').get(),
    #         }
    #
    #
    #
    #     next_page = response.css('li.next a::attr("href")').get()
    #     if next_page is not None:
    #         yield response.follow(next_page, self.parse)
    #
    #

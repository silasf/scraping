import scrapy


class QuotesSpider(scrapy.Spider):
    name = "scraping"

    def start_requests(self):
        urls = [
            'https://nerdstore.com.br/categoria/especiais/game-of-thrones/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       
        for item in response.css('a.woocommerce-LoopProduct-link.woocommerce-loop-product__link'):
                yield {
                    'nome': item.css('h2.woocommerce-loop-product__title::text').get(),
                    'link':  item.css('img.attachment-woocommerce_thumbnail.size-woocommerce_thumbnail').attrib['src'],
                    'price': item.css('span.woocommerce-Price-amount.amount::text').get(),
                }

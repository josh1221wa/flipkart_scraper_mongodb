import scrapy

from flipkart_scraper.items import FlipkartScraperItem


class FlipkartSpiderSpider(scrapy.Spider):
    name = "flipkart_spider"
    allowed_domains = ["www.flipkart.com"]
    start_urls = ["https://www.flipkart.com/search?q=phones"]
    page = 1

    def parse(self, response):
        for counter in range(2, 26):
            item = FlipkartScraperItem()
            item['name'] = response.xpath(
                f'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[{counter}]/div/div/div/a/div[2]/div[1]/div[1]').css("::text").get()

            item['url'] = 'https://www.flipkart.com' + response.xpath(
                f'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[{counter}]/div/div/div/a').css("::attr(href)").get()
            item['price'] = response.xpath(
                f'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[{counter}]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]').css("::text").get()
            item['rating'] = response.xpath(
                f'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[{counter}]/div/div/div/a/div[2]/div[1]/div[2]/span[1]/div').css("::text").get()
            item['image'] = response.xpath(
                f'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[{counter}]/div/div/div/a/div[1]/div[1]/div/div/img').css("::attr(src)").get()
            yield item

        if self.page != 10:
            self.page += 1
            next_page = f'https://www.flipkart.com/search?q=phones&page={self.page}'
            yield scrapy.Request(next_page, callback=self.parse)

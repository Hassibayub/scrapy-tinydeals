# -*- coding: utf-8 -*-
import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.tinydeal.com']
    start_urls = ['https://www.tinydeal.com/specials.html']

    def parse(self, response):

       for item in response.xpath("//ul[@class='productlisting-ul']/div/li"):

            item_name = item.xpath(".//a[@class='p_box_title']/text()").get()
            item_url =  item.xpath(".//a[@class='p_box_title']/@href").get()
            item_discount_price = item.xpath(".//div[@class = 'p_box_price']/span[@class='productSpecialPrice fl']/text()").get()
            item_original_price = item.xpath(".//div[@class = 'p_box_price']/span[@class='normalprice fl']/text()").get()


            yield {
                "name ": item_name,
                "url ": "www.tinydeal.com/" + item_url,
                "discount price ": item_discount_price,
                "original price ": item_original_price 
            }
        
        next_page = response.xpath("//a[@class='nextPage']")

        if next_page:
            yield scrapy.Request(url=next_page, callback= self.parse)

        

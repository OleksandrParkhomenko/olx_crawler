# -*- coding: utf-8 -*-
import scrapy

from olx_crawler.items import OlxCrawlerItem
from scrapy.http.request import Request


class OlxSpiderSpider(scrapy.Spider):
    name = 'olx_spider'
    allowed_domains = ['www.olx.ua']
    start_urls = ['https://www.olx.ua/zhivotnye/sobaki/kiev/?search%5Bdistrict_id%5D=11/' , 'https://www.olx.ua/zhivotnye/koshki/kiev/?search%5Bdistrict_id%5D=11/']

    def parse(self, response):
        next_page = response.css("a.link.pageNextPrev::attr(href)").extract()
        next_page = next_page[-1]

        for ad in response.css("div.offer-wrapper").css("a.marginright5::attr(href)"):
            ad_url = ad.extract()
            yield Request(ad_url, callback=self.parse_item)

        if next_page != response.url:
            yield Request(next_page, callback=self.parse)

    def parse_item(self, response):
        item = OlxCrawlerItem()
        item["title"] = response.css("div.offer-titlebox h1::text").extract_first().lstrip().rstrip()
        item["info"] = response.css("[id='textContent']::text").extract_first().lstrip().rstrip()
        item["photos"] = response.css("div.photo-glow img::attr(src)").extract()
        item["ad_id"] = response.css("div.offer-titlebox__details small::text").extract_first()

        yield item

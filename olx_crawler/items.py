# -*- coding: utf-8 -*-

import scrapy


class OlxCrawlerItem(scrapy.Item):
    title = scrapy.Field()
    info = scrapy.Field()
    photos = scrapy.Field()
    ad_id = scrapy.Field()

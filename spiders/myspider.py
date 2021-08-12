# -*- coding: utf-8 -*-
import scrapy
from stackoverflow.items import StackoverflowItem


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://stackoverflow.com/questions?tab=Bounties']

    def parse(self, response):
        SET_SELECTOR = '.question-summary'
        for line in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'h3 ::text'
            item = StackoverflowItem()

            item['question'] = line.css(NAME_SELECTOR).extract_first()
            yield item
            pass

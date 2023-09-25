import re
from urllib.parse import urljoin

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        peps = response.css('#numerical-index tbody tr')

        for pep in peps:
            link = pep.css('a::attr(href)').get()
            yield response.follow(
                urljoin(self.start_urls[0], link), callback=self.parse_pep
            )

    def parse_pep(self, response):
        pattern = r'PEP (?P<number>\d+) – (?P<name>.*)'

        number, name = re.search(
            pattern, response.css('h1.page-title::text').get()
        ).groups()

        yield PepParseItem({
            'number': number,
            'name': name,
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get()
        })

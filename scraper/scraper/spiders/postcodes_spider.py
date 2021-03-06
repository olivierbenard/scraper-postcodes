import re
import bs4
import scrapy
from bs4 import BeautifulSoup


class QuotesSpider(scrapy.Spider):

    # scrapy crawl quotes
    name = "postcodes"

    def start_requests(self):

        base = "http://germany.postcode.info/"

        # collection of all postcodes
        file = open('../results/postcodes.list', 'r')
        postcodes = (line.replace('\n', '') for line in file.readlines())
        file.close()

        # defintiion of urls to scrap
        urls = [f'{base}p/{postcode}' for postcode in postcodes]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        def parse_page(soup):
            content = soup.find_all("div", {'class': 'cnt'})[0]
            in_block = False
            i_line = 0
            lines = []
            line = []
            while True:
                try:
                    content = content.next_element
                    if isinstance(content, bs4.element.Tag):
                        if content.name == 'strong' and not in_block:
                            in_block = True
                        if content.name == 'br':
                            if line != []:
                                lines.append(line)
                            line = []
                            in_block = False
                            i_line = 0
                    if isinstance(content, bs4.element.NavigableString) and in_block:
                        i_line += 1
                        if i_line == 1: # Ort
                            line.append(content.strip())
                        if i_line == 2: # Plz (5-digit postcode)
                            line.append(content.strip().replace(',', '').zfill(5))
                        if i_line == 3: # Lander
                            line.append(content.strip())
                        if i_line == 4: # Kreise + GPS Lat, Long
                            matched = re.findall(r'^,([^,]*)[^\d]*(\d{1,}.?\d{0,})[^\d]*(\d{1,}.?\d{0,})', content)
                            temp = [line.append(item.strip()) for item in matched[0]]
                except:
                    break
            return lines

        page = response.url
        html = response.body
        soup = BeautifulSoup(html, 'html.parser')
        with open('../results/postcodes.de', 'a') as file:
            data = parse_page(soup)
            file.write('\n'.join(','.join(item) for item in data) + '\n')
        file.close()

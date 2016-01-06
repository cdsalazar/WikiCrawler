from bs4 import BeautifulSoup
import re
import scrapy
from wikiCrawler.items import WikicrawlerItem

class WikiSpider(scrapy.Spider):
    name = "wiki"
    allowed_domains = ["wikipedia.org"]
    start_urls = []
    search_type = open('./domains.txt', 'r').readline()
    dirname = ''
    ALL_STRING = ''

    def __init__(self):
        for line in open('./domains.txt', 'r').readlines():
            if(('https:' not in line) and ('DOMAIN' not in line) and ('QA' not in line)):
                self.dirname = line
            elif(('DOMAIN' in line) or ('QA' in line)):
                continue
            else:
                self.start_urls.append(line.strip())

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        name = soup.title.string
        name = name.split(' - ')[0]
        
        html_text = re.sub('<[^<]+?>', '', response.body)
        edited_text = html_text
        if (len(html_text.split('body{behavior:url("/w/static/1.27.0-wmf.6/skins/Vector/csshover.min.htc")}')) == 2):
            edited_text = html_text.split('body{behavior:url("/w/static/1.27.0-wmf.6/skins/Vector/csshover.min.htc")}')[1]
        elif (len(html_text.split('body{behavior:url("/w/static/1.27.0-wmf.5/skins/Vector/csshover.min.htc")}')) == 2):
            edited_text = html_text.split('body{behavior:url("/w/static/1.27.0-wmf.5/skins/Vector/csshover.min.htc")}')[1]
        elif(len(html_text.split('body{behavior:url("/w/static/1.27.0-wmf.4/skins/Vector/csshover.min.htc")}')) == 2):
            edited_text = html_text.split('body{behavior:url("/w/static/1.27.0-wmf.4/skins/Vector/csshover.min.htc")}')[1]
        elif(len(html_text.split('body{behavior:url("/w/static/1.27.0-wmf.3/skins/Vector/csshover.min.htc")}')) == 2):
            edited_text = html_text.split('body{behavior:url("/w/static/1.27.0-wmf.3/skins/Vector/csshover.min.htc")}')[1]
        elif(len(html_text.split('body{behavior:url("/w/static/1.27.0-wmf.2/skins/Vector/csshover.min.htc")}')) == 2):
            edited_text = html_text.split('body{behavior:url("/w/static/1.27.0-wmf.2/skins/Vector/csshover.min.htc")}')[1]

        name = re.sub('/', ' ', name)
        edited_text = edited_text.split('Mobile view')[0]
        if(self.search_type.strip() == 'DOMAIN'):
            filename = self.dirname.strip() + '/' + name + '.txt'
            with open(filename, 'wb') as f:
                f.write(edited_text)
        elif(self.search_type.strip() == 'QA'):
            filename = 'pages/' + name + '.txt'
            with open(filename, 'wb') as f:
                f.write(edited_text)

        # for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
        #     url = response.urljoin(href.extract())
        #     yield scrapy.Request(url, callback=self.parse_dir_contents)

        for sel in response.xpath('//ul/li'):
            if(len(sel.xpath('a/@href').extract()) == 2):
                link = sel.xpath('a/@href').extract()[0]
                if(len(link)>0):
                    if('/wiki/' in link):
                        url = 'https://en.wikipedia.org' + link
                        yield scrapy.Request(url, callback=self.parse)


    def parse_dir_contents(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        name = soup.title.string
        name = name.split(' - ')[0]
        
        html_text = re.sub('<[^<]+?>', '', response.body)
        # p = re.compile(r'<.*?>')
        # html_text = p.sub('', response.body)
        edited_text = html_text
        if (len(html_text.split('body{behavior:url("/w/static/1.27.0-wmf.6/skins/Vector/csshover.min.htc")}')) == 2):
            edited_text = html_text.split('body{behavior:url("/w/static/1.27.0-wmf.6/skins/Vector/csshover.min.htc")}')[1]
        elif (len(html_text.split('body{behavior:url("/w/static/1.27.0-wmf.5/skins/Vector/csshover.min.htc")}')) == 2):
            edited_text = html_text.split('body{behavior:url("/w/static/1.27.0-wmf.5/skins/Vector/csshover.min.htc")}')[1]
        elif(len(html_text.split('body{behavior:url("/w/static/1.27.0-wmf.4/skins/Vector/csshover.min.htc")}')) == 2):
            edited_text = html_text.split('body{behavior:url("/w/static/1.27.0-wmf.4/skins/Vector/csshover.min.htc")}')[1]
        elif(len(html_text.split('body{behavior:url("/w/static/1.27.0-wmf.3/skins/Vector/csshover.min.htc")}')) == 2):
            edited_text = html_text.split('body{behavior:url("/w/static/1.27.0-wmf.3/skins/Vector/csshover.min.htc")}')[1]
        elif(len(html_text.split('body{behavior:url("/w/static/1.27.0-wmf.2/skins/Vector/csshover.min.htc")}')) == 2):
            edited_text = html_text.split('body{behavior:url("/w/static/1.27.0-wmf.2/skins/Vector/csshover.min.htc")}')[1]

        name = re.sub('/', ' ', name)
        edited_text = edited_text.split('Mobile view')[0]
        if(self.search_type.strip() == 'DOMAIN'):
            filename = self.dirname.strip() + '/' + name + '.txt'
            with open(filename, 'wb') as f:
                f.write(edited_text)
        elif(self.search_type.strip() == 'QA'):
            filename = 'pages/' + name + '.txt'
            with open(filename, 'wb') as f:
                f.write(edited_text)

        # for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
        #     url = response.urljoin(href.extract())
        #     yield scrapy.Request(url, callback=self.parse_dir_contents)

        for sel in response.xpath('//ul/li'):
            if(len(sel.xpath('a/@href').extract()) == 2):
                link = sel.xpath('a/@href').extract()[0]
                if(len(link)>0):
                    if('/wiki/' in link):
                        url = 'https://en.wikipedia.org' + link
                        yield scrapy.Request(url, callback=self.parse)



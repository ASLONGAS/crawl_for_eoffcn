from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
import urllib

from dirbot.items import Website


class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["eoffcn.com"]
    start_urls = [
        'http://www.eoffcn.com/stixz/moniti/xingce/66162.html',
    ]
    count = 0

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        # sites = response.css('#site-list-content > div.site-item > div.title-and-desc')
        # items = []
        #
        # for site in sites:
        #     item = Website()
        #     item['name'] = site.css(
        #         'a > div.site-title::text').extract_first().strip()
        #     item['url'] = site.xpath(
        #         'a/@href').extract_first().strip()
        #     item['description'] = site.css(
        #         'div.site-descr::text').extract_first().strip()
        #     items.append(item)

        item=Website()
        item['imgUrls']=response.xpath('//div[@class="main_l_cont"]/center/img/@src').extract()
        for imgUrl in item['imgUrls']:
            urllib.urlretrieve(imgUrl.strip(), 'pictures\\' + str(self.count) + '.png')
            self.count=self.count+1
            print imgUrl


        item['nextUrl']=response.xpath('//div[@id="pages"]/a[@class="a1"][2]/@href').extract()
        print item['nextUrl']
        req = Request(url=item['nextUrl'][0], callback=self.parse)
        yield req
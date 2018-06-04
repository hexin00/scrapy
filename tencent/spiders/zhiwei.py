import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencent.items import TencentItem

class ZhiweiSpider(CrawlSpider):
    name = 'zhiwei'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=#a0']

    
    rules = (
        Rule(LinkExtractor(allow='start=\d+'), callback='parse_item', follow=True),
    )
    
    def parse_item(self, response):
        print('-'*50)
        td = response.xpath("//tr[@class='even']")
        td+=(response.xpath("//tr[@class='odd']"))
        for each in td:
            items = TencentItem()
            gangwei = each.xpath("./td[1]/a/text()").extract()[0]
            zhiwei = each.xpath("./td[2]/text()").extract()[0]
            renshu = each.xpath("./td[3]/text()").extract()[0]
            didian = each.xpath("./td[4]/text()").extract()[0]
            shijian = each.xpath("./td[5]/text()").extract()[0]
            items['gangwei'] = gangwei
            items['zhiwei'] = zhiwei
            items['renshu'] = renshu
            items['didian'] = didian
            items['shijian'] = shijian
            yield items

    


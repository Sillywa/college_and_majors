# -*- coding: utf-8 -*-
import scrapy
from graduate_info.items import GraduateInfoItem


class GraduateSpiderSpider(scrapy.Spider):
    name = "graduate_spider"
    allowed_domains = ["yz.chsi.com.cn"]
    start_urls = ['https://yz.chsi.com.cn/sch']
    base_url = 'https://yz.chsi.com.cn'

    def parse(self, response):
        # 从文档中开始找
        college_list = response.xpath("//table[@class='ch-table']/tbody/tr")
        # 循环
        for item in college_list:

            college = GraduateInfoItem()
            college['name'] = item.xpath("./td[1]/a/text()").extract_first().strip()

            college["place"] = item.xpath("./td[2]/text()").extract_first()

            college["attachment"] = item.xpath("./td[3]/text()").extract_first()

            college["has_graduate_institute"] = item.xpath("./td[4]/i/text()").extract_first()
            if college["has_graduate_institute"]:
                college["has_graduate_institute"] = 1
            else:
                college["has_graduate_institute"] = 0

            college["is_self_score"] = item.xpath("./td[5]/i/text()").extract_first()
            if college["is_self_score"]:
                college["is_self_score"] = 1
            else:
                college["is_self_score"] = 0

            link = item.xpath("./td[6]/a/@href").extract()
            college["announcement"] = self.base_url + link[0]

            link = item.xpath("./td[7]/a/@href").extract()
            college["regulations"] = self.base_url + link[0]

            link = item.xpath("./td[8]/a/@href").extract()
            college["adjustment"] = self.base_url + link[0]

            yield college

        # 取得 a 标签的 href 属性，解析下一页，取得后页的 xpath
        next_link = response.xpath("//ul[@class='ch-page clearfix']//li[@class='lip lip-input-box clearfix lip-last']/preceding-sibling::li[1]/a/@href").extract()
        print("---------------")
        print(next_link)
        print("-------------")
        if next_link:
            next_link = next_link[0]
            # 送到下载器下载下一页，下载之后执行回调进行解析
            yield scrapy.Request('https://yz.chsi.com.cn' + next_link, callback=self.parse)

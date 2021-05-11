# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from scrapy import Request


# 获得所有的专业信息
from graduate_info.items import MajorSchool


class MajorSchoolSpider(scrapy.Spider):
    name = "major_school"
    allowed_domains = ["yz.chsi.com.cn"]
    domain = "https://yz.chsi.com.cn"

    def start_requests(self):
        print("----------------")
        print("爬虫开始")
        print("----------------")
        df = pd.read_csv("lastCategory.csv")

        code_list = df['code'].tolist()
        link_list = df["link"].tolist()
        for (code, link) in zip(code_list, link_list):
            link = self.domain + link
            yield Request(link, callback=self.parse, meta={"code": code})

    def parse(self, response):
        # soup = BeautifulSoup(response.body, "html.parser")
        #
        # ul = soup.find_all("ul", class_="clearfix")
        # text_list = ul.find_all("li").get("title")
        parent_code = response.meta["code"]

        text_list = response.xpath("//ul[@class='clearfix']/li/@title").extract()
        ms = MajorSchool()

        ms["parent_code"] = parent_code
        ms["college"] = text_list
        yield ms
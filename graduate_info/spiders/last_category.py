# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from scrapy import FormRequest
from bs4 import BeautifulSoup

from graduate_info.items import MajorDetail

# 获得最后一级菜单，即专业
class LastCategorySpider(scrapy.Spider):
    name = "last_category"
    allowed_domains = ["yz.chsi.com.cn"]
    start_urls = 'https://yz.chsi.com.cn/zyk/specialityCategory.do'
    domain = "https://yz.chsi.com.cn"
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

    def start_requests(self):
        print("----------------")
        print("爬虫开始")
        print("----------------")
        df = pd.read_csv("thirdCategory.csv")
        id_list = df['id'].tolist()
        for id in id_list:
            form_data = {
                "method": "subCategoryXk",
                "key": str(id)
            }
            yield FormRequest(self.start_urls,
                              formdata=form_data,
                              headers=self.headers,
                              meta= {"id": id})

    def parse(self, response):
        data = response.body
        soup = BeautifulSoup(data, "html.parser")
        parent_id = response.meta["id"]
        trs = soup.find_all("tr")
        for (index, tr) in enumerate(trs):
            if index != 0:
                td_list = tr.find_all("td")
                name = td_list[0].find("a").get_text().strip()
                code = td_list[1].get_text().strip()
                link = td_list[2].find("a").get("href")
                result = {
                    "code": code,
                    "name": name,
                    "parent_id": parent_id,
                    "link": link
                }
                detail = MajorDetail()
                detail["code"] = code
                detail["name"] = name
                detail["link"] = link
                detail["parent_id"] = parent_id

                yield detail

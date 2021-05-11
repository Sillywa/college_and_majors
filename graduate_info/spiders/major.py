# -*- coding: utf-8 -*-
import scrapy
from graduate_info.items import MajorItem
from graduate_info.items import MajorDetail
from scrapy import FormRequest
from bs4 import BeautifulSoup


class MajorSpider(scrapy.Spider):
    name = "major"
    allowed_domains = ["https://yz.chsi.com.cn/"]
    start_urls = 'https://yz.chsi.com.cn/zyk/specialityCategory.do'
    domain = "https://yz.chsi.com.cn"
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    # top 级菜单
    top_list = []
    # 二级菜单
    sub_list = []
    # 三级菜单
    third_list = []
    # 四级菜单
    last_list = []
    # 每个专业的开设院校

    def start_requests(self):
        print("----------------")
        print("爬虫开始")
        print("----------------")
        form_data = {
            "method": "topCategory"
        }
        yield FormRequest(self.start_urls,
                          formdata=form_data,
                          headers=self.headers)

    def parse(self, response):
        print("----------------")
        print("主菜单爬虫开始")
        print("----------------")
        data = response.body
        soup = BeautifulSoup(data, "html.parser")
        # print(soup.prettify())
        for li in soup.find_all("li"):
            id = li.get("id")
            name = li.get_text().strip()[:-1]

            # major = MajorItem()
            # major["id"] = id
            # major["name"] = name
            # major["parent_id"] = 0
            # print(name)
            self.top_list.append({
                "id": id,
                "name": name
            })
            form_data = {
                "method": "subCategoryMl",
                "key": id
            }

            yield FormRequest(self.start_urls,
                              formdata=form_data,
                              callback=self.parse_sub,
                              headers=self.headers,
                              meta={"id": id},
                              dont_filter=True)

    def parse_sub(self, response):
        print("----------------")
        print("二级菜单爬虫开始")
        print("----------------")
        data = response.body
        soup = BeautifulSoup(data, "html.parser")
        # print(response.meta)
        parent_id = response.meta["id"]
        for li in soup.find_all("li"):
            id = li.get("id")
            name = li.get_text().strip()[:-1]

            # major = MajorItem()
            # major["id"] = id
            # major["name"] = name
            # major["parent_id"] = parent_id
            # print(name)
            self.sub_list.append({
                "id": id,
                "parent_id": parent_id,
                "name": name
            })

            form_data = {
                "method": "subCategoryMl",
                "key": id
            }
            # yield major

            yield FormRequest(self.start_urls,
                              formdata=form_data,
                              callback=self.parse_third,
                              headers=self.headers,
                              meta={"id": id},
                              dont_filter=True)

    def parse_third(self, response):
        print("----------------")
        print("三级菜单爬虫开始")
        print("----------------")
        data = response.body
        soup = BeautifulSoup(data, "html.parser")
        parent_id = response.meta["id"]
        for li in soup.find_all("li"):
            id = li.get("id")
            name = li.get_text().strip()[:-1]

            # major = MajorItem()
            # major["id"] = id
            # major["name"] = name
            # major["parent_id"] = parent_id
            # print(name)
            self.third_list.append({
                "id": id,
                "parent_id": parent_id,
                "name": name
            })
            form_data = {
                "method": "subCategoryMl",
                "key": id
            }
            yield FormRequest(self.start_urls,
                              formdata=form_data,
                              callback=self.parse_last,
                              headers=self.headers,
                              meta={"id": id},
                              dont_filter=True)

    # def parse_last(self, response):
    #     print("----------------")
    #     print("最后一级菜单爬虫开始")
    #     print("----------------")
    #     data = response.body
    #     soup = BeautifulSoup(data, "html.parser")
    #     parent_id = response.meta["id"]
    #     for (index, tr) in enumerate(soup.find_all("tr")):
    #         if index != 0:
    #             td_list = tr.find_all("td")
    #             name = td_list[0].find("a").get_text().strip()
    #             code = td_list[1].get_text().strip()
    #             link = self.domain + td_list[2].get("href")
    #
                # detail = MajorDetail()
                # detail["code"] = code
                # detail["name"] = name
                # detail["link"] = link
                # detail["parent_id"] = parent_id
    #
    #             result = {
    #                 "code": code,
    #                 "name": name,
    #                 "parent_id": parent_id,
    #                 "link": link
    #             }
    #             print(result)
    #             self.last_list.append(result)
    #
    #             yield detail

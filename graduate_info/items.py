# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GraduateInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 院校名称
    name = scrapy.Field()
    # 地点
    place = scrapy.Field()
    # 院校隶属
    attachment = scrapy.Field()
    # 是否有研究生院
    has_graduate_institute = scrapy.Field()
    # 是否自主划线
    is_self_score = scrapy.Field()
    # 招生公告
    announcement = scrapy.Field()
    # 招生简章
    regulations = scrapy.Field()
    # 调剂
    adjustment = scrapy.Field()


class MajorItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    parent_id = scrapy.Field()


class MajorDetail(scrapy.Item):
    code = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
    parent_id = scrapy.Field()


class MajorSchool(scrapy.Item):
    parent_code = scrapy.Field()
    college = scrapy.Field()

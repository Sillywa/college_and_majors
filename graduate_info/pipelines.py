# -*- coding: utf-8 -*-
import pandas as pd
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GraduateInfoPipeline(object):
    columns = []
    value_list = []

    def __init__(self):
        print("init")

    def process_item(self, item, spider):
        value_list = list(item.values())
        self.columns = list(item.keys())
        self.value_list.append(value_list)
        return item

    def close_spider(self, spider):
        df = pd.DataFrame(self.value_list, columns=self.columns)
        df.to_csv("graduateMajorSchool.csv", index=False)
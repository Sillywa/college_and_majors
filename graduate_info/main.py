from scrapy import cmdline
cmdline.execute("scrapy crawl graduate_spider -o college.csv -t csv".split())
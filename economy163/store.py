#encoding: utf-8
from pymongo import MongoClient
from scrapy.conf import settings
client = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
News_163DB = client[settings['MONGODB_DB']]
collect_163 = News_163DB[settings['MONGODB_COLLECTION']]
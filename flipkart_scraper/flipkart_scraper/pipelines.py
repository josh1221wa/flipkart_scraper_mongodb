# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import hashlib
from scrapy.exceptions import DropItem


class FlipkartScraperPipeline:
    COLLECTION_NAME = 'phones'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        item_id = self.compute_item_id(item)
        if item['name'] is not None:
            if self.db[self.COLLECTION_NAME].find_one({'_id': item_id}):
                raise DropItem(f"Duplicate item found: {item}")
            else:
                self.db[self.COLLECTION_NAME].insert_one(
                    ItemAdapter(item).asdict())
                return item

    def compute_item_id(self, item):
        return hashlib.sha256(item['url'].encode("utf-8")).hexdigest()
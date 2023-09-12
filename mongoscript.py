from pymongo import MongoCliennt

client = MongoClient("mongodb+srv://AmazoneData:AmazoneData@scrapingfromamazone.qhi9me9.mongodb.net/")

db = client.scrapy

collection = db.test_collection
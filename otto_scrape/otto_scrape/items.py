# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
    Url = scrapy.Field()
    Company_Name = scrapy.Field()
    Product_Name = scrapy.Field()
    Address = scrapy.Field()
    Phone_Number = scrapy.Field()
    Mail = scrapy.Field()

from scrapy.item import Item, Field


class Website(Item):
    imgUrls=Field()
    nextUrl=Field()

from scrapy.exceptions import DropItem
import json
import codecs


class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    def __init__(self):
        self.file = codecs.open('url.txt', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        # print line
        self.file.write(line.decode("unicode_escape"))
        return item

        # put all words in lowercase
    # words_to_filter = ['politics', 'religion']
    #
    # def process_item(self, item, spider):
    #     for word in self.words_to_filter:
    #         if word in item['description'].lower():
    #             raise DropItem("Contains forbidden word: %s" % word)
    #     else:
    #         return item

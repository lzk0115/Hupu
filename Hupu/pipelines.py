# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re


class TextPipeline(object):
    def __init__(self):
        self.re_blo = re.compile(r'<blockquote>.*</blockquote>')
        self.re_sma = re.compile(r'<small .*</small>')
        self.re_tag = re.compile(r'<.*?>')
        self.fout = open('text', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if item['text']:
            text = item['text']
            temp = text.replace('\n', '')
            temp = re.sub(self.re_blo, '', temp)
            temp = re.sub(self.re_sma, '', temp)
            temp = re.sub(self.re_tag, '', temp)
            item['text'] = temp
            self.fout.write(temp + '\n')
        return item



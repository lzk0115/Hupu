# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

re_blo = re.compile(r'<blockquote>.*</blockquote>')
re_sma = re.compile(r'<small .*</small>')
re_img = re.compile(r'<img.*>')
re_div = re.compile(r'<.*div.*>')
re_br = re.compile(r'<br>|</br>')
re_p = re.compile(r'<p>|</p>')


class TextPipeline(object):
    def __init__(self):
        self.fout = open('text', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if item['text']:
            text = item['text']
            temp = re.sub(re_blo, '', text)
            temp = re.sub(re_sma, '', temp)
            temp = re.sub(re_div, '', temp)
            temp = re.sub(re_br, '', temp)
            temp = re.sub(re_p, '', temp)
            temp = re.sub(re_img, '', temp)
            temp = temp.replace('\n', '')
            item['text'] = temp
            self.fout.write(temp + '\n')
        return item



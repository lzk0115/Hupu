# _*_ coding:utf-8 _*_
import jieba
import codecs
import re
from collections import Counter


# 读取文件
def readfile(filepath):
    fp = codecs.open(filepath, "r", encoding="utf-8")
    content = fp.read()
    fp.close()
    return content


# 保存文件
def savefile(savepath, content):
    fp = codecs.open(savepath, "w", encoding='utf-8')
    fp.write(content)
    fp.close()


# 按行加载文件
def readwordslist(filepath):
    wordslist = readfile(filepath).splitlines()
    return wordslist


# 去除输入文本中的网址数据
# 顺便把换行符和空格符也去了
def filter_url_tag(urlstring):
    results = re.compile(r'[a-zA-z]+://[^\s]*', re.S)
    return results.sub("", urlstring).replace('\n', '').replace(' ', '').replace(u'\u2605', '').replace('10', '')


inputwords_file = "text"
stopwords_file = "stopwords.dat"

cutwordslist = []
stopwords = readwordslist(stopwords_file)
stopwords.append('说')
count = 0
for url_line in readwordslist(inputwords_file):
    count += 1
    line = filter_url_tag(url_line)
    cutwordslist += [word for word in jieba.cut(line, cut_all=True) if word not in stopwords]
    if count/2000 == 0:
        print(count)
cutwords = dict(Counter(cutwordslist))

outputwords = {}
for k, v in cutwords.items():
    if k in outputwords.keys():
        outputwords[k] += v
    else:
        outputwords[k] = v

outputwords_sorted = sorted(outputwords.items(), key=lambda x: x[1], reverse=True)

fileObject = open('sampleList.txt', 'w')
for ip in outputwords_sorted:
    fileObject.write(str(ip[0]))
    fileObject.write('\n')
fileObject.close()

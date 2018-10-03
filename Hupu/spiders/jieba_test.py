import requests
import logging
import jieba
#
# url = "https://bbs.hupu.com/bxj/highlights"
# html = requests.get(url)
logging.basicConfig(filename='jieba.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d')
# # logging.debug(html.content)
# print(html.text)
string = "他到底经历了啥！感觉说话的时候都要哭了一样"
seg_list = jieba.cut(string)
logging.info(' / '.join(seg_list))
import re,logging
from scrapy.selector import Selector
with open('hupu_page/hupu-1.html', encoding='utf-8')  as fin:
    a = fin.read()

re_blo = re.compile(r'<blockquote>.*</blockquote>')
re_sma = re.compile(r'<small .*</small>')
re_img= re.compile(r'<img.*>')
re_div = re.compile(r'<.*div.*>')
re_br = re.compile(r'<br>|</br>')
re_p = re.compile(r'<p>|</p>')
sel = Selector(text=a)
elements = sel.css('div.case')
logging.basicConfig(filename='app1.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d')
for e in elements:
    b = e.extract()
    a1 = re.sub(re_blo, '', b)
    a2 = re.sub(re_sma, '', a1)
    a3 = re.sub(re_div, '', a2)
    a4 = re.sub(re_br, '', a3)
    a5 = re.sub(re_p, '', a4)
    a6 = re.sub(re_img, '', a5)
    a7 = a6.replace('\n', '')
    logging.info(a7)

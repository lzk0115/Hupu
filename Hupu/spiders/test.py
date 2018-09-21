import requests
import logging
import
url = "https://bbs.hupu.com/bxj/highlights"
html = requests.get(url)
logging.basicConfig(filename='app.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d')
# logging.debug(html.content)
print(html.text)
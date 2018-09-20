import requests 
import logging
url = "https://bbs.hupu.com/bxj/highlights"
html = requests.get(url)
logging.basicConfig(
        fileName = 'app.log',
        level = logging.ERROR
        )
logging.info(html.content)

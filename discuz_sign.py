# 需要提前执行：(报错请用pip3 install xxxxxx)
# pip install requests
# pip install bs4
#--------------------------------------
#此处修改成你的配置
url='https://你的论坛网址/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1'
headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
  "Accept-Language": "zh-CN,zh;q=0.9",
  "Accept-Encoding": "gzip, deflate, br",
  "Connection": "keep-alive",
  "Cookie" : "xxxx_1234_saltkey=xxxxxx; xxxx_1234_auth=xxxxxxxxxxxxxxxxxxxx",
  "Host": "你的论坛网址",
  "Referer": "https://你的论坛网址/plugin.php?id=dsu_paulsign:sign"}
form_data = {
    "formhash": "cb4f0a01",
    "qdxq": "kx",
    "todaysay": "今天很开心！",
}
#以上请修改成自己的配置
#--------------------------------------

import re
import requests
from bs4 import BeautifulSoup
import html

r= requests.post(url, data=form_data, headers=headers)

r.encoding="UTF-8"
soup = BeautifulSoup(r.text, 'xml')
html_text = html.unescape(soup.text)
soup1 = BeautifulSoup(html_text, 'html.parser')
div = soup1.find('div', class_='c')
text = div.get_text()
print(text)






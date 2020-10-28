# -*- codeing = utf-8 -*-
# @Time     : 10/26 0:58
# @Author   : River
# @File     : test.py
# @Software : PyCharm

import urllib.request
from bs4 import BeautifulSoup

reponse = urllib.request.urlopen('https://www.baidu.com/')

html = reponse.read().decode('utf-8')
# print(reponse.read().decode('utf-8'))

bs = BeautifulSoup(html,"html.parser")

t_list = bs.find_all(id="head")
for item in t_list:
    print("%s\n\n" % item)
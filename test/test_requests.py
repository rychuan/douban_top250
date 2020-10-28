# -*- coding: utf-8 -*-
# @Time     : 10/28 9:39
# @Author   : River
# @File     : test_requests.py
# @Software : PyCharm

import re
import requests

baseUrl = "https://www.weibo.com/"

head = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51"
    }

response = requests.get(baseUrl,headers=head)

# print(response.text)
# print(type(response.text))
print(response.request.headers)
print(response.content)
# -*- codeing = utf-8 -*-
# @Time     : 10/19 15:47
# @Author   : River
# @File     : douban.py
# @Software : PyCharm

import pandas as pd
import re
import requests
from lxml import etree

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 Edg/81.0.416.68'
    }

list_whole = []
page = 1
for i in range(0,226,25):
    url = 'https://movie`.douban.com/top250?start={}&filter='.format(i)
    print(url)
    res = requests.get(url=url,headers=headers)
    tree = etree.HTML(res.text)
    # 标题
    list00 = tree.xpath('//div[@class="article"]//ol[@class="grid_view"]/li//a/span[1]/text()')
    list01 = tree.xpath('//div[@class="article"]//ol[@class="grid_view"]/li//a/span[2]/text()')
    # 评分
    list1 = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[2]/text()')
    # 评价人数
    list2 = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[4]/text()')
    # 一句话概述
    list3 = []
    li_list = tree.xpath('//*[@id="content"]/div/div[1]/ol/li')
    for li in li_list:
        content = li.xpath('div//p[@class="quote"]/span/text()')
        if content != []:
            list3.append(content[0])
        else:
            list3.append(' ')
    # 0
    list40 = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[1]/text()[1]')
    list41 = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[1]/text()[2]')
    # 电影详情链接
    list5 = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/@href')
    # 图片链接
    list6 = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[1]/a/img/@src')
    for i5,i6,i00,i01,i1,i2,i3,i40,i41 in zip(list5,list6,list00,list01,list1,list2,list3,list40,list41):
        i01 = i01.replace("\xa0/\xa0",'')
        i2 = i2.replace("人评价",'')
        i3 = i3.replace(' ','')
        i40 = "".join(i40.split())
        i41 = "".join(i41.split())
        whole_dict = {}
        whole_dict['id'] = page
        whole_dict['电影详情链接'] = i5
        whole_dict['图片链接'] = i6
        whole_dict['标题'] = i00
        whole_dict['标题2'] = i01
        whole_dict['评分'] = i1
        whole_dict['评价人数'] = i2
        whole_dict['一句话概述'] = i3
        whole_dict['其他信息'] = i40+i41
        # print(i4)
        list_whole.append(whole_dict)
        page += 1
    # print(list_whole)

tets = pd.DataFrame(data=list_whole)
tets.to_csv('./豆瓣电影.csv',mode='w+',index=False)

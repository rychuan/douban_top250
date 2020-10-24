# -*- codeing = utf-8 -*-
# @Time     : 10/19 22:31
# @Author   : River
# @File     : spider.py
# @Software : PyCharm

from bs4 import BeautifulSoup
import re
import urllib.request , urllib.error
import xlwt
import sqlite3
import ssl

# ssl._create_default_https_context = ssl._create_unverified_context



def main():
    baseUrl = "https://movie.douban.com/top250?start="
    #1. 爬取网页
    # datalist = getData(baseUrl)
    #2. 解析数据
    savePath = ".\\豆瓣电影top250.xls"
    # 3. 保存数据
    # saveData(savePath)
    # askUrl("https://movie.douban.com/top250?start=0")
    askUrl("https://www.baidu.com")


#爬取网页
def getData(baseUrl):
    dataList = []
    for i in range(0,10):       #调用获取页面信息的函数，10次
        url = baseUrl + str(i*25)
        html = askUrl(url)      #保存获取到的网页源码

        # 2. 解析数据

    return dataList

#得到指定一个URL的网页内容
def askUrl(url):
    head = {       #模拟浏览器头部信息，向服务器发送消息
        #windows
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43"

        #MacBook
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15"
    }
    # 用户代理，表示告诉服务器，我们是什么类型的机器（本质上是告诉浏览器我们可以接收什么水平的文件内容）

    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)

    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html

#3. 保存数据
def saveData(savepath  ):
    print("save......")


if __name__ == '__main__':
    main()
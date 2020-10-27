# -*- codeing = utf-8 -*-
# @Time     : 10/19 23:03
# @Author   : River
# @File     : testBs4.py
# @Software : PyCharm

from bs4 import BeautifulSoup
import urllib.request , urllib.error
import re

'''
- Tag
- NavigableString
- BeautifulSoup
- Comment
'''
#得到指定一个URL的网页内容
def askUrl(url):
    head = {       #模拟浏览器头部信息，向服务器发送消息
        #windows
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43"

        #MacBook
        # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15"
    }
    # 用户代理，表示告诉服务器，我们是什么类型的机器（本质上是告诉浏览器我们可以接收什么水平的文件内容）

    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
        # print("......")

    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html

def getData(baseUrl):
    dataList = []
    for i in range(0,10):       #调用获取页面信息的函数，10次
        url = baseUrl + str(i*25)
        html = askUrl(url)      #保存获取到的网页源码

        # 2. 解析数据
        dataList.append(html)
        # print("已获取第%d页"%(i+1))

    return dataList

def main():
    baseUrl = "https://movie.douban.com/top250?start=0"
    #1. 爬取网页
    dataList = getData(baseUrl)
    # print(dataList[0])
    #2. 解析数据
    savePath = ".\\豆瓣电影top250.xls"
    # 3. 保存数据
    # saveData(savePath)
    # askUrl("https://movie.douban.com/top250?start=0")
    # askUrl("https://www.baidu.com")

    # file = dataList[0]
    html = dataList[0]
    bs = BeautifulSoup(html,"html.parser")

    #文档搜索
    #-------------------------------------------------
    #（1）find_all()
    #字符串过滤：会查找与字符串完全匹配的内容
    # t_list = bs.find_all("a")

    #-------------------------------------------------
    #（2）search()
    #正则表达式搜索：使用search()方法来匹配内容
    # t_list = bs.find_all(re.compile("a"))

    #-------------------------------------------------
    #(3)函数
    #方法：传入一个函数（方法），根据函数的要求来搜索
    # def name_is_exists(tag):
    #     return tag.has_attr("name")
    #
    # t_list = bs.find_all(name_is_exists)
    #
    # for item in t_list:
    #     print("%s\n\n"%item)

    #-------------------------------------------------
    #2. kwargs  参数
    # t_list = bs.find_all(id = "db-global-nav")
    # t_list = bs.find_all(class_ = True)
    # t_list = bs.find_all(href = "https://img3.doubanio.com/f/shire/859dba5cddc7ed1435808cf5a8ddde5792cd6e0c/css/douban.css")

    #3. text参数
    # t_list = bs.find_all(text = "希望让人自由。")
    # t_list = bs.find_all(text = ["风华绝代。","一部美国近现代史。","怪蜀黍和小萝莉不得不说的故事。"])
    # t_list = bs.find_all(text = re.compile("\d")) #应用正则表达式来查找包含特定文本的内容（标签里的字符串）
    # for item in t_list:
    #     print("%s\n\n"%item)


    #4. limit参数
    # t_list = bs.find_all("a",limit=3)

    #css选择器

    # t_list = bs.select("title") #通过标签来查找
    # t_list = bs.select(".item") #通过类名来查找
    # t_list = bs.select("#db-global-nav")   #通过id来查找
    # t_list = bs.select("a[class='movieannual']")    #通过属性来查找
    # t_list = bs.select("div > div") #通过子便签来查找
    # t_list = bs.select(".mnav ~ .bri")
    # print(t_list[0].get_text())

    # for item in t_list:
    #     print("%s\n\n"%item)




if __name__ == '__main__':
    main()
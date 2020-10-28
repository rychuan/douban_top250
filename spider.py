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

# ssl._create_default_https_context = ssl._create_unverified_context

def main():
    baseUrl = "https://movie.douban.com/top250?start="
    #1. 爬取网页
    dataList = getData(baseUrl)
    for i in dataList:
        print(i)
    #2. 解析数据
    savePath = ".\\豆瓣电影top250.xls"
    # 3. 保存数据
    # saveData(savePath)
    # askUrl("https://movie.douban.com/top250?start=0")
    # askUrl("https://www.baidu.com")

#影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')     #创建正则表达式对象，表示规则（字符串的模式）
#影片图片链接的规则
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)      #re.S忽略换行符，让换行符包含在字符中
findTitle = re.compile(r'<span class="title">(.*?)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
finInq = re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)


#爬取网页
def getData(baseUrl):
    dataList = []
    for i in range(0,1):       #调用获取页面信息的函数，10次
        url = baseUrl + str(i*25)
        html = askUrl(url)      #保存获取到的网页源码

        # 2. 逐一解析数据
        print("已获取第%d页"%(i+1))
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all("div",class_="item"):     #查找符合要求的字符串，形成列表
            # print(item)       #测试查看item全部信息
            data = []       #保存一部电影的所有信息
            item = str(item)

            link = re.findall(findLink,item)[0]     #re库用来通过正则表达式查找指定字符串
            data.append(link)
            # print(data)

            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)
            # print(data)

            titles = re.findall(findTitle,item)
            if(len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/","") #去掉无关的符号
            else:
                data.append(titles[0])
                data.append(' ')    #外国名留空

            rating = re.findall(findRating,item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)

            inq = re.findall(finInq,item)       #概述可能不存在
            if len(inq) != 0:
                inq = inq[0].replace("。","")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd,item)[0]             #re.findall()的返回值是什么？
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd) #去掉<br/>
            bd = re.sub('/'," ",bd) #替换/
            data.append(bd.strip()) #去掉前后的空格

            dataList.append(data)   #把处理好的一部电影信息放入dataList

    return dataList

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
        print("......")

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
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
    dataList = getData(baseUrl) #爬取结果
    # print(dataList[0])
    # print(len(dataList[0]))
    # for i in dataList:
    #     print(i)
    print("一共有%d条数据"%len(dataList))
    #2. 解析数据
    # savePath = ".\\豆瓣电影top250.xls"
    dbPath = ".\\movie.db"
    # 3. 保存数据
    # saveData(dataList,savePath)
    saveData2DB(dataList,dbPath)


    # askUrl("https://movie.douban.com/top250?start=0")
    # askUrl("https://www.baidu.com")

findLink = re.compile(r'<a href="(.*?)">')     #影片详情链接的规则，创建正则表达式对象，表示规则（字符串的模式）
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)  #影片图片链接的规则，re.S忽略换行符，让换行符包含在字符中
findTitle = re.compile(r'<span class="title">(.*?)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
finInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)  #找到影片的相关内容


#爬取网页
def getData(baseUrl):
    dataList = []
    for i in range(0,10):       #调用获取页面信息的函数，10次
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
            print(link)
            # data.append(link)
            # print(data)

            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)
            # print(data)

            titles = re.findall(findTitle,item)
            if(len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/","") #去掉无关的符号
                otitle = re.sub(r'\xa0', "", otitle)
                data.append(otitle)
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
            # bd = re.sub('/'," ",bd) #替换/
            bd = re.sub(r'\xa0', " ", bd)
            data.append(bd.strip()) #去掉前后的空格
            # 完成一部电影信息提取

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
def saveData(dataList,savePath):
    book = xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet = book.add_sheet("豆瓣电影Top250", cell_overwrite_ok = True)
    col = ("电影详情链接","图片链接","电影中文名","电影外国名","评分","评分数量","概况","相关信息") #表头

    for i in range(0,8):
        sheet.write(0,i,col[i])

    for i in range(0,len(dataList)):  #行数循环
        data = dataList[i]

        for j in range(0,len(data)):    #列数循环
            sheet.write(i+1,j,data[j])  #写入一行数据

    book.save(savePath) #保存数据
    print("数据已保存成功，请在根目录下查看%s"%savePath)

def saveData2DB(dataList,dbPath):
    # init_db(dbPath)
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()
    for data in dataList:
        for index in range(len(data)):
            if index ==4 or index == 5:
                continue
            data[index] = '"'+data[index]+'"'
        sql = '''
            insert into movie250 (
            info_link,pic_link,cname,ename,sorce,rated,instroduction,info)
            values(%s)
        '''%",".join(data)
        print(sql)
        cursor.execute(sql)
        conn.commit()

    cursor.close()
    conn.close()

def init_db(dbPath):
    sql = '''
        create table movie250 (
            id integer primary key autoincrement,
            info_link text,
            pic_link text,
            cname varchar ,
            ename varchar ,
            sorce numeric ,
            rated numeric ,
            instroduction text,
            info text
        );
    '''
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
    # init_db()
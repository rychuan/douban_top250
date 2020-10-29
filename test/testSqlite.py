# -*- codeing = utf-8 -*-
# @Time     : 10/29 16:45
# @Author   : River
# @File     : testSqlite.py
# @Software : PyCharm

import sqlite3

# conn = sqlite3.connect('test.db')   #打开或创建数据库文件
# print('成功打开数据库')
#
# c = conn.cursor()   #获取游标
#
# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
# '''
# c.execute(sql)  #执行sql语句
# conn.commit()   #提交数据库操作
# conn.close()    #关闭数据库连接
# print('建表成功')


#3. 插入数据
conn = sqlite3.connect('test.db')   #打开或创建数据库文件
print('成功打开数据库')
c = conn.cursor()   #获取游标
#
# sql1 = '''
#     insert into company (id,name,age,address,salary)
#     values (1,'张三',32,'成都',8000)
# '''
# sql2 = '''
#     insert into company (id,name,age,address,salary)
#     values (2,'李四',30,'重庆',15000)
# '''
#
# sql3 = '''
#     insert into company (id,name,age,address,salary)
#     values (3,'李四1',34,'重庆',16000)
# '''
#
# # c.execute(sql1)  #执行sql语句
# c.execute(sql3)  #执行sql语句
# conn.commit()   #提交数据库操作
# conn.close()    #关闭数据库连接
# print('插入数据完毕')

sql = "select id,name,address,salary from company"
cursor = c.execute(sql)

for row in cursor:
    print("id = ",row[0])
    print("name = ", row[1])
    print("address = ", row[2])
    print("salary = ", row[3],"\n")

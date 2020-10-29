# -*- codeing = utf-8 -*-
# @Time     : 10/29 16:09
# @Author   : River
# @File     : testXlwt.py
# @Software : PyCharm


import xlwt

workbook = xlwt.Workbook(encoding='utf-8',style_compression=0)  #创建workbook对象
worksheet = workbook.add_sheet('sheet1')    #创建工作表

# worksheet.write(0,0,'hello')    #写入数据，第1个参考表示行，第2个参考表示列，第3个参考是内容
# workbook.save('student.xls')

for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d * %d = %d"%(i+1,j+1,(i+1)*(j+1)))

workbook.save('student.xls')
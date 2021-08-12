import pymysql
from pymysql import cursors
from pymysql.cursors import Cursor
import scrapy
 
def dbHandle():
    conn = pymysql.connect(
        host = "localhost",
        user = "root",
        passwd = "0987410640",
        charset = "utf8",
        use_unicode = False
    )
    return conn
 
def pagination(pageNumber, pageSize):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        firstRecord = (pageNumber - 1)* pageSize
        maxRecord = pageSize
        cursor.execute('USE Question_SOF')
        cursor.execute('Select * from question_list LIMIT '+str(firstRecord)+','+str(maxRecord))
        result = cursor.fetchall()
        for question in result:
            print(question)
try:
        print("Input page number: ")
        a = int(input())
        print("Input page size: ")
        b = int(input())
        pagination(a,b)
except BaseException as e:
        print("The error is here>>>>>>>>>>>>>", e, "<<<<<<<<<<<<<<The error is here")
        

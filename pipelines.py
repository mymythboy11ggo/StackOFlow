import pymysql
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


def dbHandle():
    conn = pymysql.connect(
        host = "localhost",
        user = "root",
        passwd = "0987410640",
        charset = "utf8",
        use_unicode = False
    )
    return conn


class StackoverflowPipeline(object):
    def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        cursor.execute("USE Question_SOF")
                 #Insert database
        sql = "INSERT INTO question_list(Name) VALUES(%s)"
        try:
            cursor.execute(sql,
                           ( item['question']))
            cursor.connection.commit()
        except BaseException as e:
                         print("The error is here>>>>>>>>>>>>>", e, "<<<<<<<<<<<<<<The error is here")
        
        return item

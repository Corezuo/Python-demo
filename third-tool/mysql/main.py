# -*- coding: utf-8 -*-

"""
Python操作MySQL数据库
驱动：mysql-connector
Created by zfh on 2018/11/20
"""
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="123456", host="127.0.0.1", database="mooc")
cur = conn.cursor()

# 查询一条数据
# sql = "INSERT INTO `user` (openid, nickname, avatar, create_time, update_time) VALUES(%s, %s, %s, %s, %s)"
# val = ("12345", "dz", "www.img.com", "2018-11-20", None)
# cur.execute(sql, val)
# 提交事务
# conn.commit()

# 查询数据
cur.execute("SELECT * FROM `sc_user` WHERE id = %s", (3,))
# 取出第一条记录
result = cur.fetchone()
print("type: ", type(result))
print("value: ", result)
print("name: ", result[1])

# 获取所有记录
# result = cur.fetchall()
# print("rows: ", len(result))
# value = result[0]
# print("first record: ", value)
# print("record type: ", type(value))

# 删除数据
# sql = "DELETE FROM `user` WHERE id = %s"
# val = (2,)
# cur.execute(sql, val)
# conn.commit()

# 关闭数据库
conn.close()

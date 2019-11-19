# -*- coding: utf-8 -*-

"""
使用BdUtils数据库连接池
"""

import mysql.connector
from DBUtils.PooledDB import PooledDB


conn_kwargs = {'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'passwd': '123456', 'db': 'mooc', 'charset': "utf8"}
db_pool = PooledDB(mysql.connector, mincached=0, maxcached=10, maxshared=10, maxusage=100, **conn_kwargs)


if __name__ == '__main__':
    conn = db_pool.connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM `sc_user` WHERE id = %s", (3,))
    # 取出第一条记录
    result = cur.fetchone()
    print("type: ", type(result))
    print("value: ", result)
    print("name: ", result[1])

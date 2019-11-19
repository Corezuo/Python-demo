# -*- coding: utf-8 -*-

"""
商圈联合活动-统计数据分析

基本数据：

activity_id = 200
日期格式：%Y-%m-%d %H:%i:%s
DBUtils 数据库连接池

统计指标：
  1.每日转发数
  2.每日访客量
  3.每日到店人数
  4.每日销量
"""

import mysql.connector
import pyecharts.options as opts
from pyecharts.charts import Bar
from DBUtils.PooledDB import PooledDB


conn_kwargs = {'host': '139.129.xxx.xxx', 'port': 8066, 'user': 'xx', 'passwd': 'xx', 'db': 'sc_shop', 'charset': "utf8"}
db_pool = PooledDB(mysql.connector, mincached=0, maxcached=10, maxshared=10, maxusage=100, **conn_kwargs)


def query_every_day_share():
    """
    统计每日转发量
    :return: list
    """
    conn = db_pool.connection()
    cur = conn.cursor()
    query_sql = '''
    SELECT
        COUNT(id) AS num,
        DATE_FORMAT(create_time, '%Y-%m-%d') AS createTime
    FROM sc_shop_share_details
    WHERE operation_type = 1
    AND share_type = 19
    AND business_id = 200
    GROUP BY DATE_FORMAT(create_time, '%Y-%m-%d');
    '''
    cur.execute(query_sql, ())
    data = cur.fetchall()
    draw_echarts_graph(data, "每日转发量统计图")


def query_every_day_visitor():
    """
    统计每日访客量
    :return: list
    """
    conn = db_pool.connection()
    cur = conn.cursor()
    query_sql = '''
    SELECT
        COUNT(id) AS num,
        DATE_FORMAT(create_time, '%Y-%m-%d') AS createTime
    FROM sc_business_district_visitor
    WHERE business_type = 1
    AND business_id = 200
    GROUP BY DATE_FORMAT(create_time, '%Y-%m-%d');
    '''
    cur.execute(query_sql, ())
    data = cur.fetchall()
    draw_echarts_graph(data, "每日访客量统计图")


def query_every_day_enter_shop():
    """
    统计每日到店人数
    :return: list
    """
    conn = db_pool.connection()
    cur = conn.cursor()
    query_sql = '''
        SELECT
            COUNT(id) AS num,
            DATE_FORMAT(create_time, '%Y-%m-%d') AS createTime
        FROM sc_shop_exchange_receive
        WHERE exchange_type IN (5, 8)
        AND exchange_status = 1
        AND district_union_activity_id = 200
        GROUP BY DATE_FORMAT(create_time, '%Y-%m-%d');
        '''
    cur.execute(query_sql, ())
    data = cur.fetchall()
    draw_echarts_graph(data, "每日到店人数统计图")


def query_every_day_sign():
    """
    统计每日销量
    :return: list
    """
    conn = db_pool.connection()
    cur = conn.cursor()
    query_sql = '''
    SELECT
        COUNT(id) AS num,
        DATE_FORMAT(create_time, '%Y-%m-%d') AS createTime
    FROM sc_business_district_union_activity_purchase_record
    WHERE pay_status = 1
    AND dis_activity_id = 200
    GROUP BY DATE_FORMAT(create_time, '%Y-%m-%d');
    '''
    cur.execute(query_sql, ())
    data = cur.fetchall()
    draw_echarts_graph(data, "每日销量统计图")


def draw_echarts_graph(data, title):
    """
    使用echarts绘制直方图
    """
    # 提取x,y轴数据
    new_user_num_list = []
    date_list = []
    for item in data:
        new_user_num_list.append(item[0])
        date_list.append(item[1])

    bar = Bar(init_opts=opts.InitOpts(width="1400px", height="600px"))
    bar.add_xaxis(date_list)
    bar.add_yaxis(series_name="数量", yaxis_data=new_user_num_list, label_opts=opts.LabelOpts(is_show=False))
    bar.set_global_opts(
        tooltip_opts=opts.TooltipOpts(
            is_show=True,
            trigger="axis",
            axis_pointer_type="cross"
        ),
        yaxis_opts=opts.AxisOpts(
            splitline_opts=opts.SplitLineOpts(is_show=True)
        ),
        title_opts=opts.TitleOpts(title=title))
    bar.render(title + ".html")


if __name__ == '__main__':
    query_every_day_share()
    query_every_day_visitor()
    query_every_day_enter_shop()
    query_every_day_sign()

# -*- coding: utf-8 -*-

"""
用户量增长统计

目标：
    统计2016.08 ~ 2019.12用户增长量，以月为单位。

流程：
    1.查询MySQL数据
    2.清洗数据
    3.绘图
"""
import mysql.connector
from matplotlib import pyplot as plt
import pyecharts.options as opts
from pyecharts.charts import Bar


def query_data_by_mysql():
    """
    查询MySQL数据，分别统计每月新增的用户量
    :return: list
    """
    conn = mysql.connector.connect(user="xxx", passwd="xxx", host="139.129.xx.xx", database="sc_user", port="8066")
    cur = conn.cursor()
    query_sql = '''
    SELECT
        COUNT(id) AS num,
        DATE_FORMAT(createtime, '%Y-%m') AS createTime
    FROM sc_sys_user
    WHERE isdel = 0
    AND locked = 0
    GROUP BY DATE_FORMAT(createtime, '%Y-%m');
    '''
    cur.execute(query_sql, ())
    return cur.fetchall()


def draw_matplotlib_graph(data):
    """
    使用matplotlib绘制曲线图（绘图太慢）
    """
    # 提取x,y轴数据
    new_user_num_list = []
    date_list = []
    for item in data:
        new_user_num_list.append(item[0])
        date_list.append(item[1])

    # 绘图
    plt.figure(figsize=(100, 80), dpi=80)
    plt.plot(date_list, new_user_num_list)
    plt.xticks(date_list)
    plt.grid()
    plt.savefig("./graowth_statistics.png")
    # plt.show()


def draw_echarts_graph(data):
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
    bar.add_yaxis(series_name="新用户", yaxis_data=new_user_num_list, label_opts=opts.LabelOpts(is_show=False))
    bar.set_global_opts(
        tooltip_opts=opts.TooltipOpts(
            is_show=True,
            trigger="axis",
            axis_pointer_type="cross"
        ),
        yaxis_opts=opts.AxisOpts(
            splitline_opts=opts.SplitLineOpts(is_show=True)
        ),
        title_opts=opts.TitleOpts(title="2016.08 ~ 2019.12用户增量图"))
    bar.render("growth_statistics.html")


if __name__ == '__main__':
    data_list = query_data_by_mysql()
    draw_echarts_graph(data_list)

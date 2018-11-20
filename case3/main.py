# -*- coding: utf-8 -*-

"""
时间和日期
Created by zfh on 2018/11/20
"""

import time

print("当前时间戳：", time.time())
localtime = time.localtime(time.time())
print("本地时间：", localtime)
print("时间元祖：", time.localtime())
print("year: ", localtime.tm_year, "mon: ", localtime.tm_mon)
# 获取格式化的日期
asctime = time.asctime(time.localtime(time.time()))
print("asctime: ", asctime)
# 接收时间戳，返回格林威治天文时间的时间元组
print(time.gmtime(1542726958))
# 接受时间戳，返回当前时间下的时间元组
print(time.localtime(1542726958))
# 推迟调用线程的运行
start = time.time()
# time.sleep(1)
print("耗时：", time.time() - start, " s")
# 格式化日期
time1 = time.strftime("%Y-%m-%d", time.localtime())
print("time1: ", time1)

# 时间字符串转换为时间元组
try:
    time2 = time.strptime("2018/11/3", "%Y/%m/%d")
    print("time2: ", time2)
except BaseException as e:
    print("exception:", e)






# 字符串转化为时间戳
# time.strftime("%Y-%m-%d", "2018")

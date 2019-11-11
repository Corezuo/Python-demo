# -*- coding: utf-8 -*-

"""
pandas的常用数据类型

Series 一维，带标签数据
DataFrame 二维，Series容器
"""

import pandas as pd
import numpy as np

t = pd.Series([1, 3, 8, 13])
# 带标签的数组（索引）
print(t)

t2 = pd.Series([1, 3, 8, 12], index=list('abcd'))
print(t2)

# 通过字典创建Series
temp_dict = {"name": "dazuo", "age": 23}
t3 = pd.Series(temp_dict)
print(t3)


# DataFrame的创建（行索引，列索引）
t4 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list('abc'), columns=list('WXYZ'))
print(t4)

# 通过字典创建DataFrame的创建
t5 = {"name": ["dazuo", "yuanbao"], "age": [24, 23], "tel": [110, 112]}
df = pd.DataFrame(t5)
print(df)

# 显示头几行
print(df.head(1))
print(df.tail(1))
print(df.describe())

# df的排序
df2 = df.sort_values(by="age")
print(df2)

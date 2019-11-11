# -*- coding: utf-8 -*-

"""
numpy创建数组
"""

import numpy as np

# 使用numpy创建数组，得到ndarray的类型
t1 = np.array([1, 2, 3, ])
print(t1)
print(type(t1))

t2 = np.array(range(10))
print(t2)

t3 = np.arange(2, 10, 2)
print(t3)
print(t3.dtype)

t4 = np.arange(1, 4, dtype="float")
print(t4)
print(t4.dtype)

# 布尔类型
t5 = np.array([1, 1, 0, 1, 1], dtype=bool)
print(t5)
print(t5.dtype)

# 调整数据类型
t6 = t5.astype('int8')
print(t6)
print(t6.dtype)


"""
numpy数组的计算
"""
t1 = np.arange(12)
# 一维数组
print(t1.shape)

t2 = np.array([[1, 2, 3], [4, 5, 6]])
# 二维数组
print(t2.shape)

t3 = np.arange(12)
# 改变形状，调整为 3行 4列
t4 = t3.reshape(3, 4)
print(t4)

# 展开，转换为一维
t5 = t4.flatten()
print(t5)

# 数组中的每个元素的同时 + 2
# 当两个形状相同的两个数组相加，对应位置的元素进行计算
t6 = t5 + 2
print(t6)



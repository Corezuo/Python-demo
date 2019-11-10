# -*- coding: utf-8 -*-

"""
sorted排序高阶函数 和 operator.itemgetter()的使用
"""
from operator import itemgetter

# 定义一个列表
count = [1, -5, 22, 2, -39, 7]
print(count)

# 默认升序
count = sorted(count)
print(count)

print("------------------------------")

# 根据 key 函数进行排序，key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
# 绝对值排序
print(sorted(count, key=abs))

print("------------------------------")

# 忽略大小写的排序
str_list = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(str_list)

print("------------------------------")

# 反向排序，可以传入第三个参数
str_list = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(str_list)

print("------------------------------")

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 按照每个元祖的第0个元素，即：名字排序
print("custom: ", sorted(L, key=itemgetter(0)))
# 按照每个元祖的第1个元素，即：成绩排序
print("custom: ", sorted(L, key=itemgetter(1), reverse=True))

print("------------------------------")


# 自定义key函数，按照名字排序
def by_name(t):
    return t[0]


print("by_name: ", sorted(L, key=by_name))


# 自定义key函数，按照成绩排序
def by_scores(t):
    return -t[1]


print("by_scores: ", sorted(L, key=by_scores))


print("------------------------------")

# operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些序号（即需要获取的数据在对象中的序号）
a = ["name", "age", 3]
# 获取对象的第0个域的值
print(itemgetter(0)(a))
# 获取对象的第1个域和第0个的值
print(itemgetter(1, 0)(a))

print("------------------------------")

b = {"name": "dazuo", "age": 22}
# 获取索引位置的值
print(itemgetter("name", "age")(b))


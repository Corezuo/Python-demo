# -*- coding: utf-8 -*-


"""
数据类型 和 条件语句
"""

"""
字符串类型
"""
title = "hello world"
print(title)
# 字符格式化
print("hello %s" % "world")
print(title.__len__())
print(title.upper())


"""
List列表
"""
user_list = ["dazuo", 232.023, True]
print(user_list)
print(user_list[0])
user_list.append("yuanbao")
print(user_list)
item = user_list.pop()
print(item)


"""
Tuple元祖（类似于列表，但是元组不允许更新。而列表是允许更新的）
"""
first_touple = (1,)
test_touple = ('dazuo', 232.113)
print(test_touple)
print(test_touple[0])


"""
Dict字典（字典由索引(key)和它对应的值value组成）
"""
test_dict = {'name': 'dazuo'}
print(test_dict)
test_dict['age'] = 20
print(test_dict['name'])


"""
Set是一个无序不重复元素集，set的元素没有重复，而且是无序的。
"""
test_set = {'a', 'b', 'b'}
print(test_set)


"""
条件语句 if
"""
a = 23
if a == 23:
    print("number")
elif a == '23':
    print("string")
else:
    print("none")


"""
条件for...in循环
"""
order_list = ['123', 'abc', 232, 'dfasdf']
for item in order_list:
    print(item)


"""
while循环
"""
count = 5
while count > 1:
    count -= 1
    print(count)


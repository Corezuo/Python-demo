# -*- coding: utf-8 -*-

"""
正则表达式
Created by zfh on 2018/11/21
"""

import re

# 通过pattern对象匹配
pattern = re.compile('\d{3}\w{2}')
result = pattern.match("123abc")
if result is not None:
    print("hello")
    # 输出匹配的结果: 123ab
    print(result.group())

# 字符串加r，防止字符串被转义
print(r'\adb')

# 不使用pattern对象，直接通过match()方法
string = "hello world"
result = re.match("^hello [0-9a-z]{3}", string)
# 默认开头开始匹配，返回第一个匹配的结果，如果匹配失败返回None
print(result.group())
# 获取匹配字符的长度范围
print(result.span())

# re.search扫描整个字符串返回第一个成功匹配的结果
email = "863329112@qq.com"
result = re.search("\d{3}@", email)
# 输出112@
print(result.group())

# 将字符串中匹配的内容替换成其他值
newEmail = re.sub("\d{3}@", "113@", email)
print("newEmail: " + newEmail)

# 根据匹配分割字符串，返回分割字符串组成的列表
strList = re.split("\d{3}@", email)
print("strList: ", strList)

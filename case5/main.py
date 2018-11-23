# -*- coding: utf-8 -*-

"""
正则表达式
Created by zfh on 2018/11/21
"""

import re

content = "hello 1world"
result = re.match("^hello [0-9a-z]{3}", content)
# 获取匹配的结果
print(result.group())
# 获取匹配字符的长度范围
print(result.span())

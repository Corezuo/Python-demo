# -*- coding: utf-8 -*-

"""
正则表达式
Created by zfh on 2018/11/21
"""

import re

"""
Python提供re模块，可在python中利用正则式对字符串进行搜索、抽取和替换操作。

常用的匹配模式：
    \d        可以匹配一个数字
    \w        可以匹配一个数字或一个字母
    .         可以匹配任意字符
    *         表示任意个字符（包括0个）
    +         表示最少一个字符
    ?         表示0个或1个字符
    {n}       表示n个字符
    {n-m}     表示 n~m 个字符
    \d{3}     表示匹配3个数字
    \s        表示匹配一个空格
    \d{3,8}   表示3~8个数字
    [0-9]     可以精确表示范围。 
    A|B       可以匹配A或B
    ^         表示行的开头。
    $         表示行的结束。
    [abc]     匹配符合其中的一个字符。

示例：
    '00\d'          可以匹配'007',但是不能匹配'00A'。
    'py.'           可以匹配'py0'、'pya'等。
    '\d{2,3}'       可以匹配'23'、'123' 等。
    ^\d             表示必须以数字开头。
    \d$             表示必须以数字结束。
    '027-12345'     如果要匹配这个的字符，由于' - '是特殊字符，要用 ' \ ' 转义。
    [0-9a-zA-Z\_]   表示可以匹配一个数字、字母或者下划线；
    [0-9a-zA-Z\_]+  可以匹配至少由一个数字、字母或者下划线组成的字符串，如'0_Z'，'Py3000'等。

"""


def test_compile():
    """
    re.compile()
    将正则表达式编译成正则表达式对象，方便复用该正则表达式，返回一个pattern对象
    """
    pattern = re.compile('\\d{3}\\w{2}')
    result = pattern.match("123abc")
    if result is not None:
        print(result.group())


def test_match():
    """
    re.match()
    尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配的话，match（）就会返回None
    """
    string = "hello world"
    result = re.match("^hello [0-9a-z]{3}", string)
    # 默认开头开始匹配，返回第一个匹配的结果，如果匹配失败返回None
    print(result.group())
    # 获取匹配字符的长度范围
    print(result.span())


def test_search():
    """
    re.search()
    扫描整个字符串返回第一个成功匹配的结果
    """

    email = "863329112@qq.com"
    result = re.search("\\d{3}@", email)
    # 输出112@
    print(result.group())


def test_sub():
    """
    re.sub()
    替换字符串中每一个匹配的子串后，返回替换后的字符串
    """
    email = "863329112@qq.com"
    new_email = re.sub("\\d{3}@", "113@", email)
    print("newEmail: " + new_email)


def test_split():
    """
    re.split()
    根据匹配分割字符串，返回分割字符串组成的列表
    """
    email = "863329112@qq.com"
    str_list = re.split("\\d{3}@", email)
    print("strList: ", str_list)


def test_r():
    """
    字符串前加r，防止字符串被转义
    """
    print('\nabc')
    print(r'\nadb')


if __name__ == '__main__':
    test_r()


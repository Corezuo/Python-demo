# -*- coding: utf-8 -*-

"""
Requests 请求
Created by zfh on 2018/11/20
"""

import requests

response = requests.get("https://www.baidu.com")
# 编码
response.encoding = "utf-8"
print(response.text)
print("status_code：", response.status_code)
print("headers: ", response.headers)
print("content-type: ", response.headers['content-type'])


# Created by zfh on 2018/11/19

import requests
import json

"""
简单的爬虫实验
"""

# response = requests.get("https://www.baidu.com")
response = requests.get("http://httpbin.org/get")
response.encoding = "utf-8"
print(json.loads(response.text))

# -*- coding: utf-8 -*-

"""
BeautifulSoup的使用，网页解析器
Created by zfh on 2018/12/3
"""

from bs4 import BeautifulSoup
import requests

# 请求网页
response = requests.get("https://www.baidu.com")
response.encoding = 'utf-8'
html = response.content
# print(response.text)

doc = '''
<html> 
<head>
<meta http-equiv=content-type content=text/html;charset=utf-8>
<meta http-equiv=X-UA-Compatible content=IE=Edge>
<meta content=always name=referrer>
<link rel=stylesheet type=text/css href=https://ss1.bdstatic.com/baidu.min.css>
<title>百度一下，你就知道</title>
</head> 
<body link=#0000cc> 
    <div class=s_form> 
        <div class=s_form_wrapper> 
            <div id=lg> 
                <img hidefocus=true src=//www.baidu.com/img/bd_logo1.png width=270 height=129> 
            </div> 
            <form id=form name=f action=//www.baidu.com/s class=fm> 
                <input type=hidden name=bdorz_come value=1> 
                <input type=hidden name=ie value=utf-8> 
                <input type=hidden name=f value=8> 
                <input type=hidden name=rsv_bp value=1> 
                <input type=hidden name=rsv_idx value=1> 
                <input type=hidden name=tn value=baidu>
                <span class="bg s_ipt_wr">
                    <input id=kw name=wd class=s_ipt value maxlength=255 autocomplete=off autofocus=autofocus>
                </span>
                <span class="bg s_btn_wr">
                    <input type=submit id=su value=百度一下 class="bg s_btn" autofocus>
                </span> 
            </form> 
        </div> 
    </div> 
</body> 
</html>
'''

# 从字符串中读取html
# 指定解析器；lxml是python的一个解析器，支持html和xml的解析
soup = BeautifulSoup(doc, 'lxml')
print(soup.title)
print(soup.title.name)
print(soup.title.string)

# 找到所有的<input>标签
for link in soup.find_all('input'):
    print(link)

# 取出所有的文字内容
# print(soup.get_text)

# 从文件流中读取html
soup = BeautifulSoup(open("index.html"), "lxml")
print(soup.find('h1'))


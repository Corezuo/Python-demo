# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

"""
知乎Hot热点数据采集器
~~~~~~~~~~~~~~~~~~
"""

"""
请求页面数据
使用的三方库 requests
"""
def _get_zhihu_hot_page():
    url = "https://www.zhihu.com/hot"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': '_zap=5a05f5ca-1870-4549-9766-ee3787d0210a; _xsrf=4gBtsPCxDVIBepE6eVazyXrM7gqtZydq; d_c0="ACDh_aNxvQ-PTpWO7hzbxN9lPJci4MFkjpk=|1563191403"; q_c1=db9b28cc635c4016b6be42060edeaa85|1563359433000|1563359433000; tgw_l7_route=80f350dcd7c650b07bd7b485fcab5bf7; l_n_c=1; l_cap_id="MDg2MjMxYmNlNzE2NGEwZjgwMDE1MjZiMDdiYTg4YzM=|1565400527|6d40ed251fd94705de98305ea55149398a56d2a8"; r_cap_id="ZTQxYzI2YzFiZTQ3NDg4NjhiZmVmNDdlYjczNzE5MjA=|1565400527|34b4a6bbf742759015b619cc537417e4a67bb98c"; cap_id="NDkzODc5ZmIwMjg2NGVkNTlmYTA1ZWNiMTY4NWNlODM=|1565400527|026e68ae2b95a73ac94dc531363f2cb3514bb839"; n_c=1; __utmc=51854390; __utmv=51854390.000--|3=entry_date=20190717=1; __utma=51854390.17438644.1565400529.1565400529.1565400542.2; __utmb=51854390.0.10.1565400542; __utmz=51854390.1565400542.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; tst=h; tshl=; capsion_ticket="2|1:0|10:1565400837|14:capsion_ticket|44:MjA0MGRlMTY1MDUyNDlkZTgxZWVhYmNjOTA2NGJiM2E=|958980dcd6fe58409040792a9d3c72ca3383cc3f0ccc0a31060319574a9b1b40"; z_c0="2|1:0|10:1565400900|4:z_c0|92:Mi4xdGYxa0F3QUFBQUFBSU9IOW8zRzlEeWNBQUFDRUFsVk5SS3gxWFFERXdQZG9BemhzQ2w0b3JMSmVXSno2MkQ4dkdn|d520155bb609c5e241e78dbe02d9e176c337fb638b9f4d953dc9f68a45115005"',
        'referer': 'https://www.zhihu.com/signin?next=%2Fhot'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print("请求错误！")
        return None


"""
解析知乎hot页面Top 50元素

提取元素（标题、链接、简介、配图、热度）
使用的三方库 BeautifulSoup
"""
def _parse_hot_item_element(content):
    # 对源代码进行美化
    soup = BeautifulSoup(content, "html.parser")
    s = soup.prettify()
    # print(s)

    # 获取TopList热点节点
    hot_list = soup.main.contents[0].div.contents[0].contents[1].contents[0].contents[0].contents[1]
    # 提取item子节点
    section_list = []
    for section in hot_list.contents:
        # 提取标题
        item_title = section.contents[1].contents[0].contents[0].contents[0]

        # 提取链接
        item_link = section.contents[1].contents[0].attrs['href']

        # 提取简介
        try:
            item_profil = section.contents[1].contents[0].contents[1].contents[0]
        except IndexError:
            item_profil = ""

        # 提取配图
        try:
            item_img_link = section.contents[2].contents[0].attrs['src']
        except IndexError:
            item_img_link = ""

        # 提取热度
        item_metrics = section.contents[1].contents[1].contents[1]

        item_info = {
            "title": item_title,
            "link": item_link,
            "profil": item_profil,
            "img_link": item_img_link,
            "metrics": item_metrics
        }
        section_list.append(item_info)

    return section_list


"""
方案一：通过缓存调度，采集数据，写入内存数据
"""
def start_collect():
    html_content = _get_zhihu_hot_page()
    section_list = _parse_hot_item_element(html_content)
    print(section_list)


"""
方案二：实时查询
"""
def get_hot_list():
    html_content = _get_zhihu_hot_page()
    return _parse_hot_item_element(html_content)

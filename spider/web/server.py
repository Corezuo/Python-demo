# -*- coding: utf-8 -*-

"""
web服务器
"""
from flask import Flask, send_file
from spider.collect import collect
import json

webapp = Flask(__name__,
               static_url_path="/static",
               static_folder="../html/static",
               template_folder="../html")


@webapp.route("/index", methods=["GET"])
def index():
    """展示的静态页面"""
    return send_file('../html/index.html')


@webapp.route("/hot-list", methods=["GET"])
def query_hot_list():
    """查询知乎热点数据"""
    hot_list = collect.get_hot_list()
    return json.dumps(hot_list)

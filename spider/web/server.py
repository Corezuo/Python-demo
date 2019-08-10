# -*- coding: utf-8 -*-

"""
web服务器
"""
from flask import Flask, send_file
from collect import collect
import json

webapp = Flask(__name__,
               static_url_path="/static",
               static_folder="../html/static",
               template_folder="../html")

"""
展示的静态页面
"""
@webapp.route("/index", methods=["GET"])
def index():
    return send_file('../html/index.html')


"""
查询知乎热点数据
"""
@webapp.route("/hot-list", methods=["GET"])
def query_hot_list():
    hot_list = collect.get_hot_list()
    return json.dumps(hot_list)

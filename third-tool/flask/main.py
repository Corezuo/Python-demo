# -*- coding: utf-8 -*-

"""
flask web服务器
"""
from flask import Flask

webapp = Flask(__name__)


@webapp.route("/web", methods=["GET"])
def hello_world():
    return "hello world"


if __name__ == "__main__":
    webapp.run("127.0.0.1", 8080)

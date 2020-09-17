# -*- coding: utf-8 -*-

"""
知乎Spider启动器
"""
from spider.web.server import webapp
from spider.cron import task


if __name__ == "__main__":
    # task.start()
    webapp.run(host='127.0.0.1', debug=False, port=8080)

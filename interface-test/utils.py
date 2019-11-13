# -*- coding: utf-8 -*-

import json

import requests

import const

"""
工具类
"""

# 环境
env = const.dev


def unified_post(cmd, data, succ_callback):
    """
    封装统一的POST请求
    @:param cmd           请求cmd
    @:param data          请求参数
    @:param succ_callback 成功的回调
    """
    form_data = {
        "cmd": cmd,
        "data": json.dumps(data),
        "version": 1
    }
    response = requests.post(url=env["url"], data=form_data, headers=env["headers"], timeout=10)
    if response.status_code == 200:
        content = json.loads(response.content)
        return succ_callback(content)
    else:
        _err_callback(response.reason)


def _succ_callback():
    """
    统一的成功处理
    """
    pass


def _err_callback(reason):
    """
    统一的失败处理
    """
    print("统一请求异常处理！")
    print(reason)

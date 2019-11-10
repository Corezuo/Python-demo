# -*- coding: utf-8 -*-

"""
异常处理
"""
from syntax.error.custom_error import CustomError

if __name__ == "__main__":
    try:
        raise CustomError('发生CustomError异常')
    except Exception as e:
        print(e.args)
    finally:
        print("执行了")

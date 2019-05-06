# -*- coding: utf-8 -*-

"""
面向对象的语法
"""


class User:

    def __init__(self):
        self.name = "dazuo"
        print("初始化")

    def get_name(self):
        return self.name

    @staticmethod
    def get_age():
        print("age: 22")


if __name__ == '__main__':
    user = User()
    print(user.get_name())
    User.get_age()

# -*- coding: utf-8 -*-

"""
面向对象的语法
"""


class User:
    bar = 1

    __gender = 'dazuo'

    # 无参构造函数
    def __init__(self):
        self.name = 'dazuo'
        print("无参构造函数")

    # 一个类只能有一个构造函数存在，不能重载
    # def __init__(self, name):
    #     self.name = name
    #     print("无参构造函数")

    def get_name(self):
        return self.name

    # 私有属性的访问
    def get_gender(self):
        return self.__gender

    # 静态方法
    @staticmethod
    def get_age():
        print("age: 22")

    # classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，
    # 可以来调用类的属性，类的方法，实例化对象等。
    @classmethod
    def get_class(cls):
        print(cls.bar)


if __name__ == '__main__':
    # 类的示例化
    user = User()
    print(user.get_name())
    User.get_age()

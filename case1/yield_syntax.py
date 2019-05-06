# -*- coding: utf-8 -*-

import random

# 默认生成包含10个数的list
for n in range(10):
    print(n)

print("---------------------------------")

# 定义一个列表
count = [1, 2, 3, 4]
for n in count:
    print(n)

print("---------------------------------")

# 遍历字典
data = {"name": "dazuo", "age": 22}
for k, v in data.items():
    print("k: ", k, " v: ", v)

print("---------------------------------")


# yield的用法
def foo():
    print("foo starting...")
    counter = 0
    while counter < 3:
        counter += 1
        print("yield start ...")
        yield 4
        print("yield end ...")


# 生成一个 generator，但是不会调用函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。
# 虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。
# 看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。

# 方式一：
p = foo()
print("1-------", next(p))
print("2-------", next(p))
print("3-------", next(p))

print("---------------------------------")

# 或者方式二：
for n in foo():
    print(n)

print("---------------------------------")

print("random：", random.random())





# -*- coding: utf-8 -*-

"""
matplotlib绘图
"""

from matplotlib import pyplot as plt

# 设置图片大小
plt.figure(figsize=(10, 8), dpi=80)

x = range(0, 24, 2)
y1 = [15, 13, 14, 5, 17, 20, 8, 9, 14, 10, 18, 15]
y2 = [1, 2, 3, 5, 11, 14, 16, 19, 19, 20, 20, 20]

# 绘图
plt.plot(x, y1, label='y1')
plt.plot(x, y2, label='y2')

# 设置x、y轴的刻度
plt.xticks(x)
plt.yticks(range(0, 20, 2))

# 绘制网格
plt.grid()

# 添加图例
plt.legend()

# 图片保存
# plt.savefig("./sig_size.png")

# 展示图形
plt.show()

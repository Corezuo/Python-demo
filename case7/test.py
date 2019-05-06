# -*- coding: utf-8 -*-

# 用户-电影评分列表
user, movieId, rating = '1', '1', '4.0'
# 用户1
train_set = {}
train_set.setdefault(user, {})
train_set[user][movieId] = rating
print(train_set)

# 用户2
train_set.setdefault('2', {})
train_set['2']['1'] = '5.0'
print(train_set)

# dict.items
print(train_set.items())
for user, movies in train_set.items():
    print("user: ", user, " movies: ", movies)
    for movie in movies:
        print("movie: ", movie)

print("-------------------------------")

b = {}
u = '1'
v = '2'
b.setdefault(u, {})
b[u].setdefault(v, 0)
b[u][v] += 1
b[u]['3'] = 0




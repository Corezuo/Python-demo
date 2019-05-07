# -*- coding: utf-8 -*-
# 基于用户的协同过滤推荐算法实现

import math
import random
from operator import itemgetter


class UserBasedCF:
    # 初始化相关参数
    def __init__(self):
        # 找到与目标用户兴趣相似的20个用户，为其推荐10部电影
        self.n_sim_user = 20
        self.n_rec_movie = 10

        # 将数据集划分为训练集和测试集
        self.trainSet = {}
        self.testSet = {}

        # 用户相似度矩阵
        self.user_sim_matrix = {}
        self.movie_count = 0

        print('Similar user number = %d' % self.n_sim_user)
        print('Recommneded movie number = %d' % self.n_rec_movie)

    # 读文件得到“用户-电影”评分数据
    def get_dataset(self, filename, pivot=0.75):
        train_set_len = 0
        test_set_len = 0
        for line in self.load_file(filename):
            user, movie, rating, timestamp = line.split(',')
            # 划分测试集和测试集
            if random.random() < pivot:
                self.trainSet.setdefault(user, {})
                self.trainSet[user][movie] = rating
                train_set_len += 1
            else:
                self.testSet.setdefault(user, {})
                self.testSet[user][movie] = rating
                test_set_len += 1
        print('Split trainingSet and testSet success!')
        print('TrainSet = %s' % train_set_len)
        print('TestSet = %s' % test_set_len)

    # 读文件（数据集）
    @staticmethod
    def load_file(filename):
        with open(filename, 'r') as f:
            for i, line in enumerate(f):
                if i == 0:  # 去掉文件第一行的title
                    continue
                yield line.strip('\r\n')
        print('Load %s success!' % filename)

    # 计算用户之间的相似度
    def calc_user_sim(self):
        print('Building movie-user table ...')
        # 构建“电影-用户”倒排表
        # key = movieID, value = list of userIDs who have seen this movie
        movie_user = {}
        for user, movies in self.trainSet.items():
            for movie in movies:
                if movie not in movie_user:
                    movie_user[movie] = set()
                movie_user[movie].add(user)
        print('Build movie-user table success!')

        self.movie_count = len(movie_user)
        print('Total movie number = %d' % self.movie_count)

        # 构建用户相似度矩阵
        print('Build user co-rated movies matrix ...')
        for movie, users in movie_user.items():
            # 迭代：某一部电影的相识度矩阵
            for u in users:
                for v in users:
                    if u == v:
                        continue
                    self.user_sim_matrix.setdefault(u, {})
                    self.user_sim_matrix[u].setdefault(v, 0)
                    self.user_sim_matrix[u][v] += 1
        print('Build user co-rated movies matrix success!')

        # 计算用户相似性
        print('Calculating user similarity matrix ...')
        for u, related_users in self.user_sim_matrix.items():
            for v, count in related_users.items():
                # 余弦相似度计算
                self.user_sim_matrix[u][v] = count / math.sqrt(len(self.trainSet[u]) * len(self.trainSet[v]))
        print('Calculate user similarity matrix success!')

    # 针对目标用户U，找到其最相似的K个用户，产生N个推荐
    def recommend(self, user):
        # 最相似的K个用户
        k = self.n_sim_user
        # 取N个推荐
        n = self.n_rec_movie
        # 推荐的电影列表
        rank = {}
        # 目标用户看过的电影
        watched_movies = self.trainSet[user]

        # 从倒排表中找到最相似的K个用户
        # v=similar user（用户）, wuv=similar factor（相似度）
        for v, wuv in sorted(self.user_sim_matrix[user].items(), key=itemgetter(1), reverse=True)[0:k]:
            # 找出相似用户看过的电影
            for m in self.trainSet[v]:
                # 过滤掉目标用户看过的电影
                if m in watched_movies:
                    continue
                rank.setdefault(m, 0)
                # 计算用户u对电影m的感兴趣程度（即：同一部电影，多个用户的相似度 进行 等差数列求和）
                rank[m] += wuv

        # 通过感兴趣程度，取最高的N个推荐
        return sorted(rank.items(), key=itemgetter(1), reverse=True)[0:n]

    # 产生推荐并通过准确率、召回率和覆盖率进行评估
    def evaluate(self):
        print("Evaluation start ...")
        # 推荐的K个电影
        n = self.n_rec_movie

        # 命中的电影数量（有重复）
        hit = 0
        # 推荐的电影总数（有重复）
        rec_count = 0
        # 测试集 用户看过的电影总数（有重复）
        test_count = 0
        # 所有推荐的电影（不重复）
        all_rec_movies = set()

        for i, user, in enumerate(self.trainSet):
            # 测试集-用户看过的电影
            test_movies = self.testSet.get(user, {})
            # 被推荐的电影
            rec_movies = self.recommend(user)
            for movie, w in rec_movies:
                if movie in test_movies:
                    hit += 1
                all_rec_movies.add(movie)
            rec_count += n
            test_count += len(test_movies)

        # 推荐准确率 = 命中的电影数 / 系数 * 推荐的总数
        precision = hit / (1.0 * rec_count)
        # 召回率 = 命中的电影数 / 系数 * 测试集中用户看过的电影总数
        recall = hit / (1.0 * test_count)
        # 覆盖率 = 所有推荐的电影数 / 系数 * 电影的总数
        coverage = len(all_rec_movies) / (1.0 * self.movie_count)
        print('precision=%.4f\trecall=%.4f\tcoverage=%.4f' % (precision, recall, coverage))


if __name__ == '__main__':
    rating_file = 'F:\\Python-demo\\case7\\dataset\\ml-latest-small\\ratings.csv'
    userCF = UserBasedCF()
    userCF.get_dataset(rating_file)
    userCF.calc_user_sim()
    userCF.evaluate()

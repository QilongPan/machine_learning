# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-12-15 10:53:11
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-12-15 14:01:50

'''
data set source:http://files.grouplens.org/datasets/movielens/ml-latest-small.zip
'''

import csv
class UserCF(object):

    def __init__(self):
        pass

    def create_data(self):
        csv_file = csv.reader(open("E:/data/ml-latest-small/ratings.csv",'r'))
        arr = list(csv_file)
        count = 1
        train = []
        for line in range(50):
            print(arr[line])
            train.append(line)
            count += 1
            if count > 50:
                break
        return train

    def calculate_similarity_jaccard(self,intersection_len,union_set_len):
        return intersection_len / union_set_len

    def user_similarity(self,train):
        for i in range(len(train)):
            for j in range(i+1,len(train)):
                if train[i][0] == train[j][0]:
                    continue


if __name__ == "__main__":
    cf = UserCF()
    cf.create_data()



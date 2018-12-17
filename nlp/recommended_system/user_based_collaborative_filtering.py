# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-12-15 10:53:11
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-12-17 13:48:35

'''
data set source:http://files.grouplens.org/datasets/movielens/ml-latest-small.zip
'''

import csv
import math
import operator

class UserCF(object):

    def __init__(self):
        pass

    def create_data(self):
        csv_file = csv.reader(open("E:/data/ml-latest-small/ratings.csv",'r'))
        arr = list(csv_file)
        count = 1
        train = []
        for i in range(1,len(arr)):
            train.append(arr[i])
            count += 1
            if count > 500:
                break
        return train

    def get_user_film(self,train,user_film_dic):
        for element in train:
            '''
            determine if exists key:
                (1)in
                "1" in dic
                if not exist will return False
                (2)get
                dic.get("1",-1)
                if not exist will return -1
            '''
            if element[0] not in user_film_dic:
                user_film_dic[element[0]] = []
            user_film_dic[element[0]].append(element[1])
        return user_film_dic

    def calculate_user_similarity(self,user_film_dict):
        similarity_dic = dict()
        for key1 in user_film_dic.keys():
            similarity_dic[key1] = dict()
            for key2 in user_film_dic.keys():
                if key1 == key2:
                    similarity = 0
                else:
                    similarity = self.calculate_similarity(user_film_dic[key1],user_film_dic[key2])
                similarity_dic[key1][key2] = similarity
        return similarity_dic


    def get_intersection_number(self,user_film1,user_film2):
        number = 0
        for film in user_film1:
            if film in user_film2:
                number += 1
        return number

    def calculate_similarity(self,user_film1,user_film2):
        equal_number = self.get_intersection_number(user_film1,user_film2)
        denominator = len(user_film1) + len(user_film2)
        if denominator == 0:
            return 0
        return equal_number / math.sqrt(denominator) 

    def get_most_similar_users(self,k,similarity_dic):
        '''
        sorted return is new arr,input arr do not change
        '''
        similarity_dic_temp = sorted(similarity_dic.items(),key = operator.itemgetter(1),reverse = True)
        users = []
        count = 0
        for i in similarity_dic_temp:
            users.append(i[0])
            count += 1
            if count >= k:
                break
        return users

if __name__ == "__main__":
    user_film_dic = dict()
    cf = UserCF()
    train = cf.create_data()
    cf.get_user_film(train,user_film_dic)
    similarity_dic = cf.calculate_user_similarity(user_film_dic)
    users = cf.get_most_similar_users(3,similarity_dic['2'])
    print("most similarity users:")
    print(users)





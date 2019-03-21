# -*- coding: utf-8 -*-
# @Date    : 2019-03-21 08:33:39
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com

from collections import Counter
import math
class Tree(object):

    def __init__(self):
        pass



class ID3(Tree):

    def __init__(self):
        pass


    #计算信息熵
    def calcShannonEnt(self,Y):
        #统计每种类别的数量，返回dict
        label_value_counts = Counter(Y)
        label_count = len(Y)
        #dic迭代 for value in di.values() 和 for value in di等价输出key
        #同时输出key,value使用for key,value in di.items()
        label_value_probs = map(lambda key:float(label_value_counts[key])/ label_count,label_value_counts)
        li = map(lambda prob:-1 * prob * math.log(prob,2),label_value_probs)
        return sum(li)

    def get_sub_data_set_by_feature_value(self,X,axis,value):
        sub_data_set = []
        for data in X:
            if data[axis] == value:
                sub_data_set.append(data)
        return sub_data_set


    #选出最好的划分属性(信息增益最高)
    def chooseBestFeatureToSplit(self,X):
        feature_num = len(X[0])
        #遍历所有的特征
        for i in range(feature_num):
            #得到特征的值
            feat_list = [element[i] for element in X]
            #使用set进行去重，找出该特征所拥有的所有值
            unique_values = set(feat_list)
            entropy = 0.0
            for value in unique_values:
                #得到属性值为value的子集
                sub_data_set = self.get_sub_data_set_by_feature_value(X,i,value)
                prob = len(sub_data_set) / float(len(X))
                pass





    def fit(self,X,Y):
        if len(X) < 0:
            print("X len is 0")
        else:
            shannonent_value = self.calcShannonEnt(Y)
            print(shannonent_value)

if __name__ == "__main__":
    Y = [1, 2, 3, 1, 1, 2]
    id3 = ID3()
    id3.fit([], Y)





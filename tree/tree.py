# -*- coding: utf-8 -*-
# @Date    : 2019-03-21 08:33:39
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com

from collections import Counter
from data import Data
import math
import numpy as np 
class Tree(object):

    def __init__(self):
        pass


class ID3(Tree):

    def __init__(self,**kwargs):
        #停止分裂的条件
        #最小节点数
        self.min_node_num = kwargs.get('min_node_num',1)
        #节点深度
        self.depth = kwargs.get('depth',None)

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

    #得到X中第axis个属性的值等于value的数据所对应的标签
    def get_sub_data_set_by_feature_value(self,X,Y,axis,value):
        sub_X = []
        sub_Y = []
        sub_data_set = []
        for j in range(len(X)):
            data = X[j]
            if data[axis] == value:
                sub_Y.append(Y[j])
                sub_X.append(X[j])
        return sub_X,sub_Y


    #选出最好的划分属性(信息增益最高)
    def chooseBestFeatureToSplit(self,X,Y):
        base_entropy = self.calcShannonEnt(Y)
        feature_num = len(X[0])
        best_info_gain = float('-inf')
        best_feature = -1
        #遍历所有的特征
        for i in range(feature_num):
            #得到特征的值
            feat_list = [element[i] for element in X]
            #使用set进行去重，找出该特征所拥有的所有值
            unique_values = set(feat_list)
            entropy = 0.0
            for value in unique_values:
                #得到属性值为value的子集
                sub_X,sub_Y = self.get_sub_data_set_by_feature_value(X,Y,i,value)
                prob = len(sub_Y) / float(len(X))
                entropy += prob * self.calcShannonEnt(sub_Y)
            info_gain = base_entropy - entropy
            if info_gain > best_info_gain:
                best_info_gain = info_gain
                best_feature = i
        return best_feature


    def create_tree(self,X,Y,visit_feature_num = 0,tree = dict()):
        #类别完全相同则停止划分
        if len(Counter(Y)) == 1:
            return Y[0]
        #遍历完所有特征，返回出现次数最多的类别
        if visit_feature_num == self.feature_num:
            return max(Counter(Y))
        #遍历完所有特征时，返回出现次数最多的类别
        best_feature = self.chooseBestFeatureToSplit(X,Y)
        print("best_feature",best_feature)
        tree[best_feature] = dict()
        #得到特征具有的值
        feature_value_counts = Counter([data[best_feature] for data in X])
        tree[best_feature]['label_value_counts'] = feature_value_counts
        print(feature_value_counts)
        for key in feature_value_counts.keys():
            sub_X,sub_Y = self.get_sub_data_set_by_feature_value(X,Y,best_feature,key)
            tree[best_feature]['sample'] = sub_Y
            self.create_tree(sub_X,sub_Y,visit_feature_num+1,tree[best_feature])
        return tree

    def fit(self,X,Y):
        if len(X) < 0:
            print("X len is 0")
        else:
            self.feature_num = len(X[0])
            print(self.feature_num)
            print(self.create_tree(X,Y))


class C45(ID3):

    def __init__(self):
        pass

    #选出最好的划分属性(信息增益最高)
    def chooseBestFeatureToSplit(self,X,Y):
        base_entropy = self.calcShannonEnt(Y)
        feature_num = len(X[0])
        best_info_gain_rate = float('-inf')
        best_feature = -1
        #遍历所有的特征
        for i in range(feature_num):
            #得到特征的值
            feat_list = [element[i] for element in X]
            #使用set进行去重，找出该特征所拥有的所有值
            unique_values = set(feat_list)
            entropy = 0.0
            for value in unique_values:
                #得到属性值为value的子集
                sub_X,sub_Y = self.get_sub_data_set_by_feature_value(X,Y,i,value)
                prob = len(sub_Y) / float(len(X))
                entropy += prob * self.calcShannonEnt(sub_Y)
            if entropy == 0:
                return i 
            else:
                info_gain = base_entropy - entropy
                info_gain_rate = float(info_gain) / entropy
                if info_gain_rate > best_info_gain_rate:
                    best_info_gain_rate = info_gain_rate
                    best_feature = i
        return best_feature


class Cart(Tree):

    def __init__(self):
        pass

if __name__ == "__main__":
    data = Data()
    X,Y = data.data1()
    id3 = C45()
    id3.fit(X,Y)
#    id3.fit([], Y)


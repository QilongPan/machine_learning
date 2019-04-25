# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-19 17:36:42
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-19 20:01:53
import pandas as pd 

data_test = pd.read_csv("E:/allcode/machineLearningExercise/titanic/data/test.csv")
data_test.to_csv("E:/allcode/machineLearningExercise/titanic/data/test2.csv",index = False)
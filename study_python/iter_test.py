# -*- coding: utf-8 -*-
# @Date    : 2019-05-15 14:01:57
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com

class ListIter(object):

    def __init__(self,data):
        self.current_index = -1
        self.data = data

    def __next__(self):
        self.current_index += 1
        if self.current_index >= len(self.data):
            raise StopIteration
        return self.data[self.current_index]


    def __iter__(self):
        return self

data = [1,2,3,4]
list_iter = ListIter(data)
data[0] = 5
for element in list_iter:
    print(element)

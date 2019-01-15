# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-12-25 15:00:27
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-12-25 16:12:33
import numpy as np 
def generate_data(num = 50):
    X = np.array(np.random.choice(2,size = (num,)))
    Y = []
    for i in range(num):
        threshold = 0.5
        if X[i-3] == 1:
            threshold += 0.5
        if X[i-8] == 1:
            threshold -= 0.25
        if np.random.rand() > threshold:
            Y.append(0)
        else:
            Y.append(1)
    return X,np.array(Y)

def generate_batch(raw_data,batch_size,num_steps):
    raw_x,raw_y = raw_data
    data_length = len(raw_x)

    batch_partition_length = data_length // batch_size
    
if __name__ == "__main__":
    X,Y = generate_data()
    print(Y)

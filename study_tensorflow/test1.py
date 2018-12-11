# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-12-11 10:09:58
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-12-11 10:46:51

import tensorflow as tf 
import numpy as np 

x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.4 + 0.7

learn_rate = tf.placeholder(dtype = tf.float32)
'''
tf.random_uniform:
Outputs random values from a uniform distribution.
The generated values follow a uniform distribution in the range [minval, maxval). 
The lower bound minval is included in the range, while the upper bound maxval is excluded.
For floats, the default range is [0, 1). For ints, at least maxval must be specified explicitly.
'''
weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases = tf.Variable(tf.zeros([1]))
predict_y = weights * x_data + biases

# loss function
loss = tf.reduce_mean(tf.square(predict_y-y_data))

#梯度下降优化器，定义learning rate
optimizer = tf.train.GradientDescentOptimizer(learn_rate)

#训练目标是loss最小化
train = optimizer.minimize(loss)

#初始化变量，即初始化 Weights 和 biases
init = tf.global_variables_initializer()

#创建session，进行参数初始化
sess = tf.Session()
sess.run(init)

#开始训练200步，每隔20步输出一下两个参数
for step in range(10000):
    sess.run(train,feed_dict = {learn_rate:0.1})
    if step % 20 == 0:
        print(step,sess.run(weights),sess.run(biases))
### create tensorflow structure end ###
sess.close()
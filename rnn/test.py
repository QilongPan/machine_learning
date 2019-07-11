# -*- coding: utf-8 -*-
# @Date    : 2019-05-29 10:20:04
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com

import tensorflow as tf 
import numpy as np

n_inputs = 3
n_neurons = 5

X0 = tf.placeholder(tf.float32,[None,n_inputs])
X1 = tf.placeholder(tf.float32,[None,n_inputs])

# 由于Wx要和X相乘，故低维是n_inputs
Wx = tf.Variable(tf.random_normal(shape=[n_inputs, n_neurons],dtype=tf.float32))
# 低维，高维都是n_neurons，为了使得输出也是hidden state的深度
# 这样下一次才可以继续运算
Wy = tf.Variable(tf.random_normal(shape=[n_neurons,n_neurons],dtype=tf.float32))
b = tf.Variable(tf.zeros([1, n_neurons], dtype=tf.float32))

# Y0初始化为0，初始时没有记忆
Y0 = tf.tanh(tf.matmul(X0, Wx) + b)
# 把上一轮输出Y0也作为输入
Y1 = tf.tanh(tf.matmul(Y0, Wy) + tf.matmul(X1, Wx) + b)
init = tf.global_variables_initializer()
X0_batch = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 0, 1]]) # t = 0 
X1_batch = np.array([[9, 8, 7], [0, 0, 0], [6, 5, 4], [3, 2, 1]]) # t = 1  
with tf.Session() as sess:
    init.run()
    Y0_val, Y1_val = sess.run([Y0, Y1], feed_dict={X0: X0_batch, X1: X1_batch}) 
    print(Y0_val)
    print(Y1_val)

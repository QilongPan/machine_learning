# -*- coding: utf-8 -*-
# @Date    : 2019-04-17 13:39:21
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com

import tensorflow as tf
import numpy as np

# 定义一个矩阵a，表示需要被卷积的矩阵。
a = np.array(np.arange(1, 1 + 20).reshape([1, 10, 2]), dtype=np.float32)

# 卷积核，此处卷积核的数目为1
kernel1 = np.array(np.arange(1, 65), dtype=np.float32).reshape([1, 2, 32])
kernel2 = np.array(np.arange(1, 3*2*64+1), dtype=np.float32).reshape([3, 2, 64])
kernel3 = np.array(np.arange(1, 5*2*128+1), dtype=np.float32).reshape([5, 2, 128])
# 进行conv1d卷积
conv1d1 = tf.nn.conv1d(a, kernel1, 1, 'SAME')
conv1d2 = tf.nn.conv1d(a, kernel2, 1, 'SAME')
conv1d3 = tf.nn.conv1d(a, kernel3, 1, 'SAME')

conv1d = tf.concat([conv1d1,conv1d2,conv1d3],1)
with tf.Session() as sess:
    # 初始化
    tf.global_variables_initializer().run()
    # 输出卷积值
    print(sess.run(conv1d1).shape)
    print(sess.run(conv1d2).shape)
    print(sess.run(conv1d3).shape)
    print(sess.run(conv1d).shape)

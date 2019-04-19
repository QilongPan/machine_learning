# -*- coding: utf-8 -*-
# @Date    : 2019-04-18 11:21:14
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com
import tensorflow as tf 
import numpy as np 

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([1,2])
op = tf.math.argmax(arr1,1)
op2 = tf.math.argmax(arr2,0)
correct = tf.equal(tf.math.argmax(arr1,1),arr2)
accuracy = tf.reduce_mean(tf.cast(correct, "float"))
with tf.Session() as sess:
    print(sess.run(accuracy))

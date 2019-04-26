# -*- coding: utf-8 -*-
# @Date    : 2019-04-26 12:38:42
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ""
import numpy as np
import tensorflow as tf
np.random.seed(0)
x = np.random.sample((11,2))

dataset = tf.data.Dataset.from_tensor_slices(x)
dataset = dataset.shuffle(3)
dataset = dataset.batch(4)
dataset = dataset.repeat(2)

# create the iterator
iter = dataset.make_one_shot_iterator()
el = iter.get_next()

with tf.Session() as sess:
    print(sess.run(el))

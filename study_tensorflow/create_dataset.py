# -*- coding: utf-8 -*-
# @Date    : 2019-04-25 09:47:58
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com

import tensorflow as tf 

def make_dataset_from_const_tensor():
    features = [[1, 2, 3, 5, 2, 1],
                [1, 3, 2, 4, 1, 2],
                [1, 4, 2, 4, 3, 5]]
    labels = [1, 2, 3]
    dataset = tf.data.Dataset.from_tensor_slices((features, labels))
    dataset.shuffle(10).repeat(2).batch(3)
    return dataset

def read():
    dataset = make_dataset_from_const_tensor()
    with tf.Session() as sess:
        data = dataset.make_one_shot_iterator().get_next()
        print(sess.run(data))

read()
read()
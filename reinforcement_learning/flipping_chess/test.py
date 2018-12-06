# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-10-24 15:23:57
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-01 16:55:06
from __future__ import print_function
import numpy as np
import tensorflow as tf


with tf.Session() as sess:
    new_saver = tf.train.import_meta_graph('best_policy.model.meta') #load graph
    for var in tf.trainable_variables(): #get the param names
        print(var.name) #print parameters' names
        new_saver.restore(sess, tf.train.latest_checkpoint('./')) #find the newest training result
        all_vars = tf.trainable_variables()
        for v in all_vars:
            v_4d = np.array(sess.run(v))


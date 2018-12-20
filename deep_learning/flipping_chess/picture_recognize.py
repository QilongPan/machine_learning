# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-12-20 16:16:41
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-12-20 16:16:57
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow.contrib.slim as slim

class Net(object):

    def __init__(self,**kwargs):
        self.mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
        self.width = int(kwargs.get('width',25))
        self.height = int(kwargs.get('height',60))
        self.channel_number = int(kwargs.get('channel_number',16))
        self.move_number = int(kwargs.get('move_number',1000))
        self.learning_rate = float(kwargs.get('learning_rate',0.01))
        self.batch_size = int(kwargs.get("batch_size",100))
        self.batch_num = int(kwargs.get("batch_num",200))
        self.model_save_path = str(kwargs.get("model_save_path",'model/'))

        self.is_training = tf.placeholder(tf.bool,[])
        self.input_states = tf.placeholder(tf.float32,shape = [None,self.width,self.height,self.channel_number])
        self.probs = tf.placeholder(tf.float32, shape=[None, self.move_number])
        self.predict_probs = self.model(self.input_states,0)

        self.global_step = tf.Variable(0, trainable=False)
        self.learning_rate = tf.train.exponential_decay(self.learning_rate, self.global_step, 100, 0.96, staircase = True)
        self.entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=self.predict_probs, labels=tf.argmax(self.probs, 1))
        self.loss = tf.reduce_mean(self.entropy)

        self.update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
        with tf.control_dependencies(self.update_ops):
            self.train_op = tf.train.AdamOptimizer(self.learning_rate).minimize(self.loss, global_step=self.global_step)

        self.prediction = tf.equal(tf.argmax(self.probs, 1), tf.argmax(self.predict_probs, 1))
        self.accuracy = tf.reduce_mean(tf.cast(self.prediction, tf.float32))

        self.sess = tf.Session()

        self.saver = tf.train.Saver()
        self.sess.run(tf.global_variables_initializer())

    def identity_block(self,input_tensor,conv_depth,kernel_shape,layer_name):
        with tf.variable_scope(layer_name):
            relu = tf.nn.relu(slim.conv2d(input_tensor,conv_depth,kernel_shape))
            outputs = tf.nn.relu(slim.conv2d(relu,conv_depth,kernel_shape) + input_tensor)
        return outputs

    def change_block(self,input_tensor,kernel_number,kernel_shape,layer_name,step_size = 2):
        with tf.variable_scope(layer_name):
            relu = tf.nn.relu(slim.conv2d(input_tensor,kernel_number,kernel_shape,stride=step_size))
            input_tensor_reshape = slim.conv2d(input_tensor,kernel_number,[1,1],stride=step_size)
            outputs = tf.nn.relu(slim.conv2d(relu,kernel_number,kernel_shape) + input_tensor_reshape)
        return outputs

    def model_2(self,input_states):
        with slim.arg_scope([slim.conv2d,slim.fully_connected],
                            activation_fn = tf.nn.tanh,
                            normalizer_fn = slim.batch_norm,
                            normalizer_params = {'is_training':self.is_training,'decay':0.95}):
            net = tf.nn.relu(slim.conv2d(input_states,32,[3,3]))
            net = self.change_block(net,64,[3,3],'layer_1')
            net = self.identity_block(net,64,[3,3],'layer_2')
            net = self.change_block(net,128,[3,3],'layer_3')
            net = self.identity_block(net,128,[3,3],'layer_4')
            net = self.change_block(net,64,[3,3],'layer_5')
            net = self.change_block(net,32,[3,3],'layer_6')
            net = slim.flatten(net,scope='flatten')
            net = slim.fully_connected(slim.dropout(net,0.8),200,activation_fn=tf.nn.tanh,scope='fc_1')
            output = slim.fully_connected(slim.dropout(net,0.8),self.move_number,activation_fn=None,scope='output_layer')
        return output
    '''
    reference vgg19,but not eexactly the same
    '''
    def model_3(self,input_states):
        with slim.arg_scope([slim.conv2d,slim.fully_connected],activation_fn = tf.nn.tanh,normalizer_fn = slim.batch_norm,normalizer_params = {'is_training':self.is_training,'decay':0.95}):
            net = tf.nn.relu(slim.conv2d(input_states,64,[3,3]))
            net = self.identity_block(net,64,[3,3],'layer_1')
            net = slim.max_pool2d(net,[2,2])

            net = self.change_block(net,128,[3,3],'layer_2',1)
            net = self.identity_block(net,128,[3,3],'layer_3')
            net = slim.max_pool2d(net,[2,2])

            net = self.change_block(net,256,[3,3],'layer_4',1)
            net = self.identity_block(net,256,[3,3],'layer_5')
            net = self.identity_block(net,256,[3,3],'layer_6')
            net = self.identity_block(net,256,[3,3],'layer_7')
            net = self.change_block(net,512,[3,3],'layer_8',2)

            net = self.identity_block(net,512,[3,3],'layer_9')
            net = self.identity_block(net,512,[3,3],'layer_10')
            net = self.identity_block(net,512,[3,3],'layer_11')
            net = slim.flatten(net,scope='flatten')
            net = slim.fully_connected(slim.dropout(net,0.8),4096,activation_fn=tf.nn.tanh,scope='fc_1')
            output = slim.fully_connected(slim.dropout(net,0.8),self.move_number,activation_fn=None,scope='output_layer')
        return output


    def model(self,input_states,index):
        if index == 0:
            return self.model_1(input_states)
        elif index == 1:
            return self.model_2(input_states)
        elif index == 2:
            return self.model_3(input_states)

    '''
    simple model
    '''
    def model_1(self,input_states):
        conv_1 = tf.nn.relu(slim.conv2d(input_states,32,[3,3]))
        pool_1 = slim.max_pool2d(conv_1,[2,2]) 
        block_1 = self.identity_block(pool_1,32,[3,3],'layer_2')
        block_2 = self.change_block(block_1,64,[3,3],'layer_3')
        block_3 = self.identity_block(block_2,64,[3,3],'layer_4')
        block_4 = self.change_block(block_3,32,[3,3],'layer_5')
        net_flatten = slim.flatten(block_4,scope='flatten')
        fc_1 = slim.fully_connected(slim.dropout(net_flatten,0.8),200,activation_fn=tf.nn.tanh,scope='fc_1')
        output = slim.fully_connected(slim.dropout(fc_1,0.8),self.move_number,activation_fn=None,scope='output_layer')
        return output

    def train(self):
        for i in range(self.batch_num):
            x_b, y_b = self.get_batch(self.batch_size)
            x_b = tf.reshape(x_b,[-1,self.width,self.height,self.channel_number]).eval(session = self.sess)
            train_op_, loss_, step = self.sess.run([self.train_op, self.loss, self.global_step], feed_dict={self.input_states: x_b, self.probs: y_b,self.is_training:True})
            if i % 1 == 0:
                print("training step {0}, loss {1}".format(step, loss_))
                x_b, y_b = self.get_test_data()
                x_b = tf.reshape(x_b,[-1,self.width,self.height,self.channel_number]).eval(session = self.sess)
                result = self.sess.run(self.accuracy, feed_dict={self.input_states: x_b, self.probs: y_b,self.is_training:False})
                print("training step {0},accuracy {1} ".format(step,result))
            self.saver.save(self.sess, self.model_save_path + 'my_model', global_step=self.global_step)

    def get_batch(self,batch_size):
        return self.mnist.train.next_batch(batch_size)

    def get_test_data(self):
        return self.mnist.test.images[:500], self.mnist.test.labels[:500]

    def restore_model(self, model_path):
        self.saver.restore(self.sess, model_path)

if __name__ == '__main__':
    net = Net(width = 28,height = 28,channel_number = 1,move_number = 10,learning_rate = 0.0001)
    net.train()
    net.sess.close()
# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-30 10:48:54
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-30 17:24:45

from game import Game
import tensorflow as tf 
import random
import numpy as np 

class SG(object):

    def __init__(self):
        self.game = Game()
        self.gamma = 0.9
        self.alpha = 0.3
        self.epsilon = 0.3
        self.iterator_number = 3000
        self.move_numbers = 4
        self.width = 4
        self.height = 4
        self.passage_number = 1

    #利用ε-greedy策略
    def epsilon_greedy(self,state):
        probs = self.prob_function(state)
        best_action_index = 0
        best_value = probs[0][0]
        for i in range(len(probs[0])):
            if best_value < probs[0][i]:
                best_value = probs[0][i]
                best_action_index = i

        probability = [0.0 for i in range(len(self.game.actions))]
        probability[best_action_index] += 1 - self.epsilon
        for i in range(len(self.game.actions)):
            probability[i] += self.epsilon / len(self.game.actions)

        random_number = random.random()
        sum_probability = 0.0
        for i in range(len(self.game.actions)):
            sum_probability += probability[i]
            if sum_probability >= random_number:
                return i
        return len(self.game.actions) - 1

    def prob_function(self,state):
        features = self.game.get_features(state)
        features = features.reshape([1,1,self.height,self.width])
        log_act_probs, value = self.session.run(
                [self.action_fc, self.evaluation_fc2],
                feed_dict={self.input_states: features}
                )
        log_act_probs = np.exp(log_act_probs)
        return log_act_probs

    def value_function(self,state,action):
        next_state = self.game.do_action(state,action)
        features = self.game.get_features(next_state)
        features = features.reshape([1,1,self.height,self.width])
        log_act_probs, value = self.session.run(
                [self.action_fc, self.evaluation_fc2],
                feed_dict={self.input_states: features}
                )
        return value

    def sg(self):
        self.input_states = tf.placeholder(tf.float32,shape = [None,self.passage_number,self.height,self.width])
        self.input_state = tf.transpose(self.input_states, [0, 2, 3, 1])
        # 2. Common Networks Layers
        #data_format:channels_last对应于具有形状（批次，高度，宽度，通道）的输入，而channels_first对应于具有形状的输入（批次，通道，高度，宽度）
        #样本数*height*width*4
        self.conv1 = tf.layers.conv2d(inputs=self.input_state,
                                      filters=32, kernel_size=[3, 3],
                                      padding="same", data_format="channels_last",
                                      activation=tf.nn.relu)
        #样本数*height*width*32
        self.conv2 = tf.layers.conv2d(inputs=self.conv1, filters=64,
                                      kernel_size=[3, 3], padding="same",
                                      data_format="channels_last",
                                      activation=tf.nn.relu)
        #样本数*height*width*64
        self.conv3 = tf.layers.conv2d(inputs=self.conv2, filters=128,
                                      kernel_size=[3, 3], padding="same",
                                      data_format="channels_last",
                                      activation=tf.nn.relu)
        #样本数*height*width*128
        # 3-1 Action Networks
        self.action_conv = tf.layers.conv2d(inputs=self.conv3, filters=4,
                                            kernel_size=[1, 1], padding="same",
                                            data_format="channels_last",
                                            activation=tf.nn.relu)
        #样本数*height*width*4
        # Flatten the tensor
        self.action_conv_flat = tf.reshape(
                self.action_conv, [-1, 4 * self.width * self.height])
        # 3-2 Full connected layer, the output is the log probability of moves
        # on each slot on the board
        self.action_fc = tf.layers.dense(inputs=self.action_conv_flat,
                                         units=self.move_numbers,
                                         activation=tf.nn.log_softmax)
        # 4 Evaluation Networks
        self.evaluation_conv = tf.layers.conv2d(inputs=self.conv3, filters=2,
                                                kernel_size=[1, 1],
                                                padding="same",
                                                data_format="channels_last",
                                                activation=tf.nn.relu)
        self.evaluation_conv_flat = tf.reshape(
                self.evaluation_conv, [-1, 2 * self.width * self.height])
        self.evaluation_fc1 = tf.layers.dense(inputs=self.evaluation_conv_flat,
                                              units=64, activation=tf.nn.relu)
        # output the score of evaluation on current state
        self.evaluation_fc2 = tf.layers.dense(inputs=self.evaluation_fc1,
                                              units=1, activation=tf.nn.tanh)

        # Define the Loss function
        # 1. Label: the array containing if the game wins or not for each state
        self.labels = tf.placeholder(tf.float32, shape=[None, 1])
        # 2. Predictions: the array containing the evaluation score of each state
        # which is self.evaluation_fc2
        # 3-1. Value Loss function
        self.value_loss = tf.losses.mean_squared_error(self.labels,
                                                       self.evaluation_fc2)
        # 3-2. Policy Loss function
        self.mcts_probs = tf.placeholder(
                tf.float32, shape=[None, self.move_numbers])
        self.policy_loss = tf.negative(tf.reduce_mean(
                tf.reduce_sum(tf.multiply(self.mcts_probs, self.action_fc), 1)))
        # 3-3. L2 penalty (regularization)
        l2_penalty_beta = 1e-4
        vars = tf.trainable_variables()
        l2_penalty = l2_penalty_beta * tf.add_n(
            [tf.nn.l2_loss(v) for v in vars if 'bias' not in v.name.lower()])
        # 3-4 Add up to be the Loss function
        self.loss = self.value_loss + self.policy_loss + l2_penalty

        # Define the optimizer we use for training
        self.learning_rate = tf.placeholder(tf.float32)
        self.optimizer = tf.train.AdamOptimizer(
                learning_rate=self.learning_rate).minimize(self.loss)

        # Make a session
        self.session = tf.Session()

        # calc policy entropy, for monitoring only
        self.entropy = tf.negative(tf.reduce_mean(
                tf.reduce_sum(tf.exp(self.action_fc) * self.action_fc, 1)))
        # Initialize variables
        init = tf.global_variables_initializer()
        self.session.run(init)

        for i in range(self.iterator_number):
            state = self.game.states[random.randint(1,len(self.game.states) - 2)]
            action_index = random.randint(0,len(self.game.actions) - 1)
            move_number = 0
            while not self.game.is_end(state) and move_number < 50:
                next_state = self.game.do_action(state,self.game.actions[action_index])
                if next_state == 0 or next_state == 15:
                    reward = 1
                else:
                    reward = 0
                state_features = self.game.get_features(next_state)
                probs = self.prob_function(next_state)
                #取得最好的下一状态，采用greedy策略
                best_value = self.value_function(next_state,self.game.actions[0])[0]
                for j in range(len(self.game.actions)):
                    value = self.value_function(next_state,self.game.actions[j])[0]
                    if value > best_value:
                        best_value = value
                next_reward = reward + self.gamma * best_value

                self.session.run([self.loss, self.entropy, self.optimizer],
                feed_dict={self.input_states: state_features,
                           self.mcts_probs: probs,
                           self.labels: [next_reward],
                           self.learning_rate: 0.03})
                state = next_state
                #走步策略采用ε-greedy策略
                action_index = self.epsilon_greedy(next_state)
                move_number += 1

if __name__ == "__main__":
    test = SG()
    test.sg()
    for i in range(len(test.game.states)):
        probs = test.prob_function(test.game.states[i])
        print(probs)
    test.session.close()

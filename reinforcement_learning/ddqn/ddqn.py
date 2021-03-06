# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-28 13:05:40
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-12-14 10:13:27

from game import Game
import tensorflow as tf 
import random
import numpy as np 

class DDqn(object):

    def __init__(self):
        self.game = Game()
        self.gamma = 0.9
        self.alpha = 0.3
        self.epsilon = 0.1
        self.iterator_number = 2000

    #利用ε-greedy策略
    def epsilon_greedy(self,state):
        best_action_index = 0
        best_value = self.value_function(state,self.game.actions[0])[0]
        best_value = float("-inf")

        for i in range(len(self.game.actions)):
            if best_value < self.value_function(state,self.game.actions[i])[0]:
                best_value = self.value_function(state,self.game.actions[i])[0]
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

    def value_function(self,state,action):
        next_state = self.game.do_action(state,action)
        features = self.game.get_features(next_state)
        features = np.array([features])
        features = features.reshape([1,16])
        return self.sess.run(self.predict_y,feed_dict={self.input_x:np.array(features)})

    def value_function2(self,state,action):
        next_state = self.game.do_action(state,action)
        features = self.game.get_features(next_state)
        features = np.array([features])
        features = features.reshape([1,16])
        return self.sess.run(self.predict_y2,feed_dict={self.input_x:np.array(features)})

    def ddqn(self):
        #地图每个位置表示一个特征，机器人所在位置为1，其余位置为0
        self.input_x = tf.placeholder(tf.float32,shape = [None,len(self.game.states)],name = 'input_name')
        #输出4个值分别为该状态采取4种行动的回报
        self.input_action_assessment = tf.placeholder(tf.float32,shape = [None,1],name = "action_assessment")

        self.input_operate_value = tf.placeholder(tf.float32,shape = [None,1],name = "operate_value")

        self.w = tf.Variable(tf.random_normal([len(self.game.states),1]))
        self.w2 = tf.Variable(tf.random_normal([len(self.game.states),1]))
        self.b = tf.Variable(tf.zeros([1]) + 0.1)
        self.b2 = tf.Variable(tf.zeros([1]) + 0.1)
        self.predict_y = tf.matmul(self.input_x,self.w) + self.b
        self.predict_y2 = tf.matmul(self.input_x,self.w2) +self.b2
        
        self.loss1 = tf.reduce_mean(tf.square(self.predict_y - self.input_action_assessment))
        self.loss2 = tf.reduce_mean(tf.square(self.predict_y2 - self.input_operate_value))

        self.loss = self.loss1 + self.loss2
        self.optimizer = tf.train.GradientDescentOptimizer(0.03)
        self.train = self.optimizer.minimize(self.loss)
        self.init = tf.global_variables_initializer()
        self.sess = tf.Session()
        self.sess.run(self.init)

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
                #取得最好的下一状态，采用greedy策略
                best_value = self.value_function2(next_state,self.game.actions[0])[0]
                for j in range(len(self.game.actions)):
                    value = self.value_function2(next_state,self.game.actions[j])[0]
                    if value > best_value:
                        best_value = value
                next_reward = reward + self.gamma * best_value
                self.sess.run(self.train,feed_dict = {self.input_x:[np.array(state_features)],
                    self.input_action_assessment:[next_reward],self.input_operate_value:[best_value]})
                state = next_state
                #走步策略采用ε-greedy策略
                action_index = self.epsilon_greedy(next_state)
                move_number += 1

if __name__ == "__main__":
    ddn = DDqn()
    ddn.ddqn()
    for i in range(len(ddn.game.states)):
        current_index = 0
        current = ddn.value_function(ddn.game.states[i],ddn.game.actions[0])[0][0]
        for j in range(len(ddn.game.actions)):
            value = ddn.value_function(ddn.game.states[i],ddn.game.actions[j])[0][0]
            if value > current:
                current_index = j
        print("current state %d ,best action %d"%(i,current_index))
    ddn.sess.close()
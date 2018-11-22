import random
from game import Game
import numpy as np 
'''
在更新St的动作值函数需要St+1的动作值函数，Sarsa用的是e-greedy方法，和选择St下的动作一样；
而Q-learning是用的greedy方法和选择St下动作不一样，因此称为off-policy
'''
class Sarsa(object):

    def __init__(self):
        self.game = Game()
        self.iterator_number = 1000
        self.alpha = 0.01
        self.theta = [0.0 for i in range(16)]
        self.theta = np.array(self.theta)
        self.theta = np.transpose(self.theta)


    #利用ε-greedy策略
    def epsilon_greedy(self,state,epsilon):
        best_action_index = 0
        best_value = self.value_function(state,0)
        for i in range(len(self.game.actions)):
            if best_value < self.value_function(state,i):
                best_value = self.value_function(state,i)
                best_action_index = i

        probability = [0.0 for i in range(len(self.game.actions))]
        probability[best_action_index] += 1 - epsilon
        for i in range(len(self.game.actions)):
            probability[i] += epsilon / len(self.game.actions)

        random_number = random.random()
        sum_probability = 0.0
        for i in range(len(self.game.actions)):
            sum_probability += probability[i]
            if sum_probability >= random_number:
                return i
        return len(self.game.actions) - 1

    def get_feature(self,state):
        #局面表示为one-hot向量 当前状态位置置为1
        return_feature = np.array([0.0 for i in range(len(self.theta))])
        return_feature[state] = 1.0
        return return_feature

    def value_function(self,state,action):
        next_state = self.game.do_action(state,action)
        return np.dot(self.get_feature(next_state),self.theta)


    def update(self,state,action_index,true_value,alpha):
        pre_value = self.value_function(state,self.game.actions[action_index])
        error_value = pre_value - true_value
        feature = self.get_feature(state)
        self.theta -= alpha * error_value *feature

    def sarsa(self,epsilon):
        for i in range(len(self.theta)):
            self.theta[i] = 0.1
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
                #选择St和找St+1的动作函数都是采用的ε-greedy策略
                next_action_index = self.epsilon_greedy(next_state,epsilon)
                self.update(state,action_index,reward + self.game.gamma * self.value_function(next_state,next_action_index),self.alpha)
                state = next_state
                action_index = next_action_index
                move_number += 1


if __name__ == '__main__':
    sar = Sarsa()
    sar.sarsa(0.5)
    for i in range(len(sar.game.states)):
        for j in range(len(sar.game.actions)):
            print(round(sar.value_function(sar.game.states[i],sar.game.actions[j]),1),end = "     ")
        print()
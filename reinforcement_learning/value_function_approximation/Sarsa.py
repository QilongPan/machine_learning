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
        self.iterator_number = 3000
        self.alpha = 0.01
        #每一个位置表示特征，分别为x0,x1,x2,x3,x4,x5,x6,x7
        #每一个位置的参数为theta，分别为theta0,theta1,theta2,theta3,theta4,theta5,theta6,theta7
        #值函数的计算方式为h(x) = x0*theta0+x1*theta1+x2*theta2+x3*theta3+x4*theta4+x5*theta5+x6*theta6+x7*theta7
        #损失函数为1/2(h(x)-y)*(h(x)-y) 线性回归的最小二乘法公式（最小平方）
        self.theta = [0.0 for i in range(8)]

    #利用ε-greedy策略
    def epsilon_greedy(self,state,epsilon):
        best_action_index = 0
        best_value = self.value_function(state,self.game.actions[0])
        for i in range(len(self.game.actions)):
            if best_value < self.value_function(state,self.game.actions[i]):
                best_value = self.value_function(state,self.game.actions[i])
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
        #局面特征表示为one-hot向量 机器人所在的位置为1，其余位置为0
        return_feature = np.array([0.0 for i in range(len(self.theta))])
        return_feature[state] = 1.0
        return return_feature

    #值函数计算
    def value_function(self,state,action):
        next_state = self.game.do_action(state,action)
        feature = self.get_feature(next_state)
        value = 0.0
        for i in range(len(self.theta)):
            value += feature[i] * self.theta[i]
        return value
    #反向传播
    def update(self,state,action_index,true_value,alpha):
        pre_value = self.value_function(state,self.game.actions[action_index])
        #要是损失函数的值最小，则对损失函数求导为 1/2 * 2 * Xi  alpha为学习率
        error_value = pre_value - true_value
        feature = self.get_feature(state)
        for i in range(len(self.theta)):
            self.theta[i] += alpha * error_value * feature[i]

    def sarsa(self,epsilon):
        for i in range(self.iterator_number):
            state = self.game.states[random.randint(1,len(self.game.states) - 2)]
            action_index = random.randint(0,len(self.game.actions) - 1)
            move_number = 0
            while not self.game.is_end(state) and move_number < 50:
                next_state = self.game.do_action(state,self.game.actions[action_index])
                if next_state == 0 or next_state == 7:
                    reward = 1
                else:
                    reward = 0
                #选择St和找St+1的动作函数都是采用的ε-greedy策略
                next_action_index = self.epsilon_greedy(next_state,epsilon)
                next_reward = reward + self.game.gamma * self.value_function(next_state,self.game.actions[next_action_index])
                self.update(state,action_index,next_reward,self.alpha)
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
    print(sar.theta)
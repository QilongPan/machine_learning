# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-20 13:20:56
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-20 13:51:19

from game import Game

'''
策略迭代算法:包括策略评估和策略改善两个步骤
'''
class Policy_Value(object):

    def __init__(self):
        self.gam = Game()
        self.values = [0.0 for i in range(len(self.gam.states))]
        self.pi = dict()
        for state in self.gam.states:
            if state == 0 or state == 15:
                continue
            self.pi[state] = self.gam.actions[0]
        self.iteration_times = 10000

    #策略评估
    def policy_evaluate(self):
        #保证值函数收敛到该策略所对应的真实值函数
        for i in range(1000):
            #扫描整个状态空间
            for state in self.gam.states:
                if state == 0 or state == 15:
                    continue
                action = self.pi[state]
                next_state,r = self.gam.do_action(state,action)
                self.values[state] = r + self.gam.gamma * self.values[next_state]

    def policy_improve(self):
        for state in self.gam.states:
            if state == 0 or state == 15:
                continue
            action = self.gam.actions[0]
            next_state,r = self.gam.do_action(state,action)
            value = r + self.gam.gamma * self.values[next_state]
            for act in self.gam.actions:
                next_state,r = self.gam.do_action(state,act)
                if value < r + self.gam.gamma * self.values[next_state]:
                    action = act 
                    value = r + self.gam.gamma * self.values[next_state]
            self.pi[state] = action

    def policy_iteration(self):
        for i in range(100):
            self.policy_evaluate()
            self.policy_improve()

if __name__ == "__main__":
    policy_value = Policy_Value()
    policy_value.policy_iteration()
    for i in range(len(policy_value.values)):
        print(round(policy_value.values[i],1),end = "   ")
        if i == 3 or i == 7 or i == 11 or i == 15:
            print()
# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-20 11:52:58
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-20 13:52:19

from game import Game

'''
值函数迭代算法:在评估一次之后就进行策略改善
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

    def value_iteration(self):
        for i in range(self.iteration_times):
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
                self.values[state] = value 

if __name__ == "__main__":
    policy_value = Policy_Value()
    policy_value.value_iteration()
    for i in range(len(policy_value.values)):
        print(round(policy_value.values[i],1),end = "   ")
        if i == 3 or i == 7 or i == 11 or i == 15:
            print()
# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-20 14:39:59
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-20 15:34:10

from game import Game 
import random

'''
该蒙特卡罗是采用异策略实现的
on-policy(同策略):探索策略(行动策略)和评估策略是同一个策略。即产生数据的策略与评估和要改善的策略是同一个策略
off-policy(异策略):产生数据的策略与评估和改善的策略不是同一个策略
'''
class MonteCarlo(object):

    def __init__(self):
        self.game = Game()
        self.gamma = 0.8
        self.simulations = 10000
        self.visits = [0 for i in range(len(self.game.states))]
        self.values = [0 for i in range(len(self.game.states))]
        self.values[0] = 1
        self.values[15] = 1
        self.pi = dict()
        for state in self.game.states:
            if state == 0 or state == 15:
                continue
            self.pi[state] = self.game.actions[0]

    def mc_method(self):
        current_simulations = 0
        while current_simulations < self.simulations:
            #随机产生初始状态，不产生结束状态 行动策略
            start_state = random.randint(1,len(self.game.states) - 2)
            sequence = self.game.simulation(start_state)
            current_simulations += 1
            value = 0
            decay_factor = 1
            #通过马尔科夫链更新状态值
            for j in range(len(sequence)-2,-1,-1):
                self.visits[sequence[j]] += 1
                reward = 0
                #到达终点奖励为1,否则没奖励
                if sequence[j+1] == 0 or sequence[j+1] == 15:
                    reward = 1
                value = reward + decay_factor * value
                self.values[sequence[j]] += value
                decay_factor *=  self.gamma
        #求状态值期望(平均值)
        for j in range(len(self.game.states)):
            if self.visits[j] > 0:
                self.values[j] = self.values[j] / self.visits[j]

    #根据值函数更新策略 改善策略采用的是最大值策略
    def policy_improve(self):
        for i in range(len(self.game.states)):
            if i == 0 or i == 15:
                continue
            max_value = self.values[self.game.states[i]]
            for j in range(len(self.game.actions)):
                next_state = self.game.do_action(self.game.states[i],self.game.actions[j])
                if self.values[next_state] > max_value:
                    self.pi[self.game.states[i]] = self.game.actions[j]
                    max_value = self.values[next_state]

if __name__ == "__main__":
    mc = MonteCarlo()
    mc.mc_method()
    mc.policy_improve()
    for i in range(len(mc.values)):
        print(round(mc.values[i],1),end = "   ")
        if i == 3 or i == 7 or i == 11 or i == 15:
            print()
    for key,value in mc.pi.items():
        print("{key}:{value}".format(key = key,value = value))
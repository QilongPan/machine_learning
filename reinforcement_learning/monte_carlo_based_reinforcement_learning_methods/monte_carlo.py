# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-20 14:39:59
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-20 15:01:38

from game import Game 
import random

class MonteCarlo(object):

    def __init__(self):
        self.game = Game()
        self.gamma = 0.8
        self.simulations = 10000
        self.visits = [0 for i in range(len(self.game.states))]
        self.values = [0 for i in range(len(self.game.states))]
        self.values[0] = 1
        self.values[15] = 1

    def mc_method(self):
        current_simulations = 0
        while current_simulations < self.simulations:
            #随机产生初始状态，不产生结束状态
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

if __name__ == "__main__":
    mc = MonteCarlo()
    mc.mc_method()
    for i in range(len(mc.values)):
        print(round(mc.values[i],1),end = "   ")
        if i == 3 or i == 7 or i == 11 or i == 15:
            print()
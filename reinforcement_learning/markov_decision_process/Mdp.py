# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-19 14:48:35
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-19 20:33:13


'''
机器人找金币例子
0 1 2 3 4
5   6   7
该网格一共有8个状态，其中状态5和状态7是死亡区域，状态7是金币区域。机器人的初始位置为网格世界中的任意一个状态，
机器人从初始状态出发寻找金币，机器人每探索一次，进入死亡区域或找到金币，本次探索结束
'''

import random

class Mdp(object):

    def __init__(self):
        #S
        self.states = [0,1,2,3,4,5,6,7]
        #A
        self.actions = ['up','down','left','right']
        #P 每一行分别表示每个状态采取每个动作的概率
        self.probability = [
            [0,0.5,0,0.5],
            [0,0,0.5,0.5],
            [0,0.34,0.33,0.33],
            [0,0,0.5,0.5],
            [0,0.5,0.5,0],
            [0.25,0.25,0.25,0.25],
            [0.25,0.25,0.25,0.25],
            [0.25,0.25,0.25,0.25]
        ]
        # R 每一行表示每个状态对应动作的回报
        self.rewards = []
        for i in range(len(self.states)):
            reward = [0,0,0,0]
            self.rewards.append(reward)
        self.rewards[0][1] = -1
        self.rewards[2][1] = 1
        self.rewards[4][1] = -1

        #折扣因子
        self.gamma = 0.8
        #每个状态的初始值
        self.values = [0.0 for i in range(len(self.states))]
        #记录每个状态的访问次数
        self.visits = [0.0 for i in range(len(self.states))]
        #当前状态
        self.state = None
        #产生序列数量
        self.state_sequence_number = 10000

    def is_end(self):
        if self.state == 5 or self.state == 6 or self.state == 7:
            return True
        else:
            return False

    def get_next_state_random(self):
        random_number = random.uniform(0, 1)
        if random_number >= 0 and random_number < self.probability[self.state][0]:
            return 0
        elif random_number >= self.probability[self.state][0] and random_number < (self.probability[self.state][0] + self.probability[self.state][1]):
            return 1
        elif random_number >= (self.probability[self.state][0] + self.probability[self.state][1]) and random_number < (self.probability[self.state][0] + self.probability[self.state][1]+ self.probability[self.state][2]):
            return 2
        else:
            return 3

    def do_action(self):
        action_index = self.get_next_state_random()
        action = self.actions[action_index]
        last_state = self.state
        if self.state == 0:
            if action == "down":
                self.state = 5
            elif action =="right":
                self.state = 1
            else:
                self.state = 0
        elif self.state == 1:
            if action == "left":
                self.state = 0
            elif action == "right":
                self.state = 2
            else:
                self.state = 1
        elif self.state == 2:
            if action == "down":
                self.state = 6
            elif action == "left":
                self.state = 1
            elif action == "right":
                self.state = 3
            else:
                self.state = 2
        elif self.state == 3:
            if action == "left":
                self.state = 2
            elif action == "right":
                self.state = 4
            else:
                self.state = 3
        elif self.state == 4:
            if action == "down":
                self.state = 7
            elif action == "left":
                self.state = 3
            else:
                self.state = 4
        else:
            print("end!")

    #模拟到终点
    def simulation(self):
        sequence = [self.state]
        #使其最多能走50步，如果还未到终点则强制结束
        move_number = 0
        while not self.is_end() and move_number < 50:
            self.do_action()
            sequence.append(self.state)
            move_number = move_number + 1
        return sequence

    def calculate_state_value(self):
        for i in range(self.state_sequence_number):
            self.state = random.randint(0,4)
            #得到一条状态序列(马尔可夫链)
            sequence = self.simulation()
            value = 0
            decay_factor = 1
            #通过马尔科夫链更新状态值
            for j in range(len(sequence)-2,-1,-1):
                self.visits[sequence[j]] = self.visits[sequence[j]] + 1
                value = self.get_reward(sequence[j],sequence[j+1]) + decay_factor * value
                self.values[sequence[j]] = self.values[sequence[j]] + value
                decay_factor = decay_factor * self.gamma
        #求状态值期望(平均值)
        for j in range(len(self.states)-3):
            if self.visits[j] > 0:
                self.values[j] = self.values[j] / self.visits[j]

    #得到状态采取动作的回报
    def get_reward(self,state,next_state):
        if state == next_state:
            return 0
        #move left
        elif state == next_state + 1:
            return self.rewards[state][2]
        #move right
        elif state == next_state - 1:
            return self.rewards[state][3]
        #move down
        elif state == 0 and next_state == 5:
            return self.rewards[state][1]
        elif state == 2 and next_state == 6:
            return self.rewards[state][1]
        elif state == 4 and next_state == 7:
            return self.rewards[state][1]
        return 0
    
if __name__ == "__main__":
    mdp = Mdp()
    mdp.calculate_state_value()
    print(mdp.values)



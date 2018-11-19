# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-19 14:48:35
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-19 20:33:13

import random

class Mdp(object):

    def __init__(self):
        self.states = [0,1,2,3,4,5,6,7]
        self.actions = ['up','down','left','right']
        self.probability = [
            [0.25,0.25,0.25,0.25],
            [0.25,0.25,0.25,0.25],
            [0.25,0.25,0.25,0.25],
            [0.25,0.25,0.25,0.25]
        ]


        '''
        rewards为二维数组，第一维表示每个状态，第二维表示每个动作，
        其中的值表示状态采取某个动作所获得的回馈
        '''
        self.rewards = []
        for i in range(len(self.states)):
            reward = [0,0,0,0]
            self.rewards.append(reward)
        self.rewards[0][1] = -1
        self.rewards[2][1] = 1
        self.rewards[4][1] = -1

        self.gamma = 0.8
        #每个状态的初始值
        self.values = [0.0 for i in range(len(self.states))]
        #记录每个状态的访问次数
        self.visits = [0.0 for i in range(len(self.states))]

        self.state = None

        self.state_sequence_number = 1000
    def step(self,state,action):
        pass

    def is_end(self):
        if self.state == 5 or self.state == 6 or self.state == 7:
            return True
        else:
            return False


    def do_action(self):
        action_index = random.randint(0,len(self.actions) - 1)
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
        return self.rewards[last_state][action_index]

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
        for i in range(1):
            self.state = random.randint(0,4)
            sequence = self.simulation()
            for j in range(len(sequence)):
                pass
        return 0


if __name__ == "__main__":
    mdp = Mdp()
    print(mdp.calculate_state_value())





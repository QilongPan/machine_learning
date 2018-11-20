# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-20 11:30:36
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-20 13:46:15

'''
走迷宫例子
0  1  2  3 
4  5  6  7
8  9  10 11
12 13 14 15

0和15为迷宫出口，机器人的起始位置是随机的
'''

class Game(object):

    def __init__(self):
        self.states = range(16)
        self.actions = ['up','down','left','right']
        #所有动作的报酬都为-1，机器人越早出迷宫越好
        self.rewards = -1
        self.gamma = 0.8

    def do_action(self,state,action):
        #到达终点，reward 为0,其余状态为-1
        if state == 0 or state == 15:
            return True,state,0
        if action == 'up':
            next_state = state - 4
        elif action == 'down':
            next_state = state + 4
        elif action == 'left':
            next_state = state - 1
        elif action == 'right':
            next_state = state + 1
        if next_state < 0 or next_state > 15:
            next_state = state
        if next_state == 0 or next_state == 15:
            return next_state,-1
        return next_state,-1



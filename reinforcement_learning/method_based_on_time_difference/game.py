# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-20 15:35:47
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-20 18:47:08


'''
走迷宫例子
0  1  2  3 
4  5  6  7
8  9  10 11
12 13 14 15

0和15为迷宫出口，机器人的起始位置是随机的
'''
import random

class Game(object):

    def __init__(self):
        self.states = range(16)
        self.actions = ['up','down','left','right']
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
            return next_state
            
        if state == 3 and next_state == 4:
            return state
        elif state == 4 and next_state == 3:
            return state
        elif state == 7 and next_state == 8:
            return state
        elif state == 8 and next_state == 7:
            return state
        elif state == 11 and next_state == 12:
            return state
        elif state == 12 and next_state == 11:
            return state

        return next_state

    def is_end(self,state):
        if state == 0 or state == 15:
            return True
        else:
            return False

    '''
    出迷宫奖励为0，没出动作为-1
    '''
    def get_reward(self,state,action):
        if state == 1:
            if action == 'left':
                return 0
        elif state == 4:
            if action == 'up':
                return 0
        elif state == 11:
            if action == 'down':
                return 0
        elif state == 14:
            if action == 'right':
                return 0
        return -1


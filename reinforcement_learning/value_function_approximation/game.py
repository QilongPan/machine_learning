# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-20 14:23:01
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-22 16:04:14

'''
走迷宫例子
0  1  2  3 
4  5  6  7
0和7为迷宫出口，机器人的起始位置是随机的
'''
import random
import numpy as np 

class Game(object):

    def __init__(self):
        self.states = range(8)
        self.actions = ['up','down','left','right']
        self.gamma = 0.8

    def do_action(self,state,action):
        #到达终点，reward 为0,其余状态为-1
        if state == 0 or state == 7:
            return state 
        elif state == 1:
            if action == 'up':
                return 1
            elif action == 'down':
                return 5
            elif action == 'left':
                return 0
            elif action == 'right':
                return 2
            else:
                print("error action" + action)
        elif state == 2:
            if action == 'up':
                return 2
            elif action == 'down':
                return 6
            elif action == 'left':
                return 1
            elif action == 'right':
                return 3
            else:
                print("error action" + action)
        elif state == 3:
            if action == 'up':
                return 3
            elif action == 'down':
                return 7
            elif action == 'left':
                return 2
            elif action == 'right':
                return 3
            else:
                print("error action" + action)
        elif state == 4:
            if action == 'up':
                return 0
            elif action == 'down':
                return 4
            elif action == 'left':
                return 4
            elif action == 'right':
                return 5
            else:
                print("error action" + action)
        elif state == 5:
            if action == 'up':
                return 1
            elif action == 'down':
                return 5
            elif action == 'left':
                return 4
            elif action == 'right':
                return 6
            else:
                print("error action" + action)
        elif state == 6:
            if action == 'up':
                return 2
            elif action == 'down':
                return 6
            elif action == 'left':
                return 5
            elif action == 'right':
                return 7
            else:
                print("error action" + action)
        else:
            print("error state" + state)

    def is_end(self,state):
        if state == 0 or state == 7:
            return True
        else:
            return False


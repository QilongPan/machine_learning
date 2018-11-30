# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-30 10:34:07
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-30 16:40:35

'''
走迷宫例子
0  1  2  3 
4  5  6  7
8  9  10 11
12 13 14 15
0和15为迷宫出口，机器人的起始位置是随机的
'''
import random
import numpy as np 

class Game(object):

    def __init__(self):
        self.states = range(16)
        self.actions = ['up','down','left','right']
        self.width = 4
        self.height = 4

    def do_action(self,state,action):
        #到达终点，reward 为0,其余状态为-1
        if state == 0 or state == 15:
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
                return 8
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
                return 9
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
                return 10
            elif action == 'left':
                return 5
            elif action == 'right':
                return 7
            else:
                print("error action" + action)
        elif state == 7:
            if action == "up":
                return 3
            elif action == 'down':
                return 11
            elif action == 'left':
                return 6
            elif action == 'right':
                return 7
            else:
                print("error action" + action)
        elif state == 8:
            if action == "up":
                return 4
            elif action == 'down':
                return 12
            elif action == 'left':
                return 8
            elif action == 'right':
                return 9
            else:
                print("error action" + action)        
        elif state == 9:
            if action == "up":
                return 5
            elif action == 'down':
                return 13
            elif action == 'left':
                return 8
            elif action == 'right':
                return 10
            else:
                print("error action" + action)        
        elif state == 10:
            if action == "up":
                return 6
            elif action == 'down':
                return 14
            elif action == 'left':
                return 9
            elif action == 'right':
                return 11
            else:         
                print("error action" + action)   
        elif state == 11:
            if action == "up":
                return 7
            elif action == 'down':
                return 15
            elif action == 'left':
                return 10
            elif action == 'right':
                return 11
            else:    
                print("error action" + action)        
        elif state == 12:
            if action == "up":
                return 8
            elif action == 'down':
                return 12
            elif action == 'left':
                return 12
            elif action == 'right':
                return 13
            else:         
                print("error action" + action)   
        elif state == 13:
            if action == "up":
                return 9
            elif action == 'down':
                return 13
            elif action == 'left':
                return 12
            elif action == 'right':
                return 14
            else:            
                print("error action" + action)
        elif state == 14:
            if action == "up":
                return 10
            elif action == 'down':
                return 14
            elif action == 'left':
                return 13
            elif action == 'right':
                return 15
            else:       
                print("error action" + action)     
        else:
            print("error state" + state)

    def get_features(self,state):
        features = np.zeros((1,1,self.height,self.width))
        features[0][0][state // 4][state % 4] = 1.0
        return features

    def is_end(self,state):
        if state == 0 or state == 15:
            return True
        else:
            return False
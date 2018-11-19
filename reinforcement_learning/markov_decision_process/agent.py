# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-19 13:22:27
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-19 20:34:43

class Agent(object):
    def __init__(self):
        self.actions = ['up','down','left','right']


class Env(object):
    def __init__(self):
        self.states = [1,2,3,4,5,6,7,8]
        
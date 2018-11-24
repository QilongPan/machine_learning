# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-24 13:52:19
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-24 13:55:08

'''
储存牌的容器
'''
class CardContainer(object):
    
    def __init__(self):
        self.cardsNumber = 0
        self.cards = {}

    def init_card_container(self,cards):
        self.cardsNumber = len(cards)
        self.cards = cards
# -*- coding: utf-8 -*-
# @Date    : 2019-04-11 18:50:06
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com

class Config(object):

    def __init__(self):
        #牌的张数
        self.__card_num = 52
        #使用0-51表示52张扑克牌(不存在大小王)
        self.__cards = [card for card in range(self.__card_num)]
        #小盲注
        #大盲注

    @property
    def card_num(self):
        return self.__card_num

    @property
    def cards(self):
        return self.__cards


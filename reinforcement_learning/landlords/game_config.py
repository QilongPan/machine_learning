# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-24 11:33:03
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-26 10:13:58

from __future__ import print_function

class GameConfig(object):

    def __init__(self):
        self.valid_card_names = ['3','4','5','6','7','8']
        self.valid_card_values = [0,1,2,3,4,5]
        self.cards = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
        self.cards_number = 24
        self.deal_card_number = 8
        self.player_number = 3
        self.pass_move = 18
        self.players = []
        for i in range(self.player_number):
            self.players.append(i)

    def is_valid_card_names(self,card_names):
        for card_name in card_names:
            if not self.is_valid_card_name(card_name):
                return False
        return True

    def is_valid_card_name(self,card_name):
        if card_name in self.valid_card_names:
            return True
        else:
            return False

    def get_card_value_by_card_name(self,card_name):
        try:
            return self.valid_card_values[self.valid_card_names.index(card_name)]
        except Exception as e:
            return -1

    def get_card_values_by_card_names(self,card_names):
        card_values = []
        for card_name in card_names:
            card_value = self.get_card_value_by_card_name(card_name)
            if card_value != -1:
                card_values.append(card_value)
            else:
                return card_values,False
        return card_values,True

    def get_cards_type_by_move(self,move):
        if move >= 0 and move <= 5:
            return 0
        elif move >= 6 and move <= 11:
            return 1
        elif move >= 12 and move <= 17:
            return 2
        return -1

    def get_moves_by_hand_cards(self,card_number,meet_move):
        if meet_move == self.pass_move:
            return self.get_moves_by_card_number_activate(card_number)
        else:
            return self.get_moves_by_card_number_passive(card_number,meet_move)

    def get_moves_by_card_number_activate(self,card_number):
        moves = []
        for i in card_number:
            if card_number[i] >= 1:
                moves.append(i)
            if card_number[i] >= 2:
                moves.append(i+ 6)
            if card_number[i] >= 3:
                moves.append(i+ 12)
        moves = sorted(moves)
        return moves

    def get_moves_by_card_number_passive(self,card_number,meet_move):
        moves = []
        cards_type = self.get_cards_type_by_move(meet_move)
        cards_value = None
        card_count = None
        add_value = None
        if cards_type == 0:
            cards_value = meet_move
            card_count = 1
            add_value = 0
        elif cards_type == 1:
            cards_value = meet_move - 6
            card_count = 2
            add_value = 6
        elif cards_type == 2:
            cards_value = meet_move - 12
            card_count = 3
            add_value = 12
        for i in range(cards_value+1,len(self.valid_card_values)):
            if card_number[i] >= card_count:
                moves.append(i + add_value )
        moves.append(self.pass_move)
        moves = sorted(moves)
        return moves

    def get_card_value(self,card):
        if card == 53:
            return 14
        else:
            return card // 4

    def init_player_every_card_number_zero(self):
        card_number = {}
        for i in self.valid_card_values:
            card_number[i] = 0
        return card_number

    def get_cards_type(self,cards):
        cards = sorted(cards)
        if len(cards) == 1:
            return 0
        elif len(cards) == 2 and self.get_card_value(cards[0]) == self.get_card_value(cards[1]):
            return 1
        elif len(cards) == 3 and self.get_card_value(cards[0]) == self.get_card_value(cards[2]):
            return 2
        return -1

    def get_cards_value(self,cards,cards_type):
        if cards_type == 0 or cards_type == 1 or cards_type == 2:
            return self.get_card_value(cards[0])

    def get_move_by_cards(self,cards):
        if len(cards) == 0:
            return self.pass_move
        cards_type = self.get_cards_type(cards)
        cards_value = self.get_cards_value(cards,cards_type)
        #单牌
        if cards_type == 0:
            dic = {0:0,1:1,2:2,3:3,4:4,5:5}
        elif cards_type == 1:
            dic = {0:6,1:7,2:8,3:9,4:10,5:11}
        elif cards_type == 2:
            dic = {0:12,1:13,2:14,3:15,4:16,6:17}
        return dic[cards_value]

    def get_card_name(self,card):
        card_value = self.get_card_value(card)
        return self.valid_card_names[card_value]

    def get_card_names_by_cards(self,cards):
        card_names = []
        for card in cards:
            card_value = self.get_card_value(card)
            card_names.append(self.valid_card_names[card_value])
        return card_names
        
    def get_before_player(self,player):
        if player == 0:
            return self.player_number - 1
        else:
            return player - 1
    def get_after_player(self,player):
        return (player + 1) % self.player_number

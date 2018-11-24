# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-24 11:31:57
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-24 15:35:26
from __future__ import print_function
from copy import deepcopy
import numpy as np

class Board(object):

    def __init__(self,config,**kwargs):
        self.player_number =  config.player_number
        self.players = config.players
        self.deal_card_number = config.deal_card_number
        self.config = config

    def init_board(self, start_player=0):
        self.current_player = self.players[start_player]
        self.players_hand_cards = {}
        self.deal_cards()
        self.players_every_card_number = {}
        self.init_player_every_card_number()
        self.last_move = self.config.pass_move
        self.meet_move = self.config.pass_move
        self.meet_move_player = self.current_player
        self.meet_cards = []
        self.pass_number = 0
        self.states = []
        self.already_played_cards = []
        self.last_play_card_player = self.current_player
        self.availables = self.config.get_moves_by_hand_cards(self.players_every_card_number[self.current_player],self.meet_move)

    def get_cards_by_card_values(self,card_values,player_id):
        play_cards = deepcopy(self.players_hand_cards[player_id])
        visits = np.zeros(len(play_cards),dtype = int)
        cards = []
        for value in card_values:
            for i in range(len(play_cards)):
                card = play_cards[i]
                card_value = self.config.get_card_value(card)
                if card_value == value and visits[i] == 0:
                    cards.append(card)
                    visits[i] = 1
                    break
        return cards

    def deal_cards(self):
        shuffled_cards = np.random.permutation(self.config.cards_number)
        for i in range(len(self.players)):
            cards = np.sort(shuffled_cards[i*self.deal_card_number:i*self.deal_card_number+self.deal_card_number])
            self.players_hand_cards[self.players[i]] = list(cards)

    def init_player_every_card_number(self):
        for key in self.players_hand_cards:
            card_number = self.config.init_player_every_card_number_zero()
            hand_cards = sorted(self.players_hand_cards[key])
            for card in hand_cards:
                card_value = self.config.get_card_value(card)
                card_number[card_value] = card_number[card_value] + 1
            self.players_every_card_number[key] = card_number

    def get_current_player(self):
        return self.current_player

    def get_cards_by_move(self,move):
        cards_values = []
        if move >= 0 and move <= 14:
            cards_values.append(move)
            return self.get_cards_by_card_values(cards_values,self.current_player)
        elif move >= 15 and move <= 27:
            cards_values.append(move - 15)
            cards_values.append(move - 15)
            return self.get_cards_by_card_values(cards_values,self.current_player)
        elif move >= 28 and move <= 40:
            cards_values.append(move - 28)
            cards_values.append(move - 28)
            cards_values.append(move - 28)
            return self.get_cards_by_card_values(cards_values,self.current_player)
        return cards_values

    def do_move(self, move):
        self.last_move = move
        self.states.append(move)
        if move != self.config.pass_move:
            self.pass_number = 0
            self.meet_move = move
            self.meet_move_player = self.current_player
            self.meet_cards = self.get_cards_by_move(self.meet_move)
        cards = self.get_cards_by_move(move)
        self.already_played_cards.append(deepcopy(cards))
        for i in range(len(cards)):
            self.players_hand_cards[self.current_player].remove(cards[i])
            card_value = self.config.get_card_value(cards[i])
            self.players_every_card_number[self.current_player][card_value] -= 1
        #上一个出牌玩家
        self.last_play_card_player = self.current_player
        self.current_player = (self.current_player + 1) % 3
        if self.last_move == self.config.pass_move:
            self.pass_number += 1
        if self.pass_number == 2:
            self.meet_move = self.config.pass_move
            self.pass_number = 0
            self.meet_cards = []
        self.availables = self.config.get_moves_by_hand_cards(self.players_every_card_number[self.current_player],self.meet_move)

    def game_end(self):
        for i in self.players_hand_cards:
            if len(self.players_hand_cards[i]) <= 10:
                return True,i
        return False,-1

    '''
    第一个通道为己方牌
    第二个通道为上家牌
    第三个通道为下家牌
    接下来的通道为玩家倒着的出牌序列
    '''
    def current_state(self):
        square_state = np.zeros((5, 54, 1))
        before_player = self.config.get_before_player(self.current_player)
        after_player = self.config.get_after_player(self.current_player)
        #初始化前三个通道
        for card in self.config.cards:
            if card in self.players_hand_cards[self.current_player]:
                square_state[0][card,0] = 1.0
            else:
                square_state[0][card,0] = 0.0
            if card in self.players_hand_cards[before_player]:
                square_state[1][card,0] = 1.0
            else:
                square_state[1][card,0] = 0.0
            if card in self.players_hand_cards[after_player]:
                square_state[2][card,0] = 1.0
            else:
                square_state[2][card,0] = 0.0
                square_state[index][card,0] = 1.0
        index = 3
        for i in range(len(self.already_played_cards)-1,-1,-1):
            cards = self.already_played_cards[i]
            for card in cards:


        index = 3
        for cards in self.already_played_cards:
            for card in cards:
                square_state[index][card,0] = 1.0
            index += 1
            if index > 21:
                break
        #初始化第四个通道
        for card in self.meet_cards:
            square_state[3][card,0] = 1.0

        for i in range(54):
            square_state[4][i,0] = self.meet_move_player
        return square_state

class Game(object):
    def __init__(self, board):
        self.board = board

    def graphic(self, board):
        for i in board.players_hand_cards:
            print("player:",i,"cards:")
            hand_cards = board.players_hand_cards[i]
            hand_cards_str = ""
            for hand_card in hand_cards:
                hand_cards_str = hand_cards_str + self.board.config.get_card_name(hand_card)
                hand_cards_str = hand_cards_str + "  "
            print(hand_cards_str)

    def start_play(self, player1, player2,player3, start_player=0, is_shown=1):
        if start_player not in self.board.players:
            raise Exception('start_player should be either 0 (player1 first) '
                            'or 1 (player2 first)'
                            'or 2 (player3 first')
        self.board.init_board(start_player)
        p1, p2, p3 = self.board.players
        player1.set_player_ind(p1)
        player2.set_player_ind(p2)
        player3.set_player_ind(p3)
        players = {p1: player1, p2: player2,p3:player3}
        count = 0
        if is_shown:
            self.graphic(self.board)
        while True:
            current_player = self.board.get_current_player()
            player_in_turn = players[current_player]
            move = player_in_turn.get_action(self.board)
            cards = self.board.get_cards_by_move(move)
            cards_names = self.board.config.get_card_names_by_cards(cards)
            print("current player:",current_player)
            print("play cards:")
            print(cards_names)
            print("")
            self.board.do_move(move)
            print("play player:",self.board.get_current_player())
            print("availables:")
            print(self.board.availables)
            count = count + 1
            if is_shown:
                self.graphic(self.board)
            end, winner = self.board.game_end()
            if end:
                if is_shown:
                    if winner != -1:
                        print("Game end. Winner is", players[winner])
                return winner

    def start_self_play(self,player,is_shown = 0,temp = 1e-3):
        self.board.init_board()
        p1,p2,p3 = self.board.players
        states,mcts_probs,current_players = [],[],[]
        while True:
            move,move_probs = player.get_action(self.board,temp=temp,return_prob = 1)
            states.append(self.board.current_state())
            mcts_probs.append(move_probs)
            current_players.append(self.board.current_player)
            self.board.do_move(move)
            if is_shown:
                self.graphic(self.board)
            end,winner = self.board.game_end()
            if end:
                winners_z = np.zeros(len(current_players))
                if winner != -1:
                    winners_z[np.array(current_players) == winner] = 1.0
                    winners_z[np.array(current_players) != winner] = -1.0
                player.reset_player()
                if is_shown:
                    if winner != -1:
                        print("Game end.Winner is player:",winner)
                return winner,zip(states,mcts_probs,winners_z)



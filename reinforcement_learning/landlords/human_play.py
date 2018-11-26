# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-24 14:12:25
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-26 10:04:51
from __future__ import print_function
from game import Board, Game
from game_config import GameConfig
from mcts_pure import MCTSPlayer as MCTS_Pure
from mcts_alphaZero import MCTSPlayer
from policy_value_net_tensorflow import PolicyValueNet

class Human(object):

    def __init__(self,config):
        self.player = None
        self.config = config

    def set_player_ind(self, p):
        self.player = p

    def get_action(self, board):
        is_continue = True
        while True:
            play_cards_str = input("Please input your cards: ")
            play_cards_str = play_cards_str.replace(' ','')
            play_card_names = []
            for play_card_name in play_cards_str.split(','):
                if play_card_name != '':
                    play_card_names.append(play_card_name)
            if len(play_card_names) == 0:
          #      print(board.availables)
                if self.config.pass_move in board.availables:
                    return self.config.pass_move
            if self.config.is_valid_card_names(play_card_names):
                card_values,correct = self.config.get_card_values_by_card_names(play_card_names)
                if correct:
                    cards = board.get_cards_by_card_values(card_values,self.player)
                    cards_type = self.config.get_cards_type(cards)
                    if len(cards) == len(card_values) and cards_type != -1:
                        move = self.config.get_move_by_cards(cards)
                        if move in board.availables:
                            return move

    def __str__(self):
        return "Human {}".format(self.player)    

def run():
    model_file = './best_policy.model'
    config = GameConfig()
    board = Board(config)
    game = Game(board)
    mcts_player1 = MCTS_Pure(c_puct=5,n_playout=1000)
    mcts_player2 = MCTS_Pure(c_puct=5,n_playout=1000)
    human = Human(config)
    human2 = Human(config)
    human3 = Human(config)
    game.start_play(mcts_player1,human,mcts_player2)

if __name__ == '__main__':
    run()
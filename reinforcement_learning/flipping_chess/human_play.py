# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-10-24 15:24:39
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-10-29 17:18:13

'''
游戏规则：
1.棋子为司令，军长，师长，旅长，团长，营长，连长，炸弹，数目依次为1,1,2,2,2,2,1,1总共12颗
2.棋盘为军棋棋盘的下半部分
3.棋盘表示:
25 26 27 28 29
20 21 22 23 24
15 16 17 18 19
10 11 12 13 14
5  6  7  8  9
0  1  2  3  4

输入:x,y x表示起始点的棋盘位置，y表示移动到的终点棋盘位置 比如 0,1 表示从棋盘的第一个位置移动到第二个位置
move的表示方式为:abcd ab为移动前的横纵坐标 cd为移动后的横纵坐标 a,c为0时可以省略
action的表示方式为[x,y] x,y可与abcd相互转换
avaiable表示行动
该游戏总共有96总行为，每颗棋子可以移动到上，下，左，右，左上，右上，右下，左下8中行为

'''
from __future__ import print_function
from game import Board,Game
from mcts_alphaZero import MCTSPlayer
from policy_value_net_tensorflow import PolicyValueNet

class Human(object):

	def __init__(self):
		self.human_seat = None

	def set_Human_seat(self,human_seat):
		self.human_seat = human_seat

	'''
	如果想要翻棋则输入"30,1",如果想要移动棋子，则输入"1,2"。1表示选中棋子位置，2表示棋子的终点位置
	'''
	def get_action(self,board):
		try:
			action = input("Please input your action:")
			action = [int(n, 10) for n in action.split(",")]
			print(action)			
		except Exception as e:
			action  = []
		if len(action) != 2:
			print("invalid move")
			action = self.get_action(board)
		if not board.can_select(action[0],self.human_seat):
			print(action[0],"is not your chess")
			action = self.get_action(board)
		if not board.can_move_to(action[0],action[1]):
			print(action[0],"can't move to",action[1])
			action = self.get_action(board)

		return action

def run():
	model_file = './current_policy.model'
	width = 5
	height = 6

	board = Board()
	game = Game(board)
	best_policy = PolicyValueNet(width, height, model_file)
	mcts_player = MCTSPlayer(best_policy.policy_value_fn,
	                         c_puct=5,
	                         n_playout=400)
	human = Human()
	game.start_play(human, mcts_player, start_player=0, is_shown=1)


if __name__ == '__main__':
	run()
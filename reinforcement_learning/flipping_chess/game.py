# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-10-24 15:27:55
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-10-30 17:24:41
from __future__ import print_function
import random
import numpy as np
'''
cross_type表示该位置类型。0表示兵站，1表示行营
'''
class Cross(object):

	def __init__(self,id = None,cross_type = None):
		self.id = id
		self.cross_type = cross_type
		self.adjacent_cross = []
		self.chess = None

	def set_cross_type(self,cross_type):
		self.cross_type = cross_type

	def set_adjacent_cross(self,cross_ids):
		for element in cross_ids:
			self.adjacent_cross.append(element)

	def to_string(self):
		print("id:",self.id,"cross type:",self.cross_type)
		for i in self.adjacent_cross:
			print(i)
		'''
		for i in self.adjacent_cross:
			print(i,end=' ')
'''

class Chess(object):
	'''
	type:司令，军长，师长，旅长，团长,营长，连长，炸弹分别采用0,1,2,3,4,5,6,7表示
	'''
	def __init__(self,chess_type = None,seat = None,color = None,show = 0,index = 0):
		self.chess_type = chess_type
		self.seat = seat
		self.color = color
		self.show = show
		self.index = index
	def get_chess_name(self):
		if self.chess_type == 0:
			return 'a'
		elif self.chess_type == 1:
			return 'b'
		elif self.chess_type == 2:
			return 'c'
		elif self.chess_type == 3:
			return 'd'
		elif self.chess_type == 4:
			return 'e'
		elif self.chess_type == 5:
			return 'f'
		elif self.chess_type == 6:
			return 'g'
		elif self.chess_type == 7:
			return 'h'
	'''
	0表示同归于尽
	1表示战胜
	2表示战败
	-1表示不能攻击
	'''
	def get_fight_result(self,attacked_chess):
		if attacked_chess == None:
			return -1
		if self.seat == attacked_chess.seat:
			return -1
		if attacked_chess.chess_type == 7 or self.chess_type == 7:
			return 0
		elif self.chess_type == attacked_chess.chess_type:
			return 0
		if self.chess_type < attacked_chess.chess_type:
			return 1
		else:
			return 2

	def to_string(self):
		print("type:",self.chess_type,"seat:",self.seat,"color:",self.color,"show:",self.show)



class Board(object):

	'''
	每位玩家具有如下棋子
	司令，军长，师长，师长，旅长，旅长，团长，团长，营长，营长，连长，炸弹 总共12颗棋
	'''
	def __init__(self):
		self.players = [0,1]
		self.cross_list = []
		for i in range(30):
			cross = Cross(i,0)
			self.cross_list.append(cross)
		self.cross_list[11].set_cross_type(1)
		self.cross_list[13].set_cross_type(1)
		self.cross_list[17].set_cross_type(1)
		self.cross_list[21].set_cross_type(1)
		self.cross_list[23].set_cross_type(1)
		self.cross_list[0].set_adjacent_cross([1,5])
		self.cross_list[1].set_adjacent_cross([0,2,6])
		self.cross_list[2].set_adjacent_cross([1,3,7])
		self.cross_list[3].set_adjacent_cross([2,4,8])
		self.cross_list[4].set_adjacent_cross([3,9])
		self.cross_list[5].set_adjacent_cross([0,6,10,11])
		self.cross_list[6].set_adjacent_cross([1,5,7,11])
		self.cross_list[7].set_adjacent_cross([2,6,8,11,12,13])
		self.cross_list[8].set_adjacent_cross([3,7,9,13])
		self.cross_list[9].set_adjacent_cross([4,8,13,14])
		self.cross_list[10].set_adjacent_cross([5,11,15])
		self.cross_list[11].set_adjacent_cross([5,6,7,10,12,15,16,17])
		self.cross_list[12].set_adjacent_cross([7,11,13,17])
		self.cross_list[13].set_adjacent_cross([7,8,9,12,14,17,18,19])
		self.cross_list[14].set_adjacent_cross([9,13,19])
		self.cross_list[15].set_adjacent_cross([10,11,16,20,21])
		self.cross_list[16].set_adjacent_cross([11,15,17,21])
		self.cross_list[17].set_adjacent_cross([11,12,13,16,18,21,22,23])
		self.cross_list[18].set_adjacent_cross([13,17,19,23])
		self.cross_list[19].set_adjacent_cross([13,14,18,23,24])
		self.cross_list[20].set_adjacent_cross([15,21,25])
		self.cross_list[21].set_adjacent_cross([15,16,17,20,22,25,26,27])
		self.cross_list[22].set_adjacent_cross([17,21,23,27])
		self.cross_list[23].set_adjacent_cross([17,18,19,22,24,27,28,29])
		self.cross_list[24].set_adjacent_cross([19,23,29])
		self.cross_list[25].set_adjacent_cross([20,21,26])
		self.cross_list[26].set_adjacent_cross([21,25,27])
		self.cross_list[27].set_adjacent_cross([21,22,23,26,28])
		self.cross_list[28].set_adjacent_cross([23,27,29])
		self.cross_list[29].set_adjacent_cross([23,24,28])

		#初始化所有的棋子
		self.all_chess = []
		#type,seat,color,show,index
		#seat = 0
		self.all_chess.append(Chess(0,0,0,1,0))
		self.all_chess.append(Chess(1,0,0,1,0))		
		self.all_chess.append(Chess(2,0,0,1,0))
		self.all_chess.append(Chess(2,0,0,1,1))		
		self.all_chess.append(Chess(3,0,0,1,0))
		self.all_chess.append(Chess(3,0,0,1,1))		
		self.all_chess.append(Chess(4,0,0,1,0))
		self.all_chess.append(Chess(4,0,0,1,1))	
		self.all_chess.append(Chess(5,0,0,1,0))
		self.all_chess.append(Chess(5,0,0,1,1))		
		self.all_chess.append(Chess(6,0,0,1,0))
		self.all_chess.append(Chess(7,0,0,1,0))	
		#seat = 1
		self.all_chess.append(Chess(0,1,1,1,0))
		self.all_chess.append(Chess(1,1,1,1,0))		
		self.all_chess.append(Chess(2,1,1,1,0))
		self.all_chess.append(Chess(2,1,1,1,1))		
		self.all_chess.append(Chess(3,1,1,1,0))
		self.all_chess.append(Chess(3,1,1,1,1))		
		self.all_chess.append(Chess(4,1,1,1,0))
		self.all_chess.append(Chess(4,1,1,1,1))	
		self.all_chess.append(Chess(5,1,1,1,0))
		self.all_chess.append(Chess(5,1,1,1,1))		
		self.all_chess.append(Chess(6,1,1,1,0))
		self.all_chess.append(Chess(7,1,1,1,0))

		self.width = 5
		self.height = 6


	def init_board(self,start_player = 0):
		self.current_player = self.players[start_player]
		self.last_action = None
		self.players_chess_number = [12,12]
		self.states = {}
		self.no_eat_chess_times = 0
		self.action_times = 0
		self.random_layout()
		current_index = 0
		for i in range(29):
			if i == 11 or i == 13 or i == 17 or i == 21 or i == 23:
				self.cross_list[i].chess = None
			else:
				self.cross_list[i].chess = self.all_chess[current_index]
				current_index = current_index + 1
		self.cross_list[29].chess = None
		self.moves = self.get_moves(self.current_player)
		self.availables = self.get_availables(self.moves)
#		print("moves:")
#		print(self.moves)
#		print("availables:")
#		print(self.availables)
		

	def random_layout(self):
		for i in range(len(self.all_chess) - 1,-1,-1):
			random_index = random.randint(0,i)
			chess = self.all_chess[random_index]
			self.all_chess[random_index] = self.all_chess[i]
			self.all_chess[i] = chess

	def to_string(self):
		str_list = []
		for i in range(self.height):
			one_raw_str = ""
			for j in range(self.width):
				cross_index = i * 5 + j
				if self.cross_list[cross_index].chess == None:
					one_raw_str = one_raw_str +"*"
				else:
					if self.cross_list[cross_index].chess.seat == 0:
						one_raw_str = one_raw_str + str(self.cross_list[cross_index].chess.chess_type)
					else:
						one_raw_str = one_raw_str + self.cross_list[cross_index].chess.get_chess_name()
				one_raw_str = one_raw_str +"          "
			str_list.append(one_raw_str)

		for i in range(len(str_list) - 1,-1,-1):
			print(str_list[i])
			print("")

	def get_current_player(self):
		return self.current_player

	def do_move(self,available):
		action = self.get_action_by_available(available,self.current_player)
		self.last_action = action
		self.action_times = self.action_times + 1
		if self.cross_list[action[1]].chess == None:
			self.no_eat_chess_times = self.no_eat_chess_times + 1
		else:
			self.no_eat_chess_times = 0
		self.move_chess(action)
		if self.current_player == self.players[1]:
			self.current_player = self.players[0]
		else:
			self.current_player = self.players[1]
		self.moves = self.get_moves(self.current_player)
		self.availables = self.get_availables(self.moves)

	def move_chess(self,action):
		if len(action) < 2:
			return 
		elif self.cross_list[action[0]].chess == None:
			return
		else:
			if self.cross_list[action[1]].chess == None:
				self.cross_list[action[1]].chess = self.cross_list[action[0]].chess
				self.cross_list[action[0]].chess = None
			else:
				fight_result = self.cross_list[action[0]].chess.get_fight_result(self.cross_list[action[1]].chess)
				if fight_result == 1:
					end_move_chess = self.cross_list[action[1]].chess
					self.players_chess_number[end_move_chess.seat] = self.players_chess_number[end_move_chess.seat] - 1
					self.cross_list[action[1]].chess= self.cross_list[action[0]].chess
				elif fight_result == 0:
					start_move_chess = self.cross_list[action[0]].chess
					end_move_chess = self.cross_list[action[1]].chess
					self.players_chess_number[start_move_chess.seat] = self.players_chess_number[start_move_chess.seat] - 1
					self.players_chess_number[end_move_chess.seat] = self.players_chess_number[end_move_chess.seat] - 1
					self.cross_list[action[1]].chess = None
				self.cross_list[action[0]].chess = None

	def has_a_winner(self):
		if len(self.availables) == 0:
			return True,(self.current_player + 1) % 2
		if self.players_chess_number[0] < 3:
			return True,1
		elif self.players_chess_number[1] < 3:
			return True,0
		return False,-1


		'''
		当没有棋子时，则判输
		当30步没吃子时，强制和棋
		当总步数超过250步时，强制和棋
		'''

	def game_end(self):
		win,winner = self.has_a_winner()
		if win:
			return True,winner
		elif self.no_eat_chess_times == 30:
			return True,-1
		elif self.action_times > 250:
			return True,-1
		return False,-1

	def can_select(self,position,seat):
		if self.cross_list[position].chess == None:
			return False
		elif self.cross_list[position].chess.seat != seat:
			return False
		return True

	def can_move_to(self,start_position,to_position):
		if to_position not in self.cross_list[start_position].adjacent_cross:
			return False
		if self.cross_list[start_position].chess == None:
			return False
		else:
			if self.cross_list[to_position].chess == None:
				return True
			else:
				fight_result = self.cross_list[start_position].chess.get_fight_result(self.cross_list[to_position].chess)
				if fight_result == 0 or fight_result == 1:
					return True
				else:
					return False
	'''
	第一个棋盘为当前玩家的棋子位置表示
	第二个棋盘为另一玩家的棋子位置表示
	第三个棋盘为最后一颗子的落子位置
	第四个棋盘为如果该己方行动，则为1，否则为0
	'''
	def current_state(self):
		square_state = np.zeros((4, self.height, self.width))
		if self.action_times > 0:
			for i in range(self.height):
				for j in range(self.width):
					chess = self.cross_list[i * self.width + j].chess
					if chess != None:
						if chess.seat == self.current_player:
							square_state[0][i,j] = chess.chess_type
						else:
							square_state[1][i,j] = chess.chess_type
			square_state[2][self.last_action[1]//self.width,self.last_action[1]%self.width] = 1.0
		if self.action_times % 2 == 0:
			square_state[3][:, :] = 1.0
        #将棋盘最后一行放到第一行，倒数第二行放在第二行，依次类推
		return square_state[:,::-1, :]
	'''
	行为表示为xyab xy表示移动前位置，ab表示移动后位置 x与a为0时可省略
	'''
	'''
	def code_action(self,action):
		return action[0]*100 + action[1]
	'''

	#move表示为xyab xy表示移动前位置，ab表示移动后位置 x与a为0时可省略
	def get_action_by_move(self,move):
		action = []
		start_location = move // 100
		start_location_x = start_location // 10
		start_location_y = start_location % 10
		action.append(start_location_x * self.width + start_location_y)
		end_location = move % 100
		end_location_x = end_location // 10
		end_location_y = end_location % 10
		action.append(end_location_x * self.width + end_location_y)
		return action
	#根据action[f,g]得到abxy
	def get_move_by_action(self,action):
		start_index = action[0]
		end_index = action[1]
		start_x = start_index // self.width
		start_y = start_index % self.width
		end_x = end_index // self.width
		end_y = end_index % self.width
		start_move = start_x * 10 + start_y
		end_move = end_x * 10 + end_y
		move = start_move * 100 + end_move
		return move


	def same_chess_count(self,chess_type,pos,seat):
		pos_x = pos // 10
		pos_y = pos % 10
		location = pos_x * self.width + pos_y
		count = 1
		for i in range(location):
			chess = self.cross_list[i].chess
			if chess != None:
				if chess.chess_type == chess_type and chess.seat == seat:
					count = count + 1
		return count


	def get_available_by_move(self,move):
		start = move // 100
		start_location_x = start // 10
		start_location_y = start % 10
		start_location = start_location_x * self.width + start_location_y

		end = move % 100
		end_location_x = end // 10
		end_location_y = end % 10
		end_location = end_location_x * self.width + end_location_y

		start_chess= self.cross_list[start_location].chess
		chess_type = start_chess.chess_type
		chess_seat = start_chess.seat

		right_direction = 1	
		left_direction = -1
		up_direction = self.width	
		down_direction = -self.width	
		left_up_direction = self.width - 1
		right_up_direction = self.width + 1
		left_down_direction = -self.width - 1
		right_down_direction = -self.width + 1

		direction = end_location - start_location
		count = self.same_chess_count(chess_type,start,chess_seat)
		#司令
		if chess_type == 0:
			dic = {right_direction:0,left_direction:1,up_direction:2,down_direction:3,left_up_direction:4,right_up_direction:5,left_down_direction:6,right_down_direction:7}
			return dic[direction]
		#军长
		elif chess_type == 1:
			dic = {right_direction:8,left_direction:9,up_direction:10,down_direction:11,left_up_direction:12,right_up_direction:13,left_down_direction:14,right_down_direction:15}			
			return dic[direction]
		#师长
		elif chess_type == 2:
			if count == 1:
				dic = {right_direction:16,left_direction:17,up_direction:18,down_direction:19,left_up_direction:20,right_up_direction:21,left_down_direction:22,right_down_direction:23}			
			else:
				dic = {right_direction:24,left_direction:25,up_direction:26,down_direction:27,left_up_direction:28,right_up_direction:29,left_down_direction:30,right_down_direction:31}	
			return dic[direction]
		#旅长
		elif chess_type == 3:
			if count == 1:
				dic = {right_direction:32,left_direction:33,up_direction:34,down_direction:35,left_up_direction:36,right_up_direction:37,left_down_direction:38,right_down_direction:39}			
			else:
				dic = {right_direction:40,left_direction:41,up_direction:42,down_direction:43,left_up_direction:44,right_up_direction:45,left_down_direction:46,right_down_direction:47}	
			return dic[direction]
		#团长
		elif chess_type == 4:
			if count == 1:
				dic = {right_direction:48,left_direction:49,up_direction:50,down_direction:51,left_up_direction:52,right_up_direction:53,left_down_direction:54,right_down_direction:55}			
			else:
				dic = {right_direction:56,left_direction:57,up_direction:58,down_direction:59,left_up_direction:60,right_up_direction:61,left_down_direction:62,right_down_direction:63}	
			return dic[direction]
		#营长
		elif chess_type == 5:
			if count == 1:
				dic = {right_direction:64,left_direction:65,up_direction:66,down_direction:67,left_up_direction:68,right_up_direction:69,left_down_direction:70,right_down_direction:71}			
			else:
				dic = {right_direction:72,left_direction:73,up_direction:74,down_direction:75,left_up_direction:76,right_up_direction:77,left_down_direction:78,right_down_direction:79}	
			return dic[direction]
		#连长
		elif chess_type == 6:
			dic = {right_direction:80,left_direction:81,up_direction:82,down_direction:83,left_up_direction:84,right_up_direction:85,left_down_direction:86,right_down_direction:87}			
			return dic[direction]			
		#炸弹
		elif chess_type == 7:
			dic = {right_direction:88,left_direction:89,up_direction:90,down_direction:91,left_up_direction:92,right_up_direction:93,left_down_direction:94,right_down_direction:95}			
			return dic[direction]	

	def get_moves(self,seat):
		moves = []
		for i in range(len(self.cross_list)):
			cross = self.cross_list[i]
			chess = cross.chess
			if chess != None:
				if chess.seat == seat:
					for element in cross.adjacent_cross:
						if self.cross_list[element].chess == None:
							move = self.get_move_by_action([i,element])
							moves.append(move)
						else:
							fight_result = chess.get_fight_result(self.cross_list[element].chess)
							if fight_result != 2 and fight_result != -1:
								move = self.get_move_by_action([i,element])
								moves.append(move)
		return moves

	def get_availables(self,moves):
		availables = []
		for i in range(len(moves)):
			available = self.get_available_by_move(moves[i])
			availables.append(available)
		return availables

	def get_chess_type_by_available(self,available):
		num = available // 8
		chess_type = None
		if num == 0:
			chess_type = 0
		elif num == 1:
			chess_type = 1
		elif num == 2 or num == 3:
			chess_type = 2
		elif num == 4 or num == 5:
			chess_type = 3
		elif num == 6 or num == 7:
			chess_type = 4
		elif num == 8 or num == 9:
			chess_type = 5
		elif num == 10:
			chess_type = 6
		elif num == 11:
			chess_type = 7
		return chess_type

	def get_chess_pos(self,chess_type,seat,count):
		for i in range(len(self.cross_list)):
			chess = self.cross_list[i].chess
			if chess != None:
				if chess.chess_type == chess_type and chess.seat == seat:
					count = count - 1
					if count == 0:
						return i 

	def get_chess_end_index(self,start_index,direction):
		if direction == 0:
			return start_index + 1
		elif direction == 1:
			return start_index - 1
		elif direction == 2:
			return start_index + self.width
		elif direction == 3:
			return start_index - self.width
		elif direction == 4:
			return start_index + self.width - 1
		elif direction == 5:
			return start_index + self.width + 1
		elif direction == 6:
			return start_index - self.width - 1
		elif direction == 7:
			return start_index - self.width + 1

	def get_action_by_available(self,available,seat):
		#chess_type = self.decode_chess_type(available)
		action = []
		num = available // 8
		direction = available % 8
		chess_type = self.get_chess_type_by_available(available)
		if num == 0 or num == 1 or num == 2 or num == 4 or num == 6 or num == 8 or num == 10 or num == 11:
			start_index = self.get_chess_pos(chess_type,seat,1)
			end_index = self.get_chess_end_index(start_index,direction)
			action.append(start_index)
			action.append(end_index)
		elif num == 3 or num == 5 or num == 7 or num == 9:
			start_index = self.get_chess_pos(chess_type,seat,2)
			end_index = self.get_chess_end_index(start_index,direction)
			action.append(start_index)
			action.append(end_index)
		return action

class Game(object):
	def __init__(self,board):
		self.board = board

	def graphic(self,board):
		self.board.to_string()
		print()
		print("---------------------")
		print()

	def start_play(self,player1,player2,start_player = 0,is_shown = 1):
		if start_player not in (0,1):
			raise Exception('start_player should be either 0(player1 first)'
				'or 1 (player2 first')
		self.board.init_board(start_player)
		p1,p2 = self.board.players
		player1.set_Human_seat(p1)
		player2.set_Human_seat(p2)
		players = {p1:player1,p2:player2}
		if is_shown:
			self.graphic(self.board)
		while True:
			current_player = self.board.get_current_player()
			player_in_turn = players[current_player]
			action = player_in_turn.get_action(self.board)
			if not isinstance(action,list):
				pass
			else:
				move = self.board.get_move_by_action(action)
				action = self.board.get_available_by_move(move)
			self.board.do_move(action)
			if is_shown:
				self.graphic(self.board)
			end,winner = self.board.game_end()
			if end:
				if is_shown:
					if winner != -1:
						print("Game end.Winner is",winner)
					else:
						print("Game end. Tie")
				return winner

	def start_self_play(self,player,is_shown = 0,temp = 1e-3):
		self.board.init_board()
		p1,p2 = self.board.players
		states,mcts_probs,current_players = [],[],[]
		while True:
			action,action_probs = player.get_action(self.board,temp=temp,return_prob = 1)
			states.append(self.board.current_state())
			mcts_probs.append(action_probs)
			current_players.append(self.board.current_player)
			if not isinstance(action,list):
				pass
			else:
				move = self.board.get_move_by_action(action)
				action = self.board.get_available_by_move(move)			
			self.board.do_move(action)
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
					else:
						print("Game end. Tie")
				return winner,zip(states,mcts_probs,winners_z)








from random import choice
from grid import *
from copy import deepcopy
import time

class Bot:
	def __init__(self):
		self.smart_mode = None

	def move(self,grid,shape):
		self.grid = grid
		self.bot_shape = shape
		if shape == "X":
			self.player_shape = "O"
		else:
			self.player_shape = "X"
		if self.smart_mode:
			return self.smartMove()
		else:
			return self.naiveMove()

	def smartMove(self):
		self.best_score = float('-inf')
		for i in range(3):
			for o in range(3):
				if self.grid[i][o] == "":
					self.grid[i][o] = self.bot_shape
					score = self.minimax(self.grid,False)
					if score > self.best_score :
						self.best_score = score
						self.best_move = (i,o)
					self.grid[i][o] = ""
		return self.best_move

	def minimax(self,grid,is_maximizing):
		if self.win(grid)[0]:
			if self.win(grid)[1]:
				return 1
			elif not self.win(grid)[1]:
				return -1
		elif self.fullGrid(grid):
			return 0
		elif is_maximizing:
			best_score = float('-inf')
			for i in range(3):
				for o in range(3):
					if grid[i][o] == "":
						grid[i][o] = self.bot_shape
						score = self.minimax(grid,False)
						best_score = max(score,best_score)
						grid[i][o] = ""
			return best_score
		else:
			best_score = float('inf')
			for i in range(3):
				for o in range(3):
					if grid[i][o] == "":
						grid[i][o] = self.player_shape
						score = self.minimax(grid,True)
						best_score = min(score,best_score)
						grid[i][o] = ""
			return best_score


	def naiveMove(self):
		return choice(self.allAvailableMove(self.grid))

	def allAvailableMove(self,grid):
		move_available = []
		for i in range(3):
			for o in range(3):
				if self.grid[i][o] == "":
					move_available.append((i,o))
		return move_available

	def win(self,grid):
		for i in range(3):
			if (grid[0][i] == grid[1][i] == grid[2][i]) and grid[0][i] != "":
				if self.bot_shape == grid[0][i]:
					return True,True
				else:
					return True,False
			if (grid[i][0] == grid[i][1] == grid[i][2]) and grid[i][0] != "":
				if self.bot_shape == grid[i][0]:
					return True,True
				else:
					return True,False
		if grid[0][0] == grid[1][1] == grid[2][2] and grid[1][1] != "":
			if self.bot_shape == grid[1][1]:
				return True,True
			else:
				return True,False
		elif grid[0][2] == grid[1][1] == grid[2][0] and grid[1][1] != "": 
			if self.bot_shape == grid[1][1]:
				return True,True
			else:
				return True,False
		return False,None


	def fullGrid(self,grid):
		for i in range(3):
			for o in range(3):
				if self.grid[i][o] == '':
					return False
		return True
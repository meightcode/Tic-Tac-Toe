#importation des autres classes
from grid import *
from bot import *
from constant import *
from random import choice
from random import uniform
import pygame

class Game:
	def __init__(self):
		self.is_playing = False
		self.grid = Grid()
		self.bot = Bot()
		self.winner = None
		self.mode = None # 0 : 1v1 / 1 : 1vBotNaive / 2 : 1vBotSmart / 3 : tableau de fin de partie / None : menu
		self.circle_images = [[pygame.transform.scale(pygame.image.load('image/circle.png'),(win[0]//11,win[0]//11)),False,(3/2*win[0]//5+win[0]//5*i,3/2*win[1]//5+win[1]//5*o)] for i in range(3) for o in range(3)]
		self.cross_images = [[pygame.transform.scale(pygame.image.load('image/cross.png'),(win[0]//11,win[0]//11)),False,(3/2*win[0]//5+win[0]//5*i,3/2*win[1]//5+win[1]//5*o)] for i in range(3) for o in range(3)]
		self.menu_button_image = pygame.transform.scale(pygame.image.load('image/menu.png'),(win[0]//14,win[0]//14))
		self.replay_button_image = pygame.transform.scale(pygame.image.load('image/replay.png'),(win[0]//14,win[0]//14))
		self.move_time = time.time()

	def initGame(self):
		if choice([False,True]):
			self.player1_shape ,self.player2_shape = "X" ,"O"
			self.player1_turn = True
			self.player2_turn = False
		else:
			self.player1_shape ,self.player2_shape = "O" ,"X"
			self.player1_turn = False
			self.player2_turn = True

	def init1v1(self):
		self.mode = 0
		self.initGame()

	def init1vNaiveBot(self):
		self.mode = 1
		self.bot.smart_mode = False
		self.initGame()

	def init1vSmartBot(self):
		self.mode = 2
		self.bot.smart_mode = True
		self.initGame()

	def botMove(self):
		move = self.bot.move(self.grid.grid,self.player2_shape)
		self.grid.grid[move[0]][move[1]] = self.player2_shape
		self.player2_turn = False
		self.player1_turn = True
			
	def refreshGrid(self):
		for i in range(3):
			for o in range(3):
				if self.grid.grid[i][o] == "X":
					self.cross_images[i*3+o][1] = True
					self.circle_images[i*3+o][1] = False
				elif self.grid.grid[i][o] == "O":
					self.circle_images[i*3+o][1] = True
					self.cross_images[i*3+o][1] = False
				elif self.grid.grid[i][o] == "":
					self.circle_images[i*3+o][1] = False
					self.cross_images[i*3+o][1] = False


		for circle in self.circle_images:
			if circle[1]:
				screen.blit(circle[0],circle[0].get_rect(center=(circle[2][0],circle[2][1])))
		for cross in self.cross_images:
			if cross[1]:
				screen.blit(cross[0],cross[0].get_rect(center=(cross[2][0],cross[2][1])))

	def checkGrid(self):
		if self.grid.win()[0]:
			if self.mode != 3:
				self.previous_mode = self.mode
			self.mode = 3
			if self.previous_mode == 0:
				if self.player1_turn:
					self.winner = "player2"
				else:
					self.winner = "player1"
			else:
				if self.player1_turn:
					self.winner = "bot"
				else:
					self.winner = "player"

		elif self.grid.fullGrid():
			if self.mode != 3:
				self.previous_mode = self.mode
			self.mode = 3
			self.winner = None

	def update(self,screen):

		if self.is_playing :
			self.refreshGrid()
			self.checkGrid()
			#grille de jeu
			for i in range(4):
				pygame.draw.line(screen,white,(win[0]//5*(i+1),win[1]//5),(win[0]//5*(i+1),win[1]-win[1]//5),5)
				pygame.draw.line(screen,white,(win[0]//5,win[1]//5*(i+1)),(win[0]-win[0]//5,win[1]//5*(i+1)),5)

			if self.mode == 0:
				pygame.draw.rect(screen,(white),cadre_player1,3)
				pygame.draw.rect(screen,(white),cadre_player2,3)
				screen.blit(text_player1,(surface_text_player1))
				screen.blit(text_player2,(surface_text_player2))

				if self.player1_turn:
					pygame.draw.rect(screen,(red),cadre_player1_turn,3)
				else:
					pygame.draw.rect(screen,(red),cadre_player2_turn,3)	

			elif self.mode == 3:
				if self.grid.win()[1][0] == "c":
					if self.grid.win()[1][1] == "0":
						pygame.draw.line(screen,red,(3*win[0]//10,win[1]//4.5),(3*win[0]//10,win[1]-win[1]//4.5),10)
					elif self.grid.win()[1][1] == "1":
						pygame.draw.line(screen,red,(5*win[0]//10,win[1]//4.5),(5*win[0]//10,win[1]-win[1]//4.5),10)
					else :
						pygame.draw.line(screen,red,(7*win[0]//10,win[1]//4.5),(7*win[0]//10,win[1]-win[1]//4.5),10)

				elif self.grid.win()[1][0] == "r":
					if self.grid.win()[1][1] == "0":
						pygame.draw.line(screen,red,(win[0]//4.5,3*win[1]//10),(win[0]-win[0]//4.5,3*win[1]//10),10)
					elif self.grid.win()[1][1] == "1":
						pygame.draw.line(screen,red,(win[0]//4.5,5*win[1]//10),(win[0]-win[0]//4.5,5*win[1]//10),10)
					else :
						pygame.draw.line(screen,red,(win[0]//4.5,7*win[1]//10),(win[0]-win[0]//4.5,7*win[1]//10),10)
				else :
					if self.grid.win()[1][1] == "0":
						pygame.draw.line(screen,red,(win[0]//4.5,win[1]//4.5),(win[0]-win[0]//4.5,win[1]-win[1]//4.5),10)
					elif self.grid.win()[1][1] == "1":
						pygame.draw.line(screen,red,(win[0]-win[0]//4.5,win[1]//4.5),(win[0]//4.5,win[1]-win[1]//4.5),10)

				if self.winner != None :
					winner_text = big_font.render("Winner : " + self.winner, True, (white))
				else:
					winner_text = big_font.render("Egalité !", True, (white))

				winner_text_surface = winner_text.get_rect(center=(win[0]//2,win[1]//10))
				screen.blit(winner_text,winner_text_surface)

				pygame.draw.rect(screen,(salmon),cadre_to_replay,2)
				pygame.draw.rect(screen,(salmon),cadre_to_menu,2)

				screen.blit(self.replay_button_image,self.replay_button_image.get_rect(center=(win[0]//30+win[0]//16,win[1]//30+win[1]//16)))
				screen.blit(self.menu_button_image,self.menu_button_image.get_rect(center=(win[0]-win[0]//30-win[0]//8+win[0]//16,win[1]//30+win[1]//16)))

			else:
				pygame.draw.rect(screen,(white),cadre_player1,3)
				pygame.draw.rect(screen,(white),cadre_player2,3)
				screen.blit(text_player,(surface_text_player1))
				screen.blit(text_naive_bot,(surface_text_player2))
				if self.player2_turn:

					pygame.draw.rect(screen,(red),cadre_player2_turn,3)
					if  time.time() - self.move_time > uniform(2,0.5):
						self.botMove()
				else:
					pygame.draw.rect(screen,(red),cadre_player1_turn,3)
		else:
			#cadre du menu
			pygame.draw.rect(screen,(salmon),menu_rect_1,2)
			pygame.draw.rect(screen,(salmon),menu_rect_2,2)
			pygame.draw.rect(screen,(salmon),menu_rect_3,2)
			pygame.draw.rect(screen,(salmon),menu_title_rect,4)

			#texte du menu
			screen.blit(text_1v1,(surface_text_1v1))
			screen.blit(text_1vnaivebot,(surface_text_1vnaivebot))
			screen.blit(text_1vsmartbot,(surface_text_1vsmartbot))
			screen.blit(text_title_2,(surface_text_title_2))
			screen.blit(text_title,(surface_text_title))


	def click(self,coordinate):
		if self.is_playing :
			if self.mode == 3:
				if win[1]//30<coordinate[1]<win[1]//30+win[1]//8:
					if win[0]//30<coordinate[0]<win[0]//30+win[0]//8:
						self.grid.clearGrid()
						self.mode = self.previous_mode
						if self.previous_mode == 0:
							self.init1v1()
						elif self.previous_mode == 1:
							self.init1vNaiveBot()
						else:
							self.init1vSmartBot()
					elif win[0]-win[0]//30-win[0]//8<coordinate[0]<win[0]-win[0]//30:
						self.grid.clearGrid()
						self.is_playing = False
						self.mode = None
			else:
				for i in range(3):
					for o in range(3):
						if win[0]//5*(i+1) < coordinate[0] < win[0]//5*(i+2):
							if win[1]//5*(o+1) < coordinate[1] < win[1]//5*(o+2) :
								if self.mode == 0:
									if self.player1_turn and self.grid.grid[i][o] == "":
										self.grid.grid[i][o] = self.player1_shape
										self.player1_turn = False
										self.player2_turn = True
									elif self.player2_turn and self.grid.grid[i][o] == "":
										self.grid.grid[i][o] = self.player2_shape
										self.player1_turn = True
										self.player2_turn = False
								else:
									if self.player1_turn and self.grid.grid[i][o] == "":
										self.move_time = time.time()
										self.grid.grid[i][o] = self.player1_shape
										self.player1_turn = False
										self.player2_turn = True
										

		else:
			#verifie si la souris est dans certaines cases 
			if win[0]//4<coordinate[0]<win[0]//4*3:
				if win[1]//4<coordinate[1]<win[1]//8*3 :
					self.is_playing = True
					self.init1v1()
				elif win[1]//4*1.7<coordinate[1]<win[1]//4*1.7+win[1]//8:
					self.is_playing = True
					self.init1vNaiveBot()
				elif win[1]//4*2.4<coordinate[1]<win[1]//4*2.4+win[1]//8:
					self.is_playing = True
					self.init1vSmartBot()




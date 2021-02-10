#importation des modules et classes 
from constant import *
from game import Game
import pygame
import sys

#creer une instance de la classe Game()
game = Game()

def main():
	while True:

		#pour chaque evenements possibles 
		for event in pygame.event.get():

			#si le joueur click sur la croix
			if event.type == pygame.QUIT :
				pygame.quit()
				sys.exit()

			#si un boutton de la souris est relaché 
			if event.type == pygame.MOUSEBUTTONUP:
				game.click(pygame.mouse.get_pos()) 

		#remplie l'ecran de la couleur de fond 
		screen.fill(bg_color)

		#met a jour les elements du jeu
		game.update(screen)

		#raffrechit le jeu en appliquant tout les nouvelles choses
		pygame.display.flip()

main()
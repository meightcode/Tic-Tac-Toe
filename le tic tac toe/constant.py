import pygame

win = [800,800]

#taille de la fenetre de jeu
screen = pygame.display.set_mode((win[0],win[1]))

#titre du jeu
title = pygame.display.set_caption("Tic Tac Toe")

#permet de limiter la vitesse du progamme pour que la puissance de l'ordinateur ne joue pas sur la vitesse du jeu
clock = pygame.time.Clock()

#creer la fenetre en lancant le jeu
pygame.init()

#creation des couleurs
white = [255,255,255]
red = [255,000,000]
bg_color = [33,47,61]
salmon = [250,128,114]

#mise en place des polices
standard_font = pygame.font.Font(None, 30)
big_font = pygame.font.Font(None, 50)
title_font = pygame.font.Font("police/CHICORY_.ttf", 30)

#rectangle qui serve de cadre dans le menu
menu_title_rect = pygame.Rect(0,0,win[0],win[1]//8)
menu_rect_1 = pygame.Rect(win[0]//4,win[1]//4,win[0]//2,win[1]//8)
menu_rect_2 = pygame.Rect(win[0]//4,win[1]//4*1.7,win[0]//2,win[1]//8)
menu_rect_3 = pygame.Rect(win[0]//4,win[1]//4*2.4,win[0]//2,win[1]//8)

#texte du titre
text_title = title_font.render("Tic Tac Toe", True , (white))
surface_text_title = text_title.get_rect(center=(win[0]//2,win[1]//16))

#texte du titre d'une autre couleur pour le relief
text_title_2 = title_font.render("Tic Tac Toe", True , (salmon))
surface_text_title_2 = text_title.get_rect(center=(win[0]//2+5,win[1]//16+5))

#texte pour la case 1v1
text_1v1 = standard_font.render("Player VS Player", True , (white))
surface_text_1v1 = text_1v1.get_rect(center=(win[0]//2,win[1]//4+win[1]//16))

#texte pour la case 1vBotNaive
text_1vnaivebot = standard_font.render("Player VS Naive Bot", True , (white))
surface_text_1vnaivebot = text_1vnaivebot.get_rect(center=(win[0]//2,win[1]//4*1.7+win[1]//16))

#texte pour la case 1vBotSmart
text_1vsmartbot = standard_font.render("Player VS Smart Bot", True , (white))
surface_text_1vsmartbot = text_1vsmartbot.get_rect(center=(win[0]//2,win[1]//4*2.4+win[1]//16))

#cadres et textes joueurs
text_player1 = standard_font.render("Player 1", True , (white))
surface_text_player1 = text_player1.get_rect(center=(win[0]//30+win[0]//16,win[1]//30+win[1]//30))

text_player2 = standard_font.render("Player 2", True , (white))
surface_text_player2 = text_player1.get_rect(center=(win[0]-win[0]//30-(win[0]//16),win[1]-win[0]//30-win[1]//30))

text_player = standard_font.render("Yourself ", True , (white))
text_naive_bot = standard_font.render("Easy Bot", True , (white))
text_smart_bot = standard_font.render("Smart Bot", True , (white))

cadre_player1 = pygame.Rect(win[0]//30,win[1]//30,win[0]//8,win[1]//15)

cadre_player2 = pygame.Rect(win[0]-win[0]//30-win[0]//8,win[1]-win[1]//30-win[0]//15,win[0]//8,win[1]//15)

cadre_player1_turn = pygame.Rect(win[0]//30,win[1]//30,win[0]//8,win[1]//15)

cadre_player2_turn = pygame.Rect(win[0]-win[0]//30-win[0]//8,win[1]-win[1]//30-win[0]//15,win[0]//8,win[1]//15)


#end menu 
cadre_to_replay = pygame.Rect(win[0]//30,win[1]//30,win[0]//8,win[1]//8)
cadre_to_menu = pygame.Rect(win[0]-win[0]//30-win[0]//8,win[1]//30,win[0]//8,win[1]//8)
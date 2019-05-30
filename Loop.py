import pygame
import sys
from Clases import*
import random

pygame.init()
run = True
game = False
game_running = False
#file_manager = csv()

white = (255, 255, 255)

#VARIABLES DE PANTALLA
screen_size = [1280, 720] #tamano de la pantalla
win = pygame.display.set_mode ((screen_size[0], screen_size[1])) #superficie principal
#pygame.display.set_caption("Death race")
#fps= 30
#frames:totales=0

#FUENTES
#fuente1 = pygame.font.Font('fonts/.ttf', 48) #fuente a usar tamano 48
#fuente2 = pygame.font.Font('fonts/.ttf', 28) #fuente a usar tamano 48

#FONDO DEL JUEGO
#background = pygame.image.load('images/background.png')
#background = pygame.transform.scale(background, (1280, 720))
#back_rect = background.get_rect()

#MUSICA DE FONDO MENU
#pygame.mixer.music.load('sounds\menu.mp3')

#pygame.mixer.music.play(-1)

from Clases import *
from pygame import *

pygame.init()
screen_size = [1280, 720]
map_size = [screen_size[0]*30, screen_size[1]*30]

win = pygame.display.set_mode((screen_size[0], screen_size[1]))

#VARIABLES DE  MODO
run = True #variable que mantiene el ciclo principal
menu_inicial = True #variable que activa el menu de inicio
pausa = False #variable que
juego = False



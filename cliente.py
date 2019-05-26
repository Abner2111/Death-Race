import Clases
import pygame
import tkinter
import random
import socket

pygame.init()

run = True
game = False
game_running = False
menu = True

#VARIABLES DE PANTALLA
screen_size = [1280, 720]
win = pygame.display.set_mode((screen_size[0], screen_size[1]))
pygame.display.set_caption("pyDakar Death")

#VARIABLES DE MENU
#COLORES
color_botones = (253, 165, 15)
color_titulo = (249,166,1)
#FUENTES

fuente1 = pygame.font.Font('Data/Fonts/AVENGEANCE.ttf', 240)
fuente2 = pygame.font.Font('Data/Fonts/AVENGEANCE.ttf', 80)
fuente3 = pygame.font.Font('Data/Fonts/AVENGEANCE.ttf', 50)

#FONDO DEL MENU
background_menu = pygame.image.load('Data/Images/background.jpg')
background_menu = pygame.transform.scale(background_menu,(1280, 720))
#TEXTOS
titulo = fuente1.render('pydakar death ', True, color_titulo)
Boton_iniciar = fuente2.render('iniciar partida', True, color_botones)
Boton_guardada = fuente3.render('partida guardada', True, color_botones)
Boton_fama = fuente3.render('salon de la fama', True, color_botones)
Boton_info = fuente3.render('info de desarrolladores', True, color_botones)
Boton_salir =  fuente3.render('salir del juego', True, color_botones)

#VARIABLES DE OBJETOS EN PANTALLA

def main_menu():
    win.blit(background_menu,(0,0))
    win.blit(titulo,(0,20))
    win.blit(Boton_iniciar,(50, 270))
    win.blit(Boton_guardada,(50, 350))
    win.blit(Boton_fama, (50, 400))
    win.blit (Boton_info, (50, 570))
    win.blit (Boton_salir, (50, 620))

def game_process(nivel):
    pass


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if menu:
        main_menu()
    pygame.display.update()
pygame.quit()


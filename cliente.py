import Clases
import pygame
import tkinter
import random
import socket

pygame.init()

run = True
game = False
menu = True

#VARIABLES DE PANTALLA
screen_size = [1280, 720]
win = pygame.display.set_mode((screen_size[0], screen_size[1]))
pygame.display.set_caption("pyDakar Death")

#VARIABLES DE MENU
#colores

color_botones = (253, 165, 15)
color_titulo = (249,166,1)
#fuentes

fuente1 = pygame.font.Font('Data/Fonts/AVENGEANCE.ttf', 240)
fuente2 = pygame.font.Font('Data/Fonts/AVENGEANCE.ttf', 80)
fuente3 = pygame.font.Font('Data/Fonts/AVENGEANCE.ttf', 50)

#fondo del menu
background_menu = pygame.image.load('Data/Images/background.jpg')
background_menu = pygame.transform.scale(background_menu,(1280, 720))
#textos
titulo = fuente1.render('pydakar death ', True, color_titulo)
Boton_iniciar = fuente2.render('iniciar partida', True, color_botones)
Boton_guardada = fuente3.render('partida guardada', True, color_botones)
Boton_fama = fuente3.render('salon de la fama', True, color_botones)
Boton_info = fuente3.render('info de desarrolladores', True, color_botones)
Boton_salir =  fuente3.render('salir del juego', True, color_botones)

#VARIABLES DE OBJETOS EN PANTALLA DURANTE EL JUEGO
misc = Clases.Misc()
nivel = 1
tamano_mapa = [screen_size[0]*10, screen_size[1]*10]
velocidad = nivel**2+4
enemigos = misc.generar_Enemigos(tamano_mapa[0], tamano_mapa[1], 100, 100, nivel**3+29, velocidad)
jugador = Clases.Jugador(0, tamano_mapa[1]-100, 100, 100, "Data/Images/Audi.png", velocidad)
mapa = Clases.Mundo(0,-(tamano_mapa[1]+screen_size[1]), tamano_mapa[0], tamano_mapa[1], velocidad)

def main_menu():
    global Boton_fama, Boton_guardada, Boton_info, Boton_iniciar, Boton_salir, game, menu
    win.blit(background_menu,(0,0))
    win.blit(titulo,(0,20))
    win.blit(Boton_iniciar,(50, 270))
    win.blit(Boton_guardada,(50, 350))
    win.blit(Boton_fama, (50, 400))
    win.blit (Boton_info, (50, 570))
    win.blit (Boton_salir, (50, 620))

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(mouse)
    if 50 < mouse[0] < 470 and 270 < mouse[1] < 330:
        if click:
            game = True
            menu = False
        Boton_iniciar = fuente2.render("iniciar partida",True, (255,255,255))
    else:
        Boton_iniciar = fuente2.render('iniciar partida', True, color_botones)

    if 50 < mouse[0] < 372 and 350 < mouse[1] < 390:
        if click:
            pass
        Boton_guardada = fuente3.render('partida guardada', True, (255,255,255))
    else:
        Boton_guardada = fuente3.render('partida guardada', True, color_botones)

    if 50 < mouse[0] < 345 and 340 < mouse[1] < 440:
        if click:
            pass
        Boton_fama = fuente3.render('salon de la fama', True, (255,255,255))
    else:
        Boton_fama = fuente3.render('salon de la fama', True, color_botones)
    
    if 50 < mouse[0] < 320 and 620< mouse[1] < 660:
        if click:
            pass
        Boton_info = fuente3.render('info de desarrolladores', True, (255,255,255))
    else:
        Boton_info = fuente3.render('info de desarrolladores', True, color_botones)

    if 50 < mouse[0] < 320 and 620< mouse[1] < 660:
        if click:
            pass
        Boton_salir =  fuente3.render('salir del juego', True, (255,255,255))
    else:
        Boton_salir =  fuente3.render('salir del juego', True, color_botones)


def game_process(nivel):
    mapa.move()
    jugador.move(tamano_mapa[0], tamano_mapa[1])
    jugador.check_collide()
    jugador.check_death()
    for sprites in enemigos:
        sprites.check_collide()
        sprites.check_death()
    for sprites in Clases.Proyectil.lista.sprites():
        sprites.check_collide(Carros)
        sprites.move(tamano_mapa[0], tamano_mapa[1])
    mapa.draw(win)
    jugador.draw(mapa.image)
    for sprites in enemigos:
        sprites.move(tamano_mapa[0], tamano_mapa[1])



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if menu:
        main_menu()

    if game:
        game_process(nivel)
        
    pygame.display.update()

pygame.quit()


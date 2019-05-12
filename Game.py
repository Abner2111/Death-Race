from Clases import *
from pygame import *

pygame.init()
screen_size = [1280, 720]
map_size = [screen_size[0]*10, screen_size[1]*10]

win = pygame.display.set_mode((screen_size[0], screen_size[1]))



#VARIABLES DE  MODO
run = True #variable que mantiene el ciclo principal
menu_inicial = True #variable que activa el menu de inicio
pausa = False #variable que
juego = False
nivel = 1

#variables de objetos en pantalla
Mapa = Mundo(0, 0, map_size[0], map_size[1], nivel*50)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.time.delay(10)
    Mapa.move()
    win.fill((0,0,0))
    Mapa.draw(win)
    display.update()
pygame.quit()





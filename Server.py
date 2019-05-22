from Clases import *
from pygame import *
import socket

pygame.init()
screen_size = [1280, 720]
#map_size = [screen_size[0]*10, screen_size[1]*10]

win = pygame.display.set_mode((screen_size[0], screen_size[1]))


#PARAMETROS POR DEFECTO
ip = "0.0.0.0"
puerto = 9797
dataConnection = (ip, puerto)
conexionesMaximas = 4

#CREACION DEL SERVIDOR

socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketServidor.bind(dataConnection)
socketServidor.listen(conexionesMaximas)

#VARIABLES PARA SERVER
cliente, direccion = socketServidor.accept()

#VARIABLES DE  MODO
run = True #variable que mantiene el ciclo principal
menu_inicial = True #variable que activa el menu de inicio
pausa = False #variable que
juego = False
nivel = 1




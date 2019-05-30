import pygame
import json
import Clases

class Misc:

    def __init__(self):
        pass

    def save_to_json(self, name1, name2, data):
        file = open('Data/Datastore/'+name1+'_'+name2+'.json', 'w+')
        json.dump(data, file)

    def game(self, jugador_s, jugador_c):




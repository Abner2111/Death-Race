import pygame
import csv
import json


class General(pygame.sprite.Sprite): #clase general
    allsprites = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_string):
        pygame.sprite.Sprite.__init__ (self)
        General.allsprites.add(self)
        self.carga_imagen = pygame.image.load(image_string)
        self.image = pygame.transform.scale(self.carga_imagen, (width, height))
        self.rect = self.image.get_rect ()
        self.width = width
        self.height = height
        self.rect.centerx = x
        self.rect.centery = y

    def draw (self, surface):  # "dibuja" a los objetos en pantalla
        surface.blit(self.image, (self.rect.x - self.rect.width / 2, self.rect.y - self.rect.height))

    def destroy (self, ClassName):  # destruye sprite
        ClassName.lista.remove (self)
        General.allsprites.remove(self)
        del self
class Mundo(General):
    def __init__ (self, x, y, width, height, image_string, vel):
        General.__init__(self, x, y, width, height, image_string)
        self.vel = vel

    def move(self):
        def move (self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.x += self.vel
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.x -= self.vel
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.y += self.vel
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.y -= self.vel

class Carros(General):
    lista = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_string, vel):
        General.__init__(self, x, y, width, height, image_string)
        Carros.lista.add(self)
        self.vel = vel

    def move(self):
        pass


class Jugador(Carros):
    lista = pygame.sprite.Group()
    def __init__(self, x, y, width, height, image_string):
        Carros.__init__(self, x, y, width, height, image_string)
        Carros.lista.add(self)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            pos_fondo[0] += self.vel
            self.x -= self.vel
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            pos_fondo[0] -= self.vel
            self.x += self.vel
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            pos_fondo[1] -= self.vel
            self.y += self.vel
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            pos_fondo[1] += self.vel
            self.y -= self.vel


    
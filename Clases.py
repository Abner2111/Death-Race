import pygame
import csv
import json
import random
import math

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

    def draw(self, surface):  # "dibuja" a los objetos en pantalla
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
        def move(self):
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
    def __init__(self, x, y, width, height, image_string, vel):
        Carros.__init__(self, x, y, width, height, image_string, vel)
        Carros.lista.add(self)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.vel
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.vel
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.vel
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.vel


class Enemigo(Carros):
    lista = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_string, vel):
        Carros.__init__(self, x, y, width, height, image_string, vel)
        Carros.lista.add(self)
        self.velx = 0
        self.vely = 0

    def rand_spawn(self, fondo):
        if random.randrange(100) > 95:
            self.draw(fondo)
            self.componentes_velocidad()

    def componentes_velocidad(self): #toma la velocidad definida y la dirige a una direccion aleatoria, descomponiendo la velocidad en componentes
        radianes = random.randrange(0, 2*math.pi, 0.02) #genera un numero aleatorio de radianes entre 0 y 2*pi, con un intervalo de 0. 2(approx. un grado)
        x = round(self.vel*math.cos(radianes), 3)
        y = round(self.vel*math.sin(radianes), 3)
        self.velx = x
        self.vely = y

    def move(self, s_width, s_height): #mueve el vehiculo enemigo
        if self.rect.x == s_width or self.rect.x == 0:
            self.velx = -self.velx
        if self.rect.y == s_height or self.rect.y ==0:
            self.vely = -self.vely
        self.rect.x += self.velx
        self.rect.y += self.vely




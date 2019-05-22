import pygame
import random
import math

color_arena= (238, 182, 70)
class General(pygame.sprite.Sprite): #clase general
    allsprites = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_string): #construye instancia con posicion x, y ancho y alto e imagen
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
    lista = pygame.sprite.Group()

    def __init__(self, x, y, width, height,  vel):
        General.__init__(self, x, y, width, height, image_string='Data/Images/sand.jpg')
        self.vel = vel

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x += self.vel
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x -= self.vel
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.vel
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.vel
    def draw(self, surface):
        pygame.draw.rect(surface, color_arena, (0,0,self.width, self.height))



class Carros(General):
    lista = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_string, vel):
        General.__init__(self, x, y, width, height, image_string)
        Carros.lista.add(self)
        self.vel = vel
        self.vida = 15
        self.direc = 0

    def check_collide(self):
        if self.rect.collide_rect(Proyectil.lista):
            self.vida -= 1.5
        elif self.rect.collide_rect(Carros.lista):
            self.vida -= 3

    def check_death(self):
        if self.vida <= 0:
            self.destroy(Carros)

class Jugador(Carros):
    lista = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_string, vel):
        Carros.__init__(self, x, y, width, height, image_string, vel)
        Jugador.lista.add(self)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.vel
            if self.direc == 0:
                self.image = pygame.transform.rotate(self.image, 90)
            elif self.direc == 1:
                self.image = pygame.transform.rotate(self.image, 180)
            elif self.direc == 3:
                self.image = pygame.transform.rotate(self.image, -90)
            self.direc = 2     
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.vel
            if self.direc == 0:
                self.image = pygame.transform.rotate(self.image, -90)
            elif self.direc == 2:
                self.image = pygame.transform.rotate(self.image, 180)
            elif self.direc == 3:
                self.image = pygame.transform.rotate(self.image, 90)
            self.direc = 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.vel
            if self.direc == 0:
                self.image = pygame.transform.rotate(self.image, 180)
            elif self.direc == 1:
                self.image = pygame.transform.rotate(self.image, -90)
            elif self.direc == 2:
                self.image = pygame.transform.rotate(self.image, 90)
            self.direc = 3
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.rect.y -= self.vel
    def disparar(self):
        if self.direc == 0:
            vel_disparo = [0,-self.vel*2]
            pos == [self.rect.centerx+self.width/2, self.rect.centery+10]
        elif self.direc == 1:
            vel_disparo = [self.vel*2,0]
            pos = [self.rect.centerx+self.width+10, self.rect.centery/2]
        elif self.direc == 2:
            vel_disparo = [-self.vel*2,0]
            pos = [self.centerx-10, self.rect.centery/2]
        else:
            vel_disparo = [0,self.vel*2]
            pos = 
        

class Enemigo(Carros):
    lista = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_string, vel):
        Carros.__init__(self, x, y, width, height, image_string, vel)
        Enemigo.lista.add(self)
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
            self.image  = pygame.transform.flip(self.image, True, False) #refleja la imagen en el eje x
        if self.rect.y == s_height or self.rect.y == 0:
            self.vely = -self.vely
            self.image  = pygame.transform.flip(self.image, False, True)#refleja la imagen en el eje y
        self.rect.x += self.velx
        self.rect.y += self.vely


class Proyectil(General):

    lista = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_string, [velx, vely]):
        General.__init__ (self, x, y, width, height, image_string)
        Proyectil.lista.add()
        self.velx = velx
        self.vely = vely

    def move(self):
        if not self.rect.collide_rect(Carros.lista):
            self.rect.y += self.vely
            self.rect.x += self.velx
        else:
            self.destroy(Proyectil)


class Obstaculo (General):

    lista = pygame.sprite.Group()
    
    def __init__(self, x, y, widt, height, image_string):
        General.__init__(self, x, y, widt, height, image_string)
        Obstaculo.lista.add()
    

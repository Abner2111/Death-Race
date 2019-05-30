import pygame
import random
import math
import json
from network import Network

WIDTH = 800
HEIGHT = 600
FPS = 60
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Death Race")
clock = pygame.time.Clock()
color_arena= (238, 182, 70)
#MUSICA DE FONDO MENU
pygame.mixer.music.load('Sounds/race.mp3')

pygame.mixer.music.play(-1)


class General(pygame.sprite.Sprite): #clase general

    allsprites = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_string):
        pygame.sprite.Sprite.__init__(self)
        General.allsprites.add(self)
        self.carga_imagen = pygame.image.load(image_string)
        self.image = pygame.transform.scale(self.carga_imagen, (width, height)) #escala la imagen a width y height
        self.rect = self.image.get_rect() #saca el area del objeto
        self.width = width #ancho
        self.height = height #alto
        self.rect.centerx = x
        self.rect.centery = y
        

    def draw(self, surface):
        """
        Entrada: self y la superficie en que se desea dibujar
        Descripcion: dibuja al objeto en pantalla dadas las coordenadas y tamano en __init__()
        """
        surface.blit(self.image, (self.rect.x - self.rect.width / 2, self.rect.y - self.rect.height/2))

    def destroy (self, ClassName):
        """
        Entrada: self y la clase a la que pertenece el objeto
        Descripcion: Destruye al sprite removiendolo del grupo general y de su clase
        """
        ClassName.lista.remove (self)
        General.allsprites.remove(self)
        del self


class Mundo(General):
    lista = pygame.sprite.Group()

    def __init__(self, x, y, width, height,  vel, image_string = 'Data/Images/sand.jpg'):
        General.__init__(self, x, y, width, height, image_string)
        self.vel = vel

    def move(self):
        """
        Entrada: self
        Descripcion: Mueve el fondo respecto a la superficie indicada en el la funcion draw(). En este caso, sera la pantalla
        Nota: Se mueve en direccion contraria al jugador para mantener a este en pantalla
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x += self.vel
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x -= self.vel
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.vel
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.vel


class Carros(General):
    lista = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_string, vel):
        General.__init__(self, x, y, width, height, image_string)
        Carros.lista.add(self)
        self.vel = vel
        self.vida = 15
        self.direc = 0 #direccion del carro: 0 es arriba, 1 es derecha, 2 es izquierda y 3 es abajo
        self.net = Network()
        self.width = w
        self.height = h
        self.player = Jugador(50, 50)
        self.player2 = Jugador(100,100)
        self.canvas = Canvas(self.width, self.height, "Death_race")


    def check_death(self):
        """
        Entrada: self
        Descripcion: si la vida del carro es 0, lo destruye
        """
        if self.vida <= 0:
            self.destroy(Carros)
            return True
        else:
            return False


class Jugador(Carros):
    lista = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_string, vel):
        Carros.__init__(self, x, y, width, height, image_string, vel)
        Jugador.lista.add(self)
    
    def run(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.K_ESCAPE:
                    run = False
            keys = pygame.key.get_pressed()

            if keys[pygame.K_RIGHT]:
                if self.player.x <= self.width - self.player.velocity:
                    self.player.move(0)

            if keys[pygame.K_LEFT]:
                if self.player.x >= self.player.velocity:
                    self.player.move(1)

            if keys[pygame.K_UP]:
                if self.player.y >= self.player.velocity:
                    self.player.move(2)

            if keys[pygame.K_DOWN]:
                if self.player.y <= self.height - self.player.velocity:
                    self.player.move(3)

    def move(self, width, height):
        """
        Entrada: self
        Descripcion: cambia las coordenadas xy de acuerdo a las pulsaciones de las teclas a w s d
                    y a la velocidad dada en __init__ y tomando en cuenta si se encuentra en alguno de los bordes del mapa. Ademas rota la imagen en la direccion de movimiento, tomando
                    en cuenta la direccion anterior; 1 = derecha, 2 = izquierda, 0 = arriba, 3 = abajo
        """
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and 0 <= self.rect.centerx :
            self.rect.x -= self.vel
            if self.direc == 0:
                self.image = pygame.transform.rotate(self.image, 90)
            elif self.direc == 1:
                self.image = pygame.transform.rotate(self.image, 180)
            elif self.direc == 3:
                self.image = pygame.transform.rotate(self.image, -90)
            self.direc = 2     
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.centerx+self.width <= width:
            self.rect.x += self.vel
            if self.direc == 0:
                self.image = pygame.transform.rotate(self.image, -90)
            elif self.direc == 2:
                self.image = pygame.transform.rotate(self.image, 180)
            elif self.direc == 3:
                self.image = pygame.transform.rotate(self.image, 90)
            self.direc = 1
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.rect.centery+self.height <= height:
            self.rect.y += self.vel
            if self.direc == 0:
                self.image = pygame.transform.rotate(self.image, 180)
            elif self.direc == 1:
                self.image = pygame.transform.rotate(self.image, -90)
            elif self.direc == 2:
                self.image = pygame.transform.rotate(self.image, 90)
            self.direc = 3
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and 0 <= self.rect.centery:
            self.rect.y -= self.vel
            if self.direc == 1:
                self.image = pygame.transform.rotate(self.image, 90)
            elif self.direc == 2:
                self.image = pygame.transform.rotate(self.image, -90)
            elif self.direc == 3:
                self.image = pygame.transform.rotate(self.image, 180)
            self.direc = 3
        #enviar info
            self.player2.x, self.player2.y = self.parse_data(self.send_data())

            # Actualizar Canvas
            self.canvas.draw_background()
            self.player.draw(self.canvas.get_canvas())
            self.player2.draw(self.canvas.get_canvas())
            self.canvas.update()

    def check_collide(self):
        """
        Entrada: self
        Descripcion: revisa si self ha colisionado con algun objeto y, de ser asi, le rebaja la vida correspondiente a
        cada tipo de objeto
        """
        if  Misc.colisiona(self, Proyectil):
            self.vida -= 1.5
        elif  Misc.colisiona(self, Enemigo):
            self.vida -= 3
    
        elif  Misc.colisiona(self, Cactus) or Misc.colisiona(self, Roca):
            self.vida -= 1
        elif  Misc.colisiona(self, Mina):
            self.vida -= 5
    def disparar(self):
        """
        Entrada: self
        Descripcion: retorna una instancia de la clase Proyectil. Con la posicion asociada al frente del carro del que
                    se está disparando.
        """
        if self.direc == 0:
            vel_disparo = (0,-self.vel*2)
            pos = [self.rect.centerx+self.width/2, self.rect.centery+10]
        elif self.direc == 1:
            vel_disparo = (self.vel*2,0)
            pos = [self.rect.centerx+self.width+10, self.rect.centery/2]
        elif self.direc == 2:
            vel_disparo = (-self.vel*2,0)
            pos = [self.rect.centerx-10, self.rect.centery/2]
        else:
            vel_disparo = (0,self.vel*2)
            pos = [self.rect.centerx+self.width/2, self.rect.centery+self.height+10]
        return Proyectil(pos[0], pos[1], 50, 50, vel_disparo[0], vel_disparo[1])
        

class Enemigo(Carros):

    lista = pygame.sprite.Group()

    def __init__(self, x, y, width, height,vel, image_string="Data/Images/Audi.png"):
        Carros.__init__(self, x, y, width, height, image_string, vel)
        Enemigo.lista.add(self)
        self.velx = 0
        self.vely = 0


    def check_collide(self):
        """
        Entrada: self
        Descripcion: revisa si self ha colisionado con algun objeto y, de ser asi, le rebaja la vida correspondiente a
        cada tipo de objeto
        """
        if  Misc.colisiona(self, Proyectil):
            self.vida -= 1.5
        elif  Misc.colisiona(self, Jugador):
            self.vida -= 3
        elif  Misc.colisiona(self, Cactus) or Misc.colisiona(self, Roca):
            self.vida -= 1
        elif  Misc.colisiona(self, Mina):
            self.vida -= 5

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

        pygame.quit()

    def send_data(self):
        """
        Enviar posicion al server
        :return: None
        """
        data = str(self.net.id) + ":" + str(self.player.x) + "," + str(self.player.y)
        reply = self.net.send(data)
        return reply

    @staticmethod
    def parse_data(data):
        try:
            d = data.split(":")[1].split(",")
            return int(d[0]), int(d[1])
        except:
            return 0,0


class Canvas:

    def __init__(self, w, h, name="None"):
        self.width = w
        self.height = h
        self.screen = pygame.display.set_mode((w,h))
        pygame.display.set_caption(name)

    @staticmethod
    def update():
        pygame.display.update()

    def draw_text(self, text, size, x, y):
        pygame.font.init()
        font = pygame.font.SysFont("comicsans", size)
        render = font.render(text, 1, (0,0,0))

        self.screen.draw(render, (x,y))

    def get_canvas(self):
        return self.screen
    def draw_background(self):
        self.screen.fill((238, 182, 70))



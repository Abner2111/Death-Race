import sys, math, random, time, traceback
import pygame
import Clases
MENU_DIMENSIONS = WIDTH, HEIGHT = 700, 560
SCREEN_DIMENSIONS = None
pygame.init()
game = None
entity = None
UI = None
animations = None

random.seed()

screen = pygame.display.set_mode(MENU_DIMENSIONS)
load_screen = pygame.image.load('Images/banner.png')
menu_background = None
#UI groups
playermenu = pygame.sprite.Group()
mapmenu = pygame.sprite.Group()
gamemenu = pygame.sprite.Group()
winmenu = pygame.sprite.Group()
#game groups
live_entities = pygame.sprite.Group()
karts = pygame.sprite.Group()
winners = []
map_img = None
signal_img = None
#winscreen groups
podium_karts = pygame.sprite.Group()

selected_map = None
countdown = 3
mode_time = time.time()
fps = 0
gamemode = 0
players = 1
#30 updates per second
pacing = 10
update_timer = 0
powerup_respawn = 32
powerup_timer = 0

readytoload = False

def get_karts():
    global karts
    return karts

def current_ui():
    #returns the current UI
    global gamemode
    if gamemode == 0:
        return playermenu
    elif gamemode == 1:
        return mapmenu
    elif gamemode == 2:
        return gamemenu
    elif gamemode == 3:
        return winmenu

def set_gamemode(value):
    #safe assignment of gamemode
    global gamemode, mode_time
    if value == '-':
        gamemode -= 1
        return
    gamemode = value
    mode_time = time.time()
    print('* gamemode = ', gamemode)

def exit_game(state, error = None):
    print('exiting game with state ', str(state))
    pygame.quit()
    if error: raise error
    sys.exit()

def select_players():
    #display the player selection UI
    set_gamemode(0)

def set_players(value):
    #assigns values for an n-player game
    global players
    players = value
    print('* players = ', players)
    select_map()

def select_map():
    #display the map selection UI
    set_gamemode(1)

def set_map(map_number):
    #records map choice
    global readytoload, selected_map
    readytoload = True
    mapmenu.sprites()[1].set_image(image_name = 'button_start')
    #todo: add more maps
    selected_map = 'sprites/map_'
    selected_map += str(map_number)
    print('* map = ', map_number)
    pass

def loadscreen():
    #quickly displays a load screen
    screen = pygame.display.set_mode(MENU_DIMENSIONS)
    screen.fill((0, 0, 0))
    screen.blit(load_screen, ((WIDTH-load_screen.get_width())/2, (HEIGHT-load_screen.get_height())/2)) 
    pygame.display.update()

def load_game():
    #prepares
    global readytoload
    if not readytoload:
        return
    loadscreen()
    loadSprites_game01()
    set_gamemode(2)

def win_game01(winners):
    loadSprites_win(winners)
    set_gamemode(3)

def unload_game01():
    loadscreen()
    global live_entities, karts, podium_karts, cameras, winners, players
    live_entities = pygame.sprite.Group()
    karts = pygame.sprite.Group()
    podium_karts = pygame.sprite.Group()
    cameras = []
    winners = []
    players = 0
    set_gamemode(0)
    
def loadSprites_win(winners):
    import game_util
    print("< loading win screen")
    background = UI.Element(image_name = 'win_background')
    podium = UI.Element(image_name = 'img_podium', centered = True)
    button_playagain = UI.Button(image_name = 'button_playagain', pos = (0, 90), centered = True,
                                 onclick = unload_game01)
    button_quit = UI.Button(image_name = 'button_quit', pos = (0, 180), centered = True,
                            onclick = exit_game, arg = 1)
    #to be implemented
    button_stats = UI.Button(image_name = 'button_stats', pos = (0, 130), centered = True)
    
    for i in range(0, players):
        if i > 2:
            break
        if i == 0:
            p = (WIDTH/2, HEIGHT/2 - (podium.rect.height/2))
        elif i == 1:
            p = (WIDTH/2 - 92, HEIGHT/2 - 10 - (podium.rect.height*(1/8)))
        elif i == 2:
            p = (WIDTH/2 + 92, HEIGHT/2 - 10 + (podium.rect.height*(1/8)))
        kart = entity.Entity(image_name = winners[i], animation = game_util.animation_kart,
                             pos = p)
        podium_karts.add(kart)

    winmenu.add(background, podium, button_playagain, button_quit, button_stats)
    screen = pygame.display.set_mode(MENU_DIMENSIONS)
    print("> loaded win screen")
    
def loadSprites_game01():
    #loading images & instantiating sprites for game01
    print("< loading game")
    global entity, live_entities, gamemap, map_img, signal_img, SCREEN_DIMENSIONS, selected_map
    import game_entity
    import game_util
    entity = game_entity
    
    #map class placeholder
    print(selected_map)
    gamemap = game_util.load_Map(selected_map)
    map_img = gamemap.image
    signal_img = gamemap.signal
    print('- loaded maps')
    
    #karts
    for i in range(0, players):
        pos_data = gamemap.kart_spawns[i]
        posi = (pos_data[0], pos_data[1])
        rot = pos_data[2]
        if i == 0:
            kart = entity.Kart(pygame.K_w, pygame.K_d, pygame.K_a, pygame.K_e, image_name = 'mario',
                               pos = posi, rotation = rot,
                               animation = game_util.animation_kart)
        elif i == 1:
            kart = entity.Kart(pygame.K_i, pygame.K_l, pygame.K_j, pygame.K_o, image_name = 'peach',
                               pos = posi, rotation = rot,
                               animation = game_util.animation_kart)
        elif i == 2:
            kart = entity.Kart(pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_0, image_name = 'bowser',
                               pos = posi, rotation = rot,
                               animation = game_util.animation_kart)
        else:
            kart = entity.Kart(pygame.K_z, pygame.K_x, pygame.K_c, pygame.K_v, image_name = 'luigi',
                               pos = posi, rotation = rot,
                               animation = game_util.animation_kart)
        karts.add(kart)
    print('- loaded karts')
    
    #checkpoints and finish
    chs = gamemap.checkpoints
    for i in range(1, len(chs)):
        check_data = chs[i]
        check = entity.Checkpoint(stage = i-1, image_name = 'checkpoint',
                                  pos = (check_data[0], check_data[1]), rotation = check_data[2],
                                  animation = game_util.animation_checkpoint)
        live_entities.add(check)
    check_data = chs[0]
    finish = entity.Checkpoint(stage = len(chs)-1, image_name = 'finish',
                               pos = (check_data[0], check_data[1]), rotation = check_data[2],
                               animation = game_util.animation_checkpoint)
    live_entities.add(finish)
    print('- loaded checkpoints')

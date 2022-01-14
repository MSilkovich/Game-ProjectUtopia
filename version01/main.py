import pygame
import os
import sys
from Board import Board
from startScreen import start_screen
from Buildings import Castle_cl, Farm, IronMine, Quarry
from SETTINGS import MYEVENTTYPE_farm, MYEVENTTYPE_castle, can_build, MYEVENTTYPE_ironmine, grids, mountains,\
    MYEVENTTYPE_quarry


pygame.init()
clock = pygame.time.Clock()
start = True

n = 0
FPS = 50
warn = False

board = Board(20, 20)

castle_sprites = pygame.sprite.Group()
farm_sprites = pygame.sprite.Group()
ironmine_sprites = pygame.sprite.Group()
quarry_sprites = pygame.sprite.Group()


def draw_rect(spis):
    pygame.draw.rect(spis[0], spis[1], spis[2])

    font = pygame.font.SysFont('arial', 20)
    for i in info:
        string_rendered = font.render(i, True, (255, 255, 255))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = ry + spis[5]
        intro_rect.x = rx + spis[6]
        screen.blit(string_rendered, intro_rect)


def draw_polygon(spis):
    pygame.draw.polygon(spis[0], spis[1], spis[2], spis[3])


def terminate():
    pygame.quit()
    sys.exit()


def update_bg():
    screen.blit(fon, (0, 0))


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def gradientRect(window, left_colour, right_colour, target_rect):
    colour_rect = pygame.Surface((2, 2))  # tiny! 2x2 bitmap
    pygame.draw.line(colour_rect, left_colour, (0, 0), (0, 1))  # left colour line
    pygame.draw.line(colour_rect, right_colour, (1, 0), (1, 1))  # right colour line
    colour_rect = pygame.transform.smoothscale(colour_rect, (target_rect.width, target_rect.height))  # stretch!
    window.blit(colour_rect, target_rect)  # paint it


def show_info(coords, screen):
    x = coords[0]
    y = coords[1]
    coords = 65
    if x >= 0 and x <= 50 and y >= 10 and y <= 60:
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (103, 0, 0), (50, 60, 450, 200))
        info = ["Пища - сновной ресурс для выживания вашего города.",
                "Количество пищи влияет на численность населения и",
                "его состояние. Пища используется для найма армии,",
                "строительства, развития науки и культуры."]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, True, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 55
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif x >= 50 and x <= 199 and y >= 10 and y <= 60:
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (103, 0, 0), (200, 60, 450, 200))
        info = ["Источники"]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, True, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 205
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif x >= 200 and x <= 250 and y >= 10 and y <= 60:
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (103, 0, 0), (250, 60, 450, 150))
        info = ["Древесина - основной строительный материал вашего",
                "города, из древесины строятся основные экономические",
                "здания. Древесину можно добыть в лесах."]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, True, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 255
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif x >= 250 and x <= 400 and y >= 10 and y <= 60:
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (103, 0, 0), (250, 60, 450, 200))
        info = ["Источники"]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, True, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 255
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif x >= 400 and x <= 450 and y >= 10 and y <= 60:
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (103, 0, 0), (450, 60, 475, 150))
        info = ["Камень - строительный ресурс для некоторых ",
                "сооружений и улучшения стен в поздней игре. Добывается",
                "в каменных залежах с пристроенным карьером."]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, True, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 455
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif x >= 450 and x <= 600 and y >= 10 and y <= 60:
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (103, 0, 0), (450, 60, 450, 200))
        info = ["Источники"]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, True, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 455
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif x >= 600 and x <= 650 and y >= 10 and y <= 60:
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (103, 0, 0), (650, 60, 450, 150))
        info = ["Железо - полезный стратегический ресурс. Используется",
                "для тренировки сильных войск. Добывается в железных",
                "жилах с пристроеным рудником."]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, True, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 655
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif x >= 650 and x <= 800 and y >= 10 and y <= 60:
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (103, 0, 0), (650, 60, 450, 200))
        info = ["Источники"]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, True, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 655
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif x >= 800 and x <= 850 and y >= 10 and y <= 60:
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (103, 0, 0), (850, 60, 450, 200))
        info = ["Золото - используется для найма проф армии, для",
                "развития науки и культуры и для постройки некоторых",
                "зданий. Добывается в золотых жилах с пристроенным",
                "рудником."]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, True, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 855
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif x >= 850 and x <= 1000 and y >= 10 and y <= 60:
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (103, 0, 0), (850, 60, 450, 200))
        info = ["Источники"]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, True, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 855
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif x >= 1000 and x <= 1050 and y >= 10 and y <= 60:
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (103, 0, 0), (1050, 60, 450, 100))
        info = ["Наука - изучайте улучшения, получайте бонусы.",
                "Увеличивается специальными постройками."]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, True, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 1055
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif x >= 1050 and x <= 1200 and y >= 10 and y <= 60:
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (103, 0, 0), (1050, 60, 450, 200))
        info = ["Источники"]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, True, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 1055
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif x >= 1200 and x <= 1250 and y >= 10 and y <= 60:
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (103, 0, 0), (1250, 60, 470, 150))
        info = ["Культура и вера - получайте доходы с мероприятий,",
                "повышайте счастье народа. Увеличиваются специальными",
                "постройками."]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, True, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 1255
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif x >= 1250 and x <= 1400 and y >= 10 and y <= 60:
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (103, 0, 0), (1250, 60, 450, 200))
        info = ["Источники"]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, True, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 1255
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif x >= 1400 and x <= 1450 and y >= 10 and y <= 60:
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (103, 0, 0), (1450, 60, 475, 150))
        info = ["Население - главный фактор вашего города, из них",
                "набирается армия, оно добывает ресурсы. Повышается от",
                "избытка пищи и счастья."]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, True, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 1455
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif x >= 1450 and x <= 1600 and y >= 10 and y <= 60:
        screen.blit(fon, (0, 0))
        global diseases
        dis = load_image('diseases .png')
        pygame.draw.rect(screen, (103, 0, 0), (1450, 60, 450, 200))
        screen.blit(dis, (1455, 65))
        info = [f"болеющие - {diseases}",
                "Прирост за день - "]
        font = pygame.font.SysFont('arial', 45)
        n = 0
        for i in info:
            if n == 0:
                string_rendered = font.render(i, True, (255, 0, 0))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = coords
                intro_rect.x = 1510
                coords += 40
                coords += intro_rect.height
                screen.blit(string_rendered, intro_rect)
                n = 1
            else:
                string_rendered = font.render(i, True, (0, 255, 0))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = coords
                intro_rect.x = 1455
                coords += 20
                coords += intro_rect.height
                screen.blit(string_rendered, intro_rect)
    elif x >= 1600 and x <= 1650 and y >= 10 and y <= 60:
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (103, 0, 0), (1125, 60, 475, 150))
        info = ["Счастье - влияет на добычу ресурсов, возникновение",
                "восстаний и количество населения. Увеличивается",
                "количеством ресурсов и постройкой культурных зданий."]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, True, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 1130
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif x >= 1650 and x <= 1800 and y >= 10 and y <= 60:
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (103, 0, 0), (1225, 60, 450, 200))
        info = ["Источники"]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, True, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 1230
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    else:
        board.update()
        board.draw(screen)


castle = Castle_cl(load_image('castle/castle_anim2.png'), 5, 1, 960, 650, castle_sprites)
pygame.time.set_timer(MYEVENTTYPE_castle, 1000)

farm, ironmine, quarry = "", "", ""

start_screen()

warn_width, warn_color, warn_word, farmcord, ironminecord, quarrycord = 340, (255, 0, 0), "", (0, 0), (0, 0), (0, 0)

size = WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

resourses, buildings = [], []
food, wood, stone, iron, gold, science, culture, population, happiness, diseases = \
    100, 0, 100, 100, 0, 0, 0, 1000, 60, 0

foodplus, woodplus, stoneplus, ironplus, goldplus, scienceplus, cultureplus, populationplus,\
happinessplus, diseasesplus = 0, 0, 0, 0, 10, 0, 0, 1, 0, 0

resourses.append(load_image('food.png'))
resourses.append(load_image('wood.png'))
resourses.append(load_image('stone.png'))
resourses.append(load_image('iron.png'))
resourses.append(load_image('gold.png'))
resourses.append(load_image('science.png'))
resourses.append(load_image('culture.png'))
resourses.append(load_image('population.png'))
resourses.append(load_image('happiness .png'))
fon = load_image('background.jpg')

running = True
y, v = 10, 20

while running:
    warn_rect, warn_polygon = [], []
    # print(board.grid_pos)

    if not warn:
        update_bg()
        show_info(pygame.mouse.get_pos(), screen)

    if warn:
        info = [warn_word]

        if board.grid_pos in buildings and can_build == False:
            info = ["Сейчас строится здание, подождите!"]
        elif board.grid_pos in buildings and can_build == True:
            info = ["На этом месте уже стоит постройка!"]

        if info[0] == "Сейчас строится здание, подождите!":
            warn_width = 350
        elif info[0] == "На этом месте уже стоит постройка!":
            warn_width = 350
        elif info[0] == "Вы не можете строить здание на этой территории!":
            warn_width = 480
        elif info[0] == "Вы не можете строить рудники не в горах!":
            warn_width = 400
        elif info[0] == "Вы не можете строить ферму в горах!":
            warn_width = 360

        mx, my = pygame.mouse.get_pos()

        if board.grid_pos[1] < 0 and not ((board.grid_pos[0] == 1 or board.grid_pos[0] == 0 or board.grid_pos[0] == 2
                                           or board.grid_pos[0] == 3) and board.grid_pos[1] == -1) and not \
                ((board.grid_pos[0] == 3 or board.grid_pos[0] == 2) and board.grid_pos[1] == -2) and not \
                ((board.grid_pos[0] == 4 or board.grid_pos[0] == 3) and board.grid_pos[1] == -3) and not \
                ((board.grid_pos[0] == 4 or board.grid_pos[0] == 3 or board.grid_pos[0] == 5) and
                 board.grid_pos[1] == -4) and not ((board.grid_pos[0] == 5 or board.grid_pos[0] == 6) and
                 board.grid_pos[1] == -5) and not ((board.grid_pos[0] == 7 or board.grid_pos[0] == 6) and
                 board.grid_pos[1] == -6) and not ((board.grid_pos[0] == 7 or board.grid_pos[0] == 8) and
                 board.grid_pos[1] == -7) and not ((board.grid_pos[0] == 8 or board.grid_pos[0] == 9) and
                 board.grid_pos[1] == -8) and not ((board.grid_pos[0] == 10 or board.grid_pos[0] == 9) and
                 board.grid_pos[1] == -9):  # iso_poly2
            coords1 = board.iso_poly2[3]
            rx, ry = coords1
            if ((mx > rx + 200) or (mx < rx - warn_width) or (my > ry + 53) or (my < ry - 53)):
                warn = False
            screen.blit(fon, (0, 0))

            ry_c, rx_c = -34, 5 - warn_width
            warn_rect = [screen, (103, 0, 0), (rx - warn_width, ry - 35, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - warn_width, ry - 50, 200 + warn_width, 100), 1)
            warn_polygon = [screen, warn_color, board.iso_poly2, 3]

        elif board.grid_pos[0] == 3 and board.grid_pos[1] == -1:
            coords1 = board.iso_poly2[3]
            rx, ry = coords1
            if ((mx > rx + warn_width + 200) or (mx < rx) or (my > ry + 53) or (my < ry - 53)):
                warn = False
            screen.blit(fon, (0, 0))

            ry_c, rx_c = -34, 205
            warn_rect = [screen, (103, 0, 0), (rx + 200, ry - 35, warn_width, 35), ry, rx, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx, ry - 50, 200 + warn_width, 100), 1)
            warn_polygon = [screen, warn_color, board.iso_poly2, 3]

        elif (board.grid_pos[0] == 17 and board.grid_pos[1] <= 3) or\
                (board.grid_pos[0] == 18 and board.grid_pos[1] <= 3) or\
                (board.grid_pos[0] == 19 and board.grid_pos[1] <= 3) or\
                (board.grid_pos[0] == 20 and board.grid_pos[1] <= 3):
            coords1 = board.iso_poly1[3]
            rx, ry = coords1
            if ((mx > rx + 200) or (mx < rx - warn_width) or (my > ry + 53) or (my < ry - 53)):
                warn = False
            screen.blit(fon, (0, 0))

            ry_c, rx_c = -34, 5 - warn_width
            warn_rect = [screen, (103, 0, 0), (rx - warn_width, ry - 35, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - warn_width, ry - 50, 200 + warn_width, 100), 1)
            warn_polygon = [screen, warn_color, board.iso_poly1, 3]

        elif ((board.grid_pos[0] == 0 or board.grid_pos[0] == 1) and board.grid_pos[1] == 0) or\
                (board.grid_pos[0] == 1 and board.grid_pos[1] == 1): # draw right down iso_poly1
            coords1 = board.iso_poly1[0]
            rx, ry = coords1
            if ((mx > rx + warn_width) or (mx < rx - 100) or (my > ry + 123) or (my < ry)):
                warn = False
            screen.blit(fon, (0, 0))

            ry_c, rx_c = 105, 5
            warn_rect = [screen, (103, 0, 0), (rx, ry + 100, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - 100, ry, warn_width + 100, 135), 1)
            warn_polygon = [screen, warn_color, board.iso_poly1, 3]

        elif board.grid_pos[0] == 2 and (board.grid_pos[1] == 1 or board.grid_pos[1] == 2):
            coords1 = board.iso_poly1[0]
            rx, ry = coords1
            if ((mx > rx + warn_width) or (mx < rx - 100) or (my > ry + 123) or (my < ry)):
                warn = False
            screen.blit(fon, (0, 0))

            ry_c, rx_c = 105, 5
            warn_rect = [screen, (103, 0, 0), (rx, ry + 100, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - 100, ry, warn_width + 100, 135), 1)
            warn_polygon = [screen, warn_color, board.iso_poly1, 3]

        elif (board.grid_pos[0] == 1 or board.grid_pos[0] == 0 or board.grid_pos[0] == 2)\
                and (board.grid_pos[1] == -1): # right iso_poly2
            coords1 = board.iso_poly2[2]
            rx, ry = coords1
            if ((mx > rx + warn_width) or (mx < rx - 100) or (my > ry + 34) or (my < ry - 83)):
                warn = False
            screen.blit(fon, (0, 0))

            ry_c, rx_c = 8, 5
            warn_rect = [screen, (103, 0, 0), (rx, ry, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - 100, ry - 100, warn_width + 102, 136), 1)
            warn_polygon = [screen, warn_color, board.iso_poly2, 3]

        elif (board.grid_pos[0] == 2 or board.grid_pos[0] == 3) and board.grid_pos[1] == -2:
            coords1 = board.iso_poly2[2]
            rx, ry = coords1
            if ((mx > rx + warn_width) or (mx < rx - 100) or (my > ry + 34) or (my < ry - 83)):
                warn = False
            screen.blit(fon, (0, 0))

            ry_c, rx_c = 8, 5
            warn_rect = [screen, (103, 0, 0), (rx, ry, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - 100, ry - 100, warn_width + 102, 136), 1)
            warn_polygon = [screen, warn_color, board.iso_poly2, 3]

        elif (board.grid_pos[0] == 3 or board.grid_pos[0] == 4) and board.grid_pos[1] == -3:
            coords1 = board.iso_poly2[2]
            rx, ry = coords1
            if ((mx > rx + warn_width) or (mx < rx - 100) or (my > ry + 34) or (my < ry - 83)):
                warn = False
            screen.blit(fon, (0, 0))

            ry_c, rx_c = 8, 5
            warn_rect = [screen, (103, 0, 0), (rx, ry, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - 100, ry - 100, warn_width + 102, 136), 1)
            warn_polygon = [screen, warn_color, board.iso_poly2, 3]

        elif (board.grid_pos[0] == 3 or board.grid_pos[0] == 4 or board.grid_pos[0] == 5) and board.grid_pos[1] == -4:
            coords1 = board.iso_poly2[2]
            rx, ry = coords1
            if ((mx > rx + warn_width) or (mx < rx - 100) or (my > ry + 34) or (my < ry - 83)):
                warn = False
            screen.blit(fon, (0, 0))

            ry_c, rx_c = 8, 5
            warn_rect = [screen, (103, 0, 0), (rx, ry, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - 100, ry - 100, warn_width + 102, 136), 1)
            warn_polygon = [screen, warn_color, board.iso_poly2, 3]

        elif (board.grid_pos[0] == 5 or board.grid_pos[0] == 6) and board.grid_pos[1] == -5:
            coords1 = board.iso_poly2[2]
            rx, ry = coords1
            if ((mx > rx + warn_width) or (mx < rx - 100) or (my > ry + 34) or (my < ry - 83)):
                warn = False
            screen.blit(fon, (0, 0))

            ry_c, rx_c = 8, 5
            warn_rect = [screen, (103, 0, 0), (rx, ry, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - 100, ry - 100, warn_width + 102, 136), 1)
            warn_polygon = [screen, warn_color, board.iso_poly2, 3]

        elif (board.grid_pos[0] == 7 or board.grid_pos[0] == 6) and board.grid_pos[1] == -6:
            coords1 = board.iso_poly2[2]
            rx, ry = coords1
            if ((mx > rx + warn_width) or (mx < rx - 100) or (my > ry + 34) or (my < ry - 83)):
                warn = False
            screen.blit(fon, (0, 0))

            ry_c, rx_c = 8, 5
            warn_rect = [screen, (103, 0, 0), (rx, ry, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - 100, ry - 100, warn_width + 102, 136), 1)
            warn_polygon = [screen, warn_color, board.iso_poly2, 3]

        elif (board.grid_pos[0] == 8 or board.grid_pos[0] == 7) and board.grid_pos[1] == -7:
            coords1 = board.iso_poly2[2]
            rx, ry = coords1
            if ((mx > rx + warn_width) or (mx < rx - 100) or (my > ry + 34) or (my < ry - 83)):
                warn = False
            screen.blit(fon, (0, 0))

            ry_c, rx_c = 8, 5
            warn_rect = [screen, (103, 0, 0), (rx, ry, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - 100, ry - 100, warn_width + 102, 136), 1)
            warn_polygon = [screen, warn_color, board.iso_poly2, 3]

        elif (board.grid_pos[0] == 8 or board.grid_pos[0] == 9) and board.grid_pos[1] == -8:
            coords1 = board.iso_poly2[2]
            rx, ry = coords1
            if ((mx > rx + 100) or (mx < rx - warn_width) or (my > ry + 34) or (my < ry - 83)):
                warn = False
            screen.blit(fon, (0, 0))

            ry_c, rx_c = 8, -warn_width
            warn_rect = [screen, (103, 0, 0), (rx - warn_width, ry, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - warn_width, ry - 100, warn_width + 102, 136), 1)
            warn_polygon = [screen, warn_color, board.iso_poly2, 3]

        elif (board.grid_pos[0] == 10 or board.grid_pos[0] == 9) and board.grid_pos[1] == -9:
            coords1 = board.iso_poly2[2]
            rx, ry = coords1
            if ((mx > rx + 100) or (mx < rx - warn_width) or (my > ry + 34) or (my < ry - 83)):
                warn = False
            screen.blit(fon, (0, 0))

            ry_c, rx_c = 8, -warn_width
            warn_rect = [screen, (103, 0, 0), (rx - warn_width, ry, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - warn_width, ry - 100, warn_width + 102, 136), 1)
            warn_polygon = [screen, warn_color, board.iso_poly2, 3]

        elif (board.grid_pos[0] == 16 or board.grid_pos[0] == 15) and board.grid_pos[1] == 0: # draw left iso_poly1
            coords1 = board.iso_poly1[1]
            rx, ry = coords1
            if ((mx > rx) or (mx < rx - warn_width - 200) or (my > ry + 53) or (my < ry - 53)):
                warn = False
            screen.blit(fon, (0, 0))

            ry_c, rx_c = -34, -warn_width - 195
            warn_rect = [screen, (103, 0, 0), (rx - 200 - warn_width, ry - 35, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - warn_width - 200, ry - 50, 200 + warn_width, 100), 1)
            warn_polygon = [screen, warn_color, board.iso_poly1, 3]

        else: # iso_poly1
            coords1 = board.iso_poly1[1]
            rx, ry = coords1
            if ((mx > rx + warn_width) or (mx < rx - 200) or (my > ry + 53) or (my < ry - 53)):
                warn = False
            screen.blit(fon, (0, 0))

            ry_c, rx_c = - 34, 5
            warn_rect = [screen, (103, 0, 0), (rx, ry - 35, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - 200, ry - 50, 200 + warn_width, 100), 1)
            warn_polygon = [screen, warn_color, board.iso_poly1, 3]

    farm_sprites.draw(screen)
    castle_sprites.draw(screen)
    quarry_sprites.draw(screen)
    ironmine_sprites.draw(screen)

    if len(warn_rect) != 0:
        draw_rect(warn_rect)
    if len(warn_polygon) != 0:
        draw_polygon(warn_polygon)

    x = 0
    res_values = [str(food)[0:3], str(wood)[0:3], str(stone)[0:3], str(iron)[0:3], str(gold)[0:3],
                  str(science)[0:3], str(culture)[0:3],
                  str(population)[0:4], str(happiness) + '%']
    coords = 80
    font = pygame.font.SysFont('arial', 40)
    for event in pygame.event.get():

        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            terminate()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if grids[board.grid_pos]:
                if can_build:
                    if event.button == 1:
                        if board.grid_pos not in mountains:
                            if board.grid_pos[1] >= 0:
                                farmcord = board.iso_poly1[3]
                            elif board.grid_pos[1] < 0:
                                farmcord = board.iso_poly2[3]
                            grids[board.grid_pos] = False
                            x_farm = farmcord[0] + 65
                            y_farm = farmcord[1] - 50
                            farm = Farm(load_image('farm_3.png'), 3, 1, x_farm, y_farm, farm_sprites)
                            buildings.append(board.grid_pos)
                            foodplus += 10
                            pygame.time.set_timer(MYEVENTTYPE_farm, 3000)
                            print(MYEVENTTYPE_farm)
                            can_build = False

                        else:
                            warn_word = "Вы не можете строить ферму в горах!"
                            warn = True

                    elif event.button == 4:
                        if board.grid_pos in mountains:
                            if board.grid_pos[1] >= 0:
                                quarrycord = board.iso_poly1[3]
                            elif board.grid_pos[1] < 0:
                                quarrycord = board.iso_poly2[3]
                            x_quarry = quarrycord[0] + 45
                            y_quarry = quarrycord[1] - 50
                            grids[board.grid_pos] = False
                            quarry = Quarry(load_image('quarry.png'), 3, 1, x_quarry,
                                                y_quarry, quarry_sprites)
                            buildings.append(board.grid_pos)
                            stoneplus += 10
                            pygame.time.set_timer(MYEVENTTYPE_quarry, 3000)
                            print(MYEVENTTYPE_quarry)
                            can_build = False

                        else:
                            warn_word = "Вы не можете строить каменоломню не в горах!"
                            warn = True

                    elif event.button == 3:
                        if board.grid_pos in mountains:
                            if board.grid_pos[1] >= 0:
                                ironminecord = board.iso_poly1[3]
                            elif board.grid_pos[1] < 0:
                                ironminecord = board.iso_poly2[3]
                            x_ironmine = ironminecord[0] + 45
                            y_ironmine = ironminecord[1] - 50
                            grids[board.grid_pos] = False
                            ironmine = IronMine(load_image('ironmine.png'), 3, 1, x_ironmine,
                                                y_ironmine, ironmine_sprites)
                            buildings.append(board.grid_pos)
                            ironplus += 10
                            pygame.time.set_timer(MYEVENTTYPE_ironmine, 3000)
                            can_build = False

                        else:
                            warn_word = "Вы не можете строить рудники не в горах!"
                            warn = True

                else:
                    warn_word = "Сейчас строится здание, подождите!"
                    warn = True

            else:
                warn_word = "Вы не можете строить здание на этой территории!"
                warn = True

        if event.type == MYEVENTTYPE_farm:
            if farm.n < 2:
                farm.update()
                pygame.time.set_timer(MYEVENTTYPE_farm, 3000)
            if farm.n == 2:
                can_build = True
                farm.builded = True
                print('you can build')

        if event.type == MYEVENTTYPE_castle:
            castle.update()
            pygame.time.set_timer(MYEVENTTYPE_castle, 150)

        if event.type == MYEVENTTYPE_ironmine:
            if ironmine.m < 2:
                ironmine.update()
                pygame.time.set_timer(MYEVENTTYPE_ironmine, 3000)
            if ironmine.m == 2:
                can_build = True
                ironmine.builded = True
                print('you can build')

        if event.type == MYEVENTTYPE_quarry:
            if quarry.m < 2:
                quarry.update()
                pygame.time.set_timer(MYEVENTTYPE_quarry, 3000)
            if quarry.m == 2:
                can_build = True
                quarry.builded = True
                print('you can build')

    for i in resourses:
        screen.blit(i, (x, y))
        pygame.draw.rect(screen, (37, 23, 5), (x + 50, y, 150, 50), 1)
        pygame.draw.rect(screen, (47, 27, 0), (x + 51, y + 1, 198, 48), 1)
        pygame.draw.rect(screen, (103, 0, 0), (x + 52, y + 2, 196, 46))
        x += 200

    for i in res_values:
        string_rendered = font.render(i, True, (255, 255, 255))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = 10
        intro_rect.x = coords
        coords += 152
        coords += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    pygame.display.flip()
    food += foodplus * clock.tick() / 15000
    stone += stoneplus * clock.tick()
    iron += ironplus * clock.tick() / 5000
    print(food, stone, iron)
    clock.tick(FPS)

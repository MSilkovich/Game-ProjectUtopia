import pygame
import os
import sys
from startScreen import start_screen
from Board import Board
from Castle import Castle


pygame.init()
clock = pygame.time.Clock()
start = True
n = 0

FPS = 50


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def terminate():
    pygame.quit()
    sys.exit()

def update_bg():
    screen.blit(fon, (0, 0))


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
            string_rendered = font.render(i, 1, (255, 255, 255))
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
            string_rendered = font.render(i, 1, (255, 255, 255))
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
            string_rendered = font.render(i, 1, (255, 255, 255))
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
            string_rendered = font.render(i, 1, (255, 255, 255))
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
            string_rendered = font.render(i, 1, (255, 255, 255))
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
            string_rendered = font.render(i, 1, (255, 255, 255))
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
            string_rendered = font.render(i, 1, (255, 255, 255))
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
            string_rendered = font.render(i, 1, (255, 255, 255))
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
            string_rendered = font.render(i, 1, (255, 255, 255))
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
            string_rendered = font.render(i, 1, (255, 255, 255))
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
            string_rendered = font.render(i, 1, (255, 255, 255))
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
            string_rendered = font.render(i, 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 1055
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif x >= 1200 and x <= 1250 and y >= 10 and y <= 60:
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (103, 0, 0), (1250, 60, 470, 150))
        info = ["Культура и вера - получайте длоходы с мероприятий,",
                "повышайте счастье народа. Увеличиваются специальными",
                "постройками."]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, 1, (255, 255, 255))
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
            string_rendered = font.render(i, 1, (255, 255, 255))
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
            string_rendered = font.render(i, 1, (255, 255, 255))
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
                string_rendered = font.render(i, 1, (255, 0, 0))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = coords
                intro_rect.x = 1510
                coords += 40
                coords += intro_rect.height
                screen.blit(string_rendered, intro_rect)
                n = 1
            else:
                string_rendered = font.render(i, 1, (0, 255, 0))
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
            string_rendered = font.render(i, 1, (255, 255, 255))
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
            string_rendered = font.render(i, 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 1230
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    else:
        screen.blit(fon, (0, 0))
        global board
        board = Board(20, 20)
        board.set_view(0, 0, 100)
        board.update()
        board.draw(screen)


castle_sprites = pygame.sprite.Group()
castle = Castle(960, 650)
castle_sprites.add(castle)

start_screen()
size = WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
resourses, buildings = [], []
food, wood, stone, iron, gold, science, culture, population, happiness, diseases = \
    600, 400, 200, 0, 0, 0, 0, 1000, 60, 0
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
y = 10
v = 20
while running:
    x = 0
    res_values = [str(food)[0:3], str(wood)[0:3], str(stone)[0:3], str(iron)[0:3], str(gold)[0:3],
                  str(science)[0:3], str(culture)[0:3],
                  str(population)[0:4], str(happiness) + '%']
    coords = 80
    font = pygame.font.SysFont('arial', 40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            terminate()
        if event.type == pygame.MOUSEMOTION:
            show_info(event.pos, screen)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()
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
    castle.update()
    castle_sprites.draw(screen)
    pygame.display.flip()
    food += v * clock.tick() / 2000
    clock.tick(FPS)

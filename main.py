import pygame
import os
import sys
from startScr import start_screen
from Board import Board
from Buildings import Farm, Castle_cl, Mill
from TYPES_TIMERS import type_farm, type_castle, type_res, type_mill, type_days

pygame.init()
clock = pygame.time.Clock()
start = True
n = 0
all_sprites = pygame.sprite.Group()
castle_sprites = pygame.sprite.Group()
farm_sprites = pygame.sprite.Group()
mill_sprites = pygame.sprite.Group()
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
        info = ["Зололто - используется для найма проф армии, для",
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
        pygame.draw.rect(screen, (103, 0, 0), (1250, 60, 475, 150))
        info = ["Население - главный фактор вашего города, из них",
                "набирается армия, оно добывает ресурсы. Повышается от",
                "избытка пищи и счастья."]
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
        global diseases
        dis = load_image('diseases .png')
        pygame.draw.rect(screen, (103, 0, 0), (1250, 60, 450, 200))
        screen.blit(dis, (1255, 65))
        info = [f"болеющие - {diseases}",
                "Прирост за день - "]
        font = pygame.font.SysFont('arial', 45)
        n = 0
        for i in info:
            if n == 0:
                string_rendered = font.render(i, 1, (255, 0, 0))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = coords
                intro_rect.x = 1310
                coords += 40
                coords += intro_rect.height
                screen.blit(string_rendered, intro_rect)
                n = 1
            else:
                string_rendered = font.render(i, 1, (0, 255, 0))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = coords
                intro_rect.x = 1255
                coords += 20
                coords += intro_rect.height
                screen.blit(string_rendered, intro_rect)
    elif x >= 1400 and x <= 1450 and y >= 10 and y <= 60:
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
    elif x >= 1450 and x <= 1600 and y >= 10 and y <= 60:
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
    elif x >= 1600 and x <= 1800 and y >= 10 and y <= 60:
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (103, 0, 0), (1475, 60, 475, 150))
        info = ["Количество пройденых вами дней"]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 1475
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    else:

        global board
        board = Board(20, 20)
        board.set_view(0, 0, 100)
        board.update()
        board.draw(screen)
        all_sprites.draw(screen)
        castle_sprites.draw(screen)
        farm_sprites.draw(screen)
        mill_sprites.draw(screen)
        # print(board.iso_poly1)


start_screen()
size = WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
resourses = []
food, wood, stone, iron, gold, science, population, happiness, diseases, days = \
    600, 400, 200, 0, 0, 0, 1000, 60, 0, 0
foodplus, woodplus, stoneplus, ironplus, goldplus, scienceplus, populationplus,\
happinessplus, diseasesplus = 1, 1, 0, 0, 10, 0, 1, 0, 0
resourses.append(load_image('food.png'))
resourses.append(load_image('wood.png'))
resourses.append(load_image('stone.png'))
resourses.append(load_image('iron.png'))
resourses.append(load_image('gold.png'))
resourses.append(load_image('science.png'))
resourses.append(load_image('population.png'))
resourses.append(load_image('happiness .png'))
resourses.append(load_image('days.png'))
fon = load_image('background.jpg')
running = True
y = 10
v = 20
class BUildFarm:
    def __init__(self, position, butHeigth, butWidth, text):
        self.position = position
        self.width = butWidth
        self.heigth = butHeigth
        self.text = text
        self.pos = menu.get_pos()

    def mouse_in(self, mous_pos):
        x, y = mous_pos
        px, py = self.position
        if x > px and x < px + self.width:
            if y > py and y < py + self.heigth:
                return True
            else:
                return False
        else:
            return False

    def render(self, screen):
        mousePos = pygame.mouse.get_pos()
        if self.mouse_in(mousePos):
            pygame.draw.rect(screen, (103, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
            if pygame.mouse.get_pressed()[0] and self.mouse_in(mousePos):
                global farm, food, wood, type_farm
                farm = Farm(load_image('farm.png'), 3, 1, self.pos[0], self.pos[1], farm_sprites, type_farm)
                pygame.time.set_timer(type_farm, 3000)
                menu.ok = False
                food -= 50
                wood -= 200
        else:
            pygame.draw.rect(screen, (0, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))


class BuildMill(BUildFarm):
    def __init__(self, position: tuple, butHeigth: int = 40, butWidth: int = 150, text: str = "Кнопка"):
        super().__init__(position, butHeigth, butWidth, text)
        self.pos = menu.get_pos()

    def render(self, screen):
        mousePos = pygame.mouse.get_pos()
        if self.mouse_in(mousePos):
            pygame.draw.rect(screen, (103, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
            if pygame.mouse.get_pressed()[0] and self.mouse_in(mousePos):
                global mill, food, wood, type_mill
                mill = Mill(load_image('mill.png'), 3, 1, self.pos[0], self.pos[1], mill_sprites, type_mill)
                pygame.time.set_timer(type_mill, 5000)
                menu.ok = False
                food -= 200
                wood -= 25
        else:
            pygame.draw.rect(screen, (0, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))


class BuildMenu:
    def __init__(self, screen, x, y, lx, ly, side, buildx, buildy):
        self.x = x
        self.y = y
        self.width = 200
        self.heigth = 350
        self.position = (board.iso_poly1[3][0] + self.width, board.iso_poly2[3][1] + self.heigth)
        self.screen = screen
        self.fdres = load_image('foodres.png')
        self.wdres = load_image('woodres.png')
        self.food = ['Ферма -',  '- 50', '- 100']
        self.mill = ['Лесопилка -', '- 200', '- 25']
        self.ok = False
        self.lx = lx
        self.ly = ly
        self.side = side
        self.bx = buildx
        self.by = buildy

    def get_pos(self):
        return self.bx, self.by

    def show_list(self):
        ms = pygame.mouse.get_pos()
        # print(ms, self.x, self.y, self.lx, self.ly)
        if self.ok:
            if self.side == 1:
                pygame.draw.polygon(self.screen, (255, 0, 0), [[self.x + 200, self.y],
                                                         [self.x + 200, self.ly + 50], [self.lx, self.ly + 50],
                                                         [self.lx, self.y]], 1)
            elif self.side == 2:
                pygame.draw.polygon(self.screen, (255, 0, 0), [[self.lx, self.y],
                                                               [self.lx, self.ly + 50], [self.x, self.ly + 50],
                                                               [self.x, self.y]], 1)
            pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, self.width, self.heigth))
            font = pygame.font.SysFont('arial', 18)
            butfr = BUildFarm(position=(self.x + 10, self.y + 5), butHeigth=60, butWidth=175, text='')
            butfr.render(self.screen)
            self.screen.blit(self.fdres, (self.x + 70, self.y + 10))
            self.screen.blit(self.wdres, (self.x + 70, self.y + 40))
            string_rendered = font.render(self.food[0], 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = self.y + 10
            intro_rect.x = self.x + 10
            screen.blit(string_rendered, intro_rect)
            string_rendered = font.render(self.food[1], 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = self.y + 10
            intro_rect.x = self.x + 100
            screen.blit(string_rendered, intro_rect)
            string_rendered = font.render(self.food[2], 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = self.y + 40
            intro_rect.x = self.x + 100
            butml = BuildMill(position=(self.x + 10, self.y + 75), butHeigth=60, butWidth=175, text='')
            butml.render(self.screen)
            self.screen.blit(self.fdres, (self.x + 100, self.y + 80))
            self.screen.blit(self.wdres, (self.x + 100, self.y + 110))
            screen.blit(string_rendered, intro_rect)
            string_rendered = font.render(self.mill[0], 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = self.y + 80
            intro_rect.x = self.x + 10
            screen.blit(string_rendered, intro_rect)
            string_rendered = font.render(self.mill[1], 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = self.y + 80
            intro_rect.x = self.x + 130
            screen.blit(string_rendered, intro_rect)
            string_rendered = font.render(self.mill[2], 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = self.y + 110
            intro_rect.x = self.x + 130
            screen.blit(string_rendered, intro_rect)
        if (self.side == 1) and \
                (not (ms[0] >= self.lx and ms[0] <= self.x + 200 and ms[1] >= self.y and ms[1] <= self.ly + 50)):
            self.ok = False
        elif (self.side == 2) and \
                (not (ms[0] <= self.lx and ms[0] >= self.x and ms[1] >= self.y and ms[1] <= self.ly + 50)):
            self.ok = False


board = Board(20, 20)
board.set_view(0, 0, 100)
pygame.time.set_timer(type_res, 1000)
pygame.time.set_timer(type_days, 60000)
menu = BuildMenu(screen, 0, 0, 0, 0, 0, 0, 0)
farm = Farm(load_image('farm.png'), 3, 1, -300, -300, farm_sprites, type_farm)
mill = Mill(load_image('mill.png'), 3, 1, -300, -300, mill_sprites, type_farm)
castle = Castle_cl(load_image('castle_anim2.png'), 5, 1, 960, 650, castle_sprites)
pygame.time.set_timer(type_castle, 150)
while running:
    x = 0
    menu.show_list()
    if not menu.ok:
        screen.blit(fon, (0, 0))
        show_info(pygame.mouse.get_pos(), screen)
        all_sprites.draw(screen)
        farm_sprites.draw(screen)
        mill_sprites.draw(screen)
    res_values = [str(round(food)), str(round(wood)), str(round(stone)), str(round(iron)), str(round(gold)),
                  str(round(science)), str(round(population)), str(round(happiness)) + '%', str(round(days))]
    coords = 80
    font = pygame.font.SysFont('arial', 40)
    menu.show_list()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            terminate()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()
        if event.type == pygame.MOUSEMOTION:
            pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                if board.grid_pos[1] >= 0:
                    cord = board.iso_poly1[1]
                    x1 = cord[0]
                    y1 = cord[1]
                    lx = board.iso_poly1[3][0]
                    ly = board.iso_poly1[3][1]
                    stayx = lx + 45
                    stayy = ly - 50
                    side = 1
                    if y1 >= 540:
                        y1 -= 300
                    else:
                        y1 -= 50
                        ly += 250
                    menu = BuildMenu(screen, x1, y1, lx, ly, 1, stayx, stayy)
                elif board.grid_pos[1] < 0:
                    cord = board.iso_poly2[3]
                    x1 = cord[0] - 200
                    y1 = cord[1]
                    lx = board.iso_poly2[1][0]
                    ly = board.iso_poly2[1][1]
                    stayx = x1 + 245
                    stayy = y1 - 50
                    side = 2
                    if y1 >= 540:
                        y1 -= 300
                    else:
                        y1 -= 50
                        ly += 250
                    menu = BuildMenu(screen, x1, y1, lx, ly, 2, stayx, stayy)
                menu.ok = True
        if event.type == type_farm:
            if farm.n == 1:
                foodplus += 10
            farm.update()
        if event.type == type_mill:
            if mill.n == 1:
                woodplus += 10
            mill.update()
        if event.type == type_res:
            food += foodplus
            wood += woodplus
        if event.type == type_days:
            days += 1
        if event.type == type_castle:
            castle.update()
            castle_sprites.draw(screen)
    menu.show_list()
    for i in resourses:
        screen.blit(i, (x, y))
        pygame.draw.rect(screen, (37, 23, 5), (x + 50, y, 150, 50), 1)
        pygame.draw.rect(screen, (47, 27, 0), (x + 51, y + 1, 198, 48), 1)
        pygame.draw.rect(screen, (103, 0, 0), (x + 52, y + 2, 196, 46))
        x += 200
    for i in res_values:
        string_rendered = font.render(i, 1, (255, 255, 255))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = 10
        intro_rect.x = coords
        coords += 152
        coords += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    pygame.display.flip()
    clock.tick(FPS)

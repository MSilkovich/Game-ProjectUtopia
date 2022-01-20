from startScreen import start_screen
from Board2 import Board
from Buildings2 import *
from SETTINGS import *

pygame.mixer.music.load('data/music/witcher3.mp3')
pygame.mixer.music.set_volume(0.01)
pygame.mixer.music.play(-1)

pygame.init()
clock = pygame.time.Clock()
start = True
n, warn = 0, False

all_sprites = pygame.sprite.Group()
castle_sprites = pygame.sprite.Group()
farm_sprites = pygame.sprite.Group()
mill_sprites = pygame.sprite.Group()
iron_mine_sprites = pygame.sprite.Group()
FPS = 50


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def update_bg():
    screen.blit(fon, (0, 0))


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
        draw_board()

    all_sprites.draw(screen)
    castle_sprites.draw(screen)
    farm_sprites.draw(screen)
    mill_sprites.draw(screen)


def draw_board():
    global board
    board = Board(20, 20)
    board.set_view(0, 0, 100)
    board.update()
    board.draw(screen)


start_screen()
size = WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

resourses, buildings = [], []

food, wood, stone, iron, gold, science, population, happiness, diseases, days = \
    600, 400, 200, 0, 0, 0, 1000, 60, 0, 0
foodplus, woodplus, stoneplus, ironplus, goldplus, scienceplus, populationplus, \
happinessplus, diseasesplus = 1, 1, 0, 0, 1, 0, 1, 0, 0

resourses.append(load_image('images/food.png'))
resourses.append(load_image('images/wood.png'))
resourses.append(load_image('images/stone.png'))
resourses.append(load_image('images/iron.png'))
resourses.append(load_image('images/gold.png'))
resourses.append(load_image('images/science.png'))
resourses.append(load_image('images/population.png'))
resourses.append(load_image('images/happiness .png'))
resourses.append(load_image('images/days.png'))
fon = load_image('images/background.jpg')

running = True
y, v = 10, 20


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
                global farm, food, wood, type_farm, can_build, grids, board
                farm = Farm(load_image('images/farm_3.png'), 3, 1, self.pos[0] + 20, self.pos[1], farm_sprites, type_farm)
                pygame.time.set_timer(type_farm, 3000)
                menu.ok = False
                food -= 50
                wood -= 200
                can_build = False
                grids[board.grid_pos] = False
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
                global mill, food, wood, type_mill, can_build, grids, board
                mill = Mill(load_image('mill.png'), 3, 1, self.pos[0], self.pos[1], mill_sprites, type_mill)
                pygame.time.set_timer(type_mill, 5000)
                menu.ok = False
                food -= 200
                wood -= 25
                can_build = False
                grids[board.grid_pos] = False
        else:
            pygame.draw.rect(screen, (0, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))


class BuildIronMine(BUildFarm):
    def __init__(self, position: tuple, butHeigth: int = 40, butWidth: int = 150, text: str = "Кнопка"):
        super().__init__(position, butHeigth, butWidth, text)
        self.pos = menu.get_pos()

    def render(self, screen):
        mousePos = pygame.mouse.get_pos()
        if self.mouse_in(mousePos):
            pygame.draw.rect(screen, (103, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
            if pygame.mouse.get_pressed()[0] and self.mouse_in(mousePos):
                global ironmine, food, wood, type_ironmine, can_build, grids, board
                ironmine = IronMine(load_image('ironmine.png'), 3, 1, self.pos[0], self.pos[1], iron_mine_sprites,
                            type_ironmine)
                pygame.time.set_timer(type_ironmine, 7000)
                menu.ok = False
                food -= 175
                wood -= 125
                can_build = False
                grids[board.grid_pos] = False
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
        self.fdres = load_image('images/foodres.png')
        self.wdres = load_image('images/woodres.png')
        self.food = ['Ферма -',  '- 50', '- 100']
        self.mill = ['Лесопилка -', '- 200', '- 25']
        self.ironmine = ['Железный -', '-175', '-75', 'рудник']
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
            if board.grid_pos not in mountains:
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
            else:
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
                butfr = BuildIronMine(position=(self.x + 10, self.y + 5), butHeigth=60, butWidth=175, text='')
                butfr.render(self.screen)
                self.screen.blit(self.fdres, (self.x + 100, self.y + 10))
                self.screen.blit(self.wdres, (self.x + 100, self.y + 40))
                string_rendered = font.render(self.ironmine[0], 1, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = self.y + 10
                intro_rect.x = self.x + 10
                screen.blit(string_rendered, intro_rect)
                string_rendered = font.render(self.ironmine[3], 1, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = self.y + 40
                intro_rect.x = self.x + 10
                screen.blit(string_rendered, intro_rect)
                string_rendered = font.render(self.ironmine[1], 1, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = self.y + 10
                intro_rect.x = self.x + 130
                screen.blit(string_rendered, intro_rect)
                string_rendered = font.render(self.ironmine[2], 1, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = self.y + 40
                intro_rect.x = self.x + 130
                screen.blit(string_rendered, intro_rect)
        if (self.side == 1) and \
                (not (ms[0] >= self.lx and ms[0] <= self.x + 200 and ms[1] >= self.y and ms[1] <= self.ly + 50)):
            self.ok = False

        elif (self.side == 2) and \
                (not (ms[0] <= self.lx and ms[0] >= self.x and ms[1] >= self.y and ms[1] <= self.ly + 50)):
            self.ok = False


board = Board(20, 20)
# board.set_view(0, 0, 100)

pygame.time.set_timer(type_res, 1000)
pygame.time.set_timer(type_days, 60000)

menu = BuildMenu(screen, 0, 0, 0, 0, 0, 0, 0)
farm = Farm(load_image('images/farm_3.png'), 3, 1, -300, -300, farm_sprites, type_farm)
mill = Mill(load_image('images/mill.png'), 3, 1, -300, -300, mill_sprites, type_farm)
ironmine = IronMine(load_image('images/ironmine.png'), 3, 1, -300, -300, iron_mine_sprites, type_ironmine)
castle = Castle_cl(load_image('images/castle/castle_anim2.png'), 5, 1, 960, 650, castle_sprites)

pygame.time.set_timer(type_castle, 150)

pygame.mixer.music.load('data/music/witcher3.mp3')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

warn_width, warn_color, warn_word, farmcord, ironminecord, quarrycord = 340, (255, 0, 0), "", (0, 0), (0, 0), (0, 0)

# pygame.mixer.music.load('')
while running:
    x = 0

    warn_rect, warn_polygon = [], []
    # print(board.grid_pos)

    # if not menu.ok:
    #     draw()
    #     show_info(pygame.mouse.get_pos(), screen)

    if menu.ok:
        update_bg()
        draw_polygon([screen, (255, 255, 255), board.iso_poly1, 3])
        draw_polygon([screen, (255, 255, 255), board.iso_poly2, 3])

    if not warn and not menu.ok:
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
                                                   board.grid_pos[1] == -5) and not (
                (board.grid_pos[0] == 7 or board.grid_pos[0] == 6) and
                board.grid_pos[1] == -6) and not ((board.grid_pos[0] == 7 or board.grid_pos[0] == 8) and
                                                  board.grid_pos[1] == -7) and not (
                (board.grid_pos[0] == 8 or board.grid_pos[0] == 9) and
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

        elif (board.grid_pos[0] == 17 and board.grid_pos[1] <= 3) or \
                (board.grid_pos[0] == 18 and board.grid_pos[1] <= 3) or \
                (board.grid_pos[0] == 19 and board.grid_pos[1] <= 3) or \
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

        elif ((board.grid_pos[0] == 0 or board.grid_pos[0] == 1) and board.grid_pos[1] == 0) or \
                (board.grid_pos[0] == 1 and board.grid_pos[1] == 1):  # draw right down iso_poly1
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

        elif (board.grid_pos[0] == 1 or board.grid_pos[0] == 0 or board.grid_pos[0] == 2) \
                and (board.grid_pos[1] == -1):  # right iso_poly2
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

        elif (board.grid_pos[0] == 16 or board.grid_pos[0] == 15) and board.grid_pos[1] == 0:  # draw left iso_poly1
            coords1 = board.iso_poly1[1]
            rx, ry = coords1
            if ((mx > rx) or (mx < rx - warn_width - 200) or (my > ry + 53) or (my < ry - 53)):
                warn = False
            screen.blit(fon, (0, 0))

            ry_c, rx_c = -34, -warn_width - 195
            warn_rect = [screen, (103, 0, 0), (rx - 200 - warn_width, ry - 35, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - warn_width - 200, ry - 50, 200 + warn_width, 100), 1)
            warn_polygon = [screen, warn_color, board.iso_poly1, 3]

        else:  # iso_poly1
            coords1 = board.iso_poly1[1]
            rx, ry = coords1
            if ((mx > rx + warn_width) or (mx < rx - 200) or (my > ry + 53) or (my < ry - 53)):
                warn = False
            screen.blit(fon, (0, 0))

            ry_c, rx_c = - 34, 5
            warn_rect = [screen, (103, 0, 0), (rx, ry - 35, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - 200, ry - 50, 200 + warn_width, 100), 1)
            warn_polygon = [screen, warn_color, board.iso_poly1, 3]

    if len(warn_rect) != 0:
        draw_rect(warn_rect)
    if len(warn_polygon) != 0:
        draw_polygon(warn_polygon)

    res_values = [str(round(food)), str(round(wood)), str(round(stone)), str(round(iron)), str(round(gold)),
                  str(round(science)), str(round(population)), str(round(happiness)) + '%', str(round(days))]
    coords = 80
    font = pygame.font.SysFont('arial', 40)
    castle_sprites.draw(screen)
    all_sprites.draw(screen)
    farm_sprites.draw(screen)
    mill_sprites.draw(screen)
    iron_mine_sprites.draw(screen)
    menu.show_list()

    for event in pygame.event.get():

        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            terminate()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if grids[board.grid_pos]:
                    if can_build:
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

                    else:
                        warn_word = "Сейчас строится здание, подождите!"
                        warn = True
                else:
                    warn_word = "Вы не можете строить здание на этой территории!"
                    warn = True

        if event.type == type_farm:
            if farm.n == 1:
                foodplus += 10
                can_build = True
            farm.update()

        if event.type == type_mill:
            if mill.n == 1:
                woodplus += 10
                can_build = True
            mill.update()

        if event.type == type_res:
            food += foodplus
            wood += woodplus
            iron += ironplus
            stone += stoneplus
            gold += goldplus
            population += populationplus

        if event.type == type_days:
            days += 1

        if event.type == type_castle:
            castle.update()

        if event.type == type_ironmine:
            if ironmine.n == 1:
                ironplus += 10
                can_build = True
            ironmine.update()

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
    clock.tick(FPS)

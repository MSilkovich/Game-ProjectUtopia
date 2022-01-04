import pygame
import os
import sys


pygame.init()
size = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
os.environ['SDL_VIDEO_CENTERED'] = '1'
start = True
n = 0

FPS = 50


class StartButton:
    def __init__(self, position: tuple, butHeigth: int = 40, butWidth: int = 150, text: str = "Кнопка"):
        self.position = position
        self.width = butWidth
        self.heigth = butHeigth
        self.text = text

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
            pygame.draw.rect(screen, (0, 50, 255), (self.position[0], self.position[1], self.width, self.heigth))
            if pygame.mouse.get_pressed()[0] and self.mouse_in(mousePos):
                global start
                start = False
        elif pygame.mouse.get_pressed() and self.mouse_in(mousePos):
            pygame.draw.rect(screen, (102, 0, 0), (50, 50, 200, 200))
        else:
            pygame.draw.rect(screen, (102, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
        self.font = pygame.font.Font(pygame.font.get_default_font(), 30)
        valueSurf = self.font.render(f"{self.text}", True, (51, 51, 51))
        textx = self.position[0] + (self.width / 2) - (valueSurf.get_rect().width / 2)
        texty = self.position[1] + (self.heigth / 2) - (valueSurf.get_rect().height / 2)
        screen.blit(valueSurf, (textx, texty))


class ConButton(StartButton):
    def __init__(self, position: tuple, butHeigth: int = 40, butWidth: int = 150, text: str = "Кнопка"):
        super().__init__(position)
        self.position = position
        self.width = butWidth
        self.heigth = butHeigth
        self.text = text

    def render(self, screen):
        mousePos = pygame.mouse.get_pos()
        if self.mouse_in(mousePos):
            pygame.draw.rect(screen, (0, 50, 255), (self.position[0], self.position[1], self.width, self.heigth))
            # if pygame.mouse.get_pressed()[0] and self.mouse_in(mousePos):
            #     global start
            #     start = False
        elif pygame.mouse.get_pressed() and self.mouse_in(mousePos):
            pygame.draw.rect(screen, (255, 0, 255), (50, 50, 200, 200))
        else:
            pygame.draw.rect(screen, (0, 0, 255), (self.position[0], self.position[1], self.width, self.heigth))
        self.font = pygame.font.Font(pygame.font.get_default_font(), 30)
        valueSurf = self.font.render(f"{self.text}", True, (255, 0, 0))
        textx = self.position[0] + (self.width / 2) - (valueSurf.get_rect().width / 2)
        texty = self.position[1] + (self.heigth / 2) - (valueSurf.get_rect().height / 2)
        screen.blit(valueSurf, (textx, texty))


class DescriptionButton(StartButton):
    def __init__(self, position: tuple, butHeigth: int = 40, butWidth: int = 150, text: str = "Кнопка"):
        super().__init__(position)
        self.position = position
        self.width = butWidth
        self.heigth = butHeigth
        self.text = text

    def render(self, screen):
        mousePos = pygame.mouse.get_pos()
        if self.mouse_in(mousePos):
            pygame.draw.rect(screen, (0, 50, 255), (self.position[0], self.position[1], self.width, self.heigth))
            if pygame.mouse.get_pressed()[0] and self.mouse_in(mousePos):
                intro_text = ['Описание:!',
                              'Средневековый город. В центре города - замок. По краям!',
                              'замка - крепостная стена. Вокруг крепостной стены - город.',
                              'Изначально игрок существует с очень маленьким городом.',
                              'Главная цель игры - сохранить город как можно дольше, ведь',
                              'город расположен на очень плодородных территориях,',
                              'на которую хочет посягнуть немало других феодалов.',
                              'Каждый день возможно осуществление многих сценариев:!',
                              'враги могут добавить яд в реки вашего города,',
                              'что грозит смертью многих жителей, их болезнью -> слабостью армии.',
                              'Вам придется потратить немало денег и ресурсов на восстановление',
                              'города и жизни в нем, возможно, весь город вымрет от яда.',
                              'Чтобы продержаться на плаву как можно дольше, грамотно',
                              'распределяйте ресурсы, стройте новые постройки.']
                font = pygame.font.Font(None, 30)
                text_coord = 25
                siz1 = 900, 600
                scr1 = pygame.display.set_mode(siz1)
                for line in intro_text:
                    if line[-1] == '!':
                        line = line.rstrip('!')
                        string_rendered = font.render(line, 1, (0, 125, 125))
                        intro_rect = string_rendered.get_rect()
                        text_coord += 10
                        intro_rect.top = text_coord
                        intro_rect.x = 150
                        text_coord += intro_rect.height
                        scr1.blit(string_rendered, intro_rect)
                    else:
                        string_rendered = font.render(line, 1, (0, 125, 125))
                        intro_rect = string_rendered.get_rect()
                        text_coord += 10
                        intro_rect.top = text_coord
                        intro_rect.x = 100
                        text_coord += intro_rect.height
                        scr1.blit(string_rendered, intro_rect)
                btn_start1 = StartButton((100, 450), butHeigth=100, butWidth=400, text='К игре!')
                while start:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            terminate()
                    btn_start1.render(scr1)
                    pygame.display.flip()
        elif pygame.mouse.get_pressed() and self.mouse_in(mousePos):
            pygame.draw.rect(screen, (255, 0, 255), (50, 50, 200, 200))
        else:
            pygame.draw.rect(screen, (0, 0, 255), (self.position[0], self.position[1], self.width, self.heigth))
        self.font = pygame.font.Font(pygame.font.get_default_font(), 30)
        valueSurf = self.font.render(f"{self.text}", True, (255, 0, 0))
        textx = self.position[0] + (self.width / 2) - (valueSurf.get_rect().width / 2)
        texty = self.position[1] + (self.heigth / 2) - (valueSurf.get_rect().height / 2)
        screen.blit(valueSurf, (textx, texty))


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

def start_screen():
    intro_text = ['Проект утопия']

    fon = pygame.transform.scale(load_image('fon.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    pygame.font.get_fonts()
    font = pygame.font.SysFont('arial', 80)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, (103, 0, 0))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 100
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    btn_start = StartButton((100, 200), butHeigth=50, butWidth=250, text='Старт')
    btn_continue = ConButton((100, 500), butHeigth=50, butWidth=250, text='Продолжить')
    btn_desc = DescriptionButton((100, 350), butHeigth=50, butWidth=250, text='Описание')
    # btn_settings = Button((100, 550), butHeigth=100, butWidth=400, text='Настройки')
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        btn_start.render(screen)
        btn_continue.render(screen)
        btn_desc.render(screen)
        # btn_settings.render(screen)
        pygame.display.flip()
        clock.tick(FPS)


class Board:
    def __init__(self, width, height, left=10, top=10, cell_size=30):
        self.width = width
        self.height = height
        self.board = [[0] * (width + 1) for i in range(height + 1)]
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255), (self.left + x * self.cell_size,
                                                           self.top + y * self.cell_size,
                                                           self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        print(mouse_pos)
        x = (mouse_pos[0] - self.left) // self.cell_size
        y = (mouse_pos[1] - self.top) // self.cell_size
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return None
        else:
            return x, y


def gradientRect( window, left_colour, right_colour, target_rect ):
    colour_rect = pygame.Surface( ( 2, 2 ) )                                   # tiny! 2x2 bitmap
    pygame.draw.line( colour_rect, left_colour,  ( 0,0 ), ( 0,1 ) )            # left colour line
    pygame.draw.line( colour_rect, right_colour, ( 1,0 ), ( 1,1 ) )            # right colour line
    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )  # stretch!
    window.blit( colour_rect, target_rect )                                    # paint it


def show_info(coords, screen):
    x = coords[0]
    y = coords[1]
    coords = 75
    if x >= 0 and x <= 50 and y >= 20 and y <= 70:
        pygame.draw.rect(screen, (103, 0, 0), (50, 70, 450, 200))
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
    elif x >= 200 and x <= 250 and y >= 20 and y <= 70:
        pygame.draw.rect(screen, (103, 0, 0), (250, 70, 450, 150))
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
    elif x >= 400 and x <= 450 and y >= 20 and y <= 70:
        pygame.draw.rect(screen, (103, 0, 0), (450, 70, 450, 150))
        info = ["Камень - строительный ресурс для некоторых сооружений",
                "и улучшения стен в поздней игре. Добывается в каменных",
                "залежах с пристроенным карьером."]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 455
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif x >= 600 and x <= 650 and y >= 20 and y <= 70:
        pygame.draw.rect(screen, (103, 0, 0), (650, 70, 450, 150))
        info = ["Железо - полезный стратегический ресурс. Используется",
                "для тренировки сильных войск. Добывается в железных",
                "жилах с пристроеным рудником"]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 655
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif x >= 800 and x <= 850 and y >= 20 and y <= 70:
        pygame.draw.rect(screen, (103, 0, 0), (850, 70, 450, 200))
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
    elif x >= 1000 and x <= 1050 and y >= 20 and y <= 70:
        pygame.draw.rect(screen, (103, 0, 0), (1050, 70, 450, 100))
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
    elif x >= 1200 and x <= 1250 and y >= 20 and y <= 70:
        pygame.draw.rect(screen, (103, 0, 0), (1250, 70, 470, 150))
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
    elif x >= 1400 and x <= 1450 and y >= 20 and y <= 70:
        pygame.draw.rect(screen, (103, 0, 0), (1450, 70, 475, 150))
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
    elif x >= 1600 and x <= 1650 and y >= 20 and y <= 70:
        pygame.draw.rect(screen, (103, 0, 0), (1125, 70, 475, 100))
        info = ["Болезни - влияют на смертность. Могут появится",
                "в ходе случайного события"]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 1130
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif x >= 1800 and x <= 1850 and y >= 20 and y <= 70:
        pygame.draw.rect(screen, (103, 0, 0), (1325, 70, 475, 150))
        info = ["Счастье - влияет на добычу ресурсов, возникновение",
                "восстаний и количество населения. Увеличивается",
                "количеством ресурсов и постройкой культурных зданий."]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 1330
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    else:
        screen.blit(fon, (0, 0))


start_screen()
# pole = Board(19, 9, cell_size=100)
size = WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode(size)
# os.environ['SDL_VIDEO_CENTERED'] = '1'
food, wood, stone, gold, iron, science, culture, population, diseases, happiness, resourses = 600, 400, 200, 0, 0, 0, 0, 1000, 0, 60, []
resourses.append(load_image('food.png'))
resourses.append(load_image('wood.png'))
resourses.append(load_image('stone.png'))
resourses.append(load_image('gold.png'))
resourses.append(load_image('iron.png'))
resourses.append(load_image('science.png'))
resourses.append(load_image('culture.png'))
resourses.append(load_image('population.png'))
resourses.append(load_image('diseases .png'))
resourses.append(load_image('happiness .png'))
fon = load_image('fon1.jpg')
running = True
y = 20
v = 20
while running:
    x = 0
    res_values = [str(food)[0:3], str(wood)[0:3], str(stone)[0:3], str(iron)[0:3], str(gold)[0:3],
                  str(science)[0:3], str(culture)[0:3],
                  str(population)[0:3], str(diseases)[0:3], str(happiness) + '%']
    coords = 80
    font = pygame.font.SysFont('arial', 40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.MOUSEMOTION:
            show_info(event.pos, screen)
    # pole.render(screen)
    for i in resourses:
        screen.blit(i, (x, y))
        pygame.draw.rect(screen, (37, 23, 5), (x + 50, y, 150, 50), 1)
        pygame.draw.rect(screen, (47, 27, 0), (x + 51, y + 1, 198, 48), 1)
        pygame.draw.rect(screen, (103, 0, 0), (x + 52, y + 2, 196, 46))
        x += 200
    for i in res_values:
        string_rendered = font.render(i, 1, (255, 255, 255))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = 20
        intro_rect.x = coords
        coords += 152
        coords += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    pygame.display.flip()
    food += v * clock.tick() / 2000
    clock.tick(FPS)

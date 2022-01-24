from startScreen import start_screen
from Board2 import Board
from Buildings2 import *
from SETTINGS import *
import random

pygame.init()
clock = pygame.time.Clock()
start = True
n, warn, draw_board_ok, error = 0, False, True, False
structures = []
all_sprites = pygame.sprite.Group()
castle_sprites = pygame.sprite.Group()

FPS = 50

start_screen()

size = WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

resourses, buildings = [], []

chance_revolt, chance_raid = 0, 0
victims_of_infection = 100
strange_infection = 5

running = True
y, v = 10, 20


def load_image(name):
    fullname = os.path.join('data/images', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


resourses.append(load_image('food.png'))
resourses.append(load_image('wood.png'))
resourses.append(load_image('stone.png'))
resourses.append(load_image('iron.png'))
resourses.append(load_image('gold.png'))
resourses.append(load_image('science.png'))
resourses.append(load_image('population.png'))
resourses.append(load_image('happiness .png'))
resourses.append(load_image('days.png'))
resourses.append(load_image('pause.png'))
fon = load_image('background.jpg')
army_sur = load_image('army.png')


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


def saveGame():
    global structures_save
    limit1 = limit
    cur.execute(f"""DELETE FROM Buildings 
            WHERE id > 1""")
    cur.execute(f"""DELETE FROM resourses WHERE id > 0""")
    cur.execute(f"""INSERT INTO resourses(food, foodplus, wood, woodplus, stone, stoneplus, iron, ironplus,
             gold, goldplus, population, populationplus, happiness, science, scienceplus, limit1, days)
             VALUES ({food}, {foodplus}, {wood}, {woodplus}, {stone}, {stoneplus}, {iron}, {ironplus}, {gold}
             , {goldplus}, {population}, {populationplus}, {happiness}, {science}, {scienceplus}, {limit1}, {days})""")
    for i in structures_save:
        if structures_save[i] != 0:
            type1 = structures_save[i][0]
            x1 = structures_save[i][1]
            y1 = structures_save[i][2]
            cell1 = structures_save[i][3]
            n = 1
            n += 1
            cur.execute(f"""INSERT INTO Buildings(type, x, y, cellx, celly) VALUES ('{type1}', {x1}, {y1},
            {cell1[0]},{cell1[1]})""")
            con.commit()


def draw_polygon(spis):
    pygame.draw.polygon(spis[0], spis[1], spis[2], spis[3])


def terminate():
    con.close()
    pygame.quit()
    sys.exit()


def show_info(coords, screen):
    x = coords[0]
    y = coords[1]
    coords = 65
    global draw_board_ok
    if x >= 0 and x <= 50 and y >= 10 and y <= 60:
        draw_board_ok = False
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
    elif x >= 200 and x <= 250 and y >= 10 and y <= 60:
        draw_board_ok = False
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
    elif x >= 400 and x <= 450 and y >= 10 and y <= 60:
        draw_board_ok = False
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
    elif x >= 600 and x <= 650 and y >= 10 and y <= 60:
        draw_board_ok = False
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
    elif x >= 800 and x <= 850 and y >= 10 and y <= 60:
        draw_board_ok = False
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
    elif x >= 1000 and x <= 1050 and y >= 10 and y <= 60:
        draw_board_ok = False
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
    elif x >= 1200 and x <= 1250 and y >= 10 and y <= 60:
        draw_board_ok = False
        pygame.draw.rect(screen, (103, 0, 0), (1250, 60, 475, 150))
        info = ["Население - главный фактор вашего города, из них",
                "набирается армия, оно добывает ресурсы. Повышается от",
                "избытка пищи и счастья."]
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
        draw_board_ok = False
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
    elif x >= 1250 and x <= 1400 and y >= 10 and y <= 60:
        draw_board_ok = False
        global army_height, army_width, info_army, army_level
        intro_rect_x = 1255
        pygame.draw.rect(screen, (103, 0, 0), (1250, 60, army_width, army_height))
        font = pygame.font.SysFont('arial', 20)

        if is_army:
            info = ["Уровень войск - " + str(army_level)]
            info_army = ["Численность войск - " + str(army)]
            army_width, army_height = 250, 100
            intro_rect_x += 65
            screen.blit(army_sur, (1260, 100))
            for i in info_army:
                string_rendered = font.render(i, True, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = coords
                intro_rect.x = 1255
                coords += 20
                coords += intro_rect.height
                screen.blit(string_rendered, intro_rect)
        else:
            army_height = 40
            info = ["У вас пока нет профессиональной армии!"]

        for i in info:
            string_rendered = font.render(i, True, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = intro_rect_x
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif x >= 1600 and x <= 1800 and y >= 10 and y <= 60:
        draw_board_ok = False
        pygame.draw.rect(screen, (103, 0, 0), (1475, 60, 300, 50))
        info = ["Количество пройденых вами дней"]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, True, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 1475
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif x >= 1800 and x <= 1850 and y >= 10 and y <= 60:
        draw_board_ok = False
        pygame.draw.rect(screen, (103, 0, 0), (1800, 60, 60, 40))
        info = ["Пауза"]
        font = pygame.font.SysFont('arial', 20)
        for i in info:
            string_rendered = font.render(i, True, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = coords
            intro_rect.x = 1800
            coords += 20
            coords += intro_rect.height
            screen.blit(string_rendered, intro_rect)
    elif x >= 50 and x <= 199 and y >= 10 and y <= 60:
        draw_board_ok = False
    elif x >= 250 and x <= 400 and y >= 10 and y <= 60:
        draw_board_ok = False
    elif x >= 450 and x <= 600 and y >= 10 and y <= 60:
        draw_board_ok = False
    elif x >= 650 and x <= 800 and y >= 10 and y <= 60:
        draw_board_ok = False
    elif x >= 850 and x <= 1000 and y >= 10 and y <= 60:
        draw_board_ok = False
    elif x >= 1050 and x <= 1200 and y >= 10 and y <= 60:
        draw_board_ok = False
    elif x >= 1450 and x <= 1600 and y >= 10 and y <= 60:
        draw_board_ok = False
    elif x >= 1650 and x <= 1800 and y >= 10 and y <= 60:
        draw_board_ok = False
    else:
        draw_board_ok = True


class Revolt:
    def __init__(self, chanse):
        self.chanse = chanse
        self.revolt = random.randint(0, 100)
        if self.revolt < self.chanse:
            global structures, foodplus, woodplus, stoneplus, ironplus, grids, scienceplus, goldplus, finish
            rem = random.randint(0, len(structures) - 1)
            if structures[rem][-1] == "castle":
                finish = True
            else:
                structures[rem][0].kill()
                if structures[rem][-1] == 'farm':
                    foodplus -= 10
                elif structures[rem][-1] == 'mill':
                    woodplus -= 10
                elif structures[rem][-1] == 'iron_mine':
                    ironplus -= 10
                elif structures[rem][1] == 'gold_mine':
                    goldplus -= 10
                elif structures[rem][-1] == 'quarry':
                    stoneplus -= 10
                elif structures[rem][-1] == 'university':
                    scienceplus -= 5
                grids[structures[rem][3]] = True
                del structures[rem]


class Raids:
    def __init__(self, chance):
        self.chance = chance
        self.raid = random.randint(0, 100)
        if self.raid < self.chance:
            global structures, foodplus, woodplus, stoneplus, ironplus, grids, scienceplus, army_level, goldplus,\
                finish, population, food, wood, stone, iron, science, gold
            chance_remove = random.randint(1, 10)

            if chance_remove > army_level:
                removing = chance_remove - army_level
                for i in range(removing):
                    rem = random.randint(0, len(structures) - 1)
                    if structures[rem][-1] == "castle":
                        finish = True
                    else:
                        res_minus = removing * 0.1

                        food -= food * res_minus
                        wood -= wood * res_minus
                        stone -= stone * res_minus
                        iron -= iron * res_minus
                        science -= science * res_minus
                        gold -= gold * res_minus

                        structures[rem][0].kill()
                        if structures[rem][-1] == 'farm':
                            foodplus -= 10
                        elif structures[rem][-1] == 'mill':
                            woodplus -= 10
                        elif structures[rem][-1] == 'iron_mine':
                            ironplus -= 10
                        elif structures[rem][1] == 'gold_mine':
                            goldplus -= 10
                        elif structures[rem][-1] == 'quarry':
                            stoneplus -= 10
                        elif structures[rem][-1] == 'university':
                            scienceplus -= 5
                        grids[structures[rem][3]] = True
                        del structures[rem]

            elif chance_remove == army_level:
                rem = random.randint(0, len(structures) - 1)
                if structures[rem][-1] == "castle":
                    finish = True
                else:
                    food -= food * 0.1
                    wood -= wood * 0.1
                    stone -= stone * 0.1
                    iron -= iron * 0.1
                    science -= science * 0.1
                    gold -= gold * 0.1

                    structures[rem][0].kill()
                    if structures[rem][-1] == 'farm':
                        foodplus -= 10
                    elif structures[rem][-1] == 'mill':
                        woodplus -= 10
                    elif structures[rem][-1] == 'iron_mine':
                        ironplus -= 10
                    elif structures[rem][1] == 'gold_mine':
                        goldplus -= 10
                    elif structures[rem][-1] == 'quarry':
                        stoneplus -= 10
                    elif structures[rem][-1] == 'university':
                        scienceplus -= 5
                    grids[structures[rem][3]] = True
                    del structures[rem]

            elif chance_remove < army_level:
                food -= food * 0.1
                wood -= wood * 0.1
                stone -= stone * 0.1
                iron -= iron * 0.1
                science -= science * 0.1
                gold -= gold * 0.1

                population -= ((army_level * 100) / 2)
                population -= (300 * (chance_remove - army_level))


def global_changes():
    global food, population, populationplus, happiness, limit, chance_revolt, gold, food, wood, stone, iron, \
        science, strange_infection, chance_raid
    populationplus = round((food - population) / 100)
    if round(food - population) > 1000 and happiness < 100 and limit > population:
        happiness += 1
    elif ((round((population - food)) > 500) or (limit - population < 100)) and happiness > 0:
        happiness -= 1
    if happiness < 50:
        chance_revolt += 1
    elif happiness > 75:
        chance_revolt = 0
        gold += 1
        population += 1
        food += 1
        wood += 1
        stone += 1
        iron += 1
    elif gold >= 1000:
        chance_raid += 1
    elif gold < 1000:
        chance_raid = 0
    victims_of_infection = round(population / 100) * 10
    victims_of_infection -= science
    population += populationplus


def draw_board():
    global board
    board = Board(20, 20)
    board.update()
    board.draw(screen)


class BUildFarm:
    def __init__(self, position, butHeigth, butWidth, text):
        self.position = position
        self.width = butWidth
        self.heigth = butHeigth
        self.text = text
        self.pos = menu.get_pos()
        self.cell = menu.get_cell()

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
                global farm, food, wood, type_farm, can_build, grids, board, warn_word, warn, error
                if food >= 50 and wood >= 100:
                    farm = Build(load_image('farm_3.png'), 3, 1, self.pos[0] + 20, self.pos[1], all_sprites, type_farm)
                    pygame.time.set_timer(type_farm, 3000)
                    menu.ok = False
                    food -= 50
                    wood -= 100
                    can_build = False
                    grids[board.grid_pos] = False
                    structures.append((farm, self.pos[0] + 20, self.pos[1], self.cell, 'farm'))
                    structures_save[self.cell] = ('farm', self.pos[0], self.pos[1], self.cell)
                else:
                    pygame.time.set_timer(type_error, 3000)
                    warn_word = "У вас недостаточно ресурсов для строительства!"
                    menu.ok = False
                    warn, error = True, True
        else:
            pygame.draw.rect(screen, (0, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))


class BuildMill(BUildFarm):
    def __init__(self, position: tuple, butHeigth: int = 40, butWidth: int = 150, text: str = "Кнопка"):
        super().__init__(position, butHeigth, butWidth, text)
        self.pos = menu.get_pos()
        self.cell = menu.get_cell()

    def render(self, screen):
        mousePos = pygame.mouse.get_pos()
        if self.mouse_in(mousePos):
            pygame.draw.rect(screen, (103, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
            if pygame.mouse.get_pressed()[0] and self.mouse_in(mousePos):
                global mill, food, wood, type_mill, can_build, grids, board, warn, warn_word, error
                if food >= 200 and wood >= 25:
                    mill = Build(load_image('mill.png'), 3, 1, self.pos[0], self.pos[1], all_sprites, type_mill)
                    pygame.time.set_timer(type_mill, 5000)
                    menu.ok = False
                    food -= 200
                    wood -= 25
                    can_build = False
                    grids[board.grid_pos] = False
                    structures.append((mill, self.pos[0], self.pos[1], self.cell, 'mill'))
                    structures_save[self.cell] = ('mill', self.pos[0], self.pos[1], self.cell)
                else:
                    pygame.time.set_timer(type_error, 3000)
                    warn_word = "У вас недостаточно ресурсов для строительства!"
                    menu.ok = False
                    warn, error = True, True
        else:
            pygame.draw.rect(screen, (0, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))


class BuildIronMine(BUildFarm):
    def __init__(self, position: tuple, butHeigth: int = 40, butWidth: int = 150, text: str = "Кнопка"):
        super().__init__(position, butHeigth, butWidth, text)
        self.pos = menu.get_pos()
        self.cell = menu.get_cell()

    def render(self, screen):
        mousePos = pygame.mouse.get_pos()
        if self.mouse_in(mousePos):
            pygame.draw.rect(screen, (103, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
            if pygame.mouse.get_pressed()[0] and self.mouse_in(mousePos):
                global ironmine, food, wood, type_ironmine, can_build, grids, board, warn, warn_word, error
                if food >= 175 and wood >= 125:
                    ironmine = Build(load_image('ironmine.png'), 3, 1, self.pos[0], self.pos[1], all_sprites,
                                type_ironmine)
                    pygame.time.set_timer(type_ironmine, 7000)
                    menu.ok = False
                    food -= 175
                    wood -= 125
                    can_build = False
                    grids[board.grid_pos] = False
                    structures.append((ironmine, self.pos[0], self.pos[1], self.cell, 'iron_mine'))
                    structures_save[self.cell] = ('ironmine', self.pos[0], self.pos[1], self.cell)
                else:
                    pygame.time.set_timer(type_error, 3000)
                    warn_word = "У вас недостаточно ресурсов для строительства!"
                    menu.ok = False
                    warn, error = True, True
        else:
            pygame.draw.rect(screen, (0, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))


class BuildVillage(BUildFarm):
    def __init__(self, position: tuple, butHeigth: int = 40, butWidth: int = 150, text: str = "Кнопка"):
        super().__init__(position, butHeigth, butWidth, text)
        self.pos = menu.get_pos()
        self.cell = menu.get_cell()

    def render(self, screen):
        mousePos = pygame.mouse.get_pos()
        if self.mouse_in(mousePos):
            pygame.draw.rect(screen, (103, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
            if pygame.mouse.get_pressed()[0] and self.mouse_in(mousePos):
                global village, food, wood, type_village, can_build, grids, board, stone, gold
                if food >= 100 and wood >= 100 and stone >= 50 and gold >= 20:
                    village = Build(load_image('village.png'), 3, 1, self.pos[0], self.pos[1], all_sprites,
                                    type_village)
                    pygame.time.set_timer(type_village, 3000)
                    menu.ok = False
                    food -= 100
                    wood -= 100
                    stone -= 50
                    gold -= 20
                    can_build = False
                    grids[board.grid_pos] = False
                    structures.append((village, self.pos[0], self.pos[1], self.cell, 'village'))
                    structures_save[self.cell] = ('village', self.pos[0], self.pos[1], self.cell)
        else:
            pygame.draw.rect(screen, (0, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))


class BuildQuarry(BUildFarm):
    def __init__(self, position: tuple, butHeigth: int = 40, butWidth: int = 150, text: str = "Кнопка"):
        super().__init__(position, butHeigth, butWidth, text)
        self.pos = menu.get_pos()
        self.cell = menu.get_cell()

    def render(self, screen):
        mousePos = pygame.mouse.get_pos()
        if self.mouse_in(mousePos):
            pygame.draw.rect(screen, (103, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
            if pygame.mouse.get_pressed()[0] and self.mouse_in(mousePos):
                global quarry, food, wood, type_quarry, can_build, grids, board, warn_word, warn, error
                if food >= 175 and wood >= 125:
                    quarry = Build(load_image('quarry.png'), 3, 1, self.pos[0], self.pos[1], all_sprites,
                                        type_quarry)
                    pygame.time.set_timer(type_quarry, 6000)
                    menu.ok = False
                    food -= 175
                    wood -= 125
                    can_build = False
                    grids[board.grid_pos] = False
                    structures.append((quarry, self.pos[0], self.pos[1],self.cell, 'quarry'))
                    structures_save[self.cell] = ('quarry', self.pos[0], self.pos[1], self.cell)
                else:
                    pygame.time.set_timer(type_error, 3000)
                    warn_word = "У вас недостаточно ресурсов для строительства!"
                    menu.ok = False
                    warn, error = True, True
        else:
            pygame.draw.rect(screen, (0, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))


class BuildBarracks(BUildFarm):
    def __init__(self, position: tuple, butHeigth: int = 40, butWidth: int = 150, text: str = "Кнопка"):
        super().__init__(position, butHeigth, butWidth, text)
        self.pos = menu.get_pos()
        self.cell = menu.get_cell()

    def render(self, screen):
        mousePos = pygame.mouse.get_pos()
        if self.mouse_in(mousePos):
            pygame.draw.rect(screen, (103, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
            if pygame.mouse.get_pressed()[0] and self.mouse_in(mousePos):
                global barracks, food, wood, type_barracks, can_build, grids, board, warn, warn_word, error
                if food >= 300 and wood >= 225:
                    barracks = Build(load_image('barracks_3.png'), 3, 1, self.pos[0], self.pos[1] - 30, all_sprites,
                            type_barracks)
                    pygame.time.set_timer(type_barracks, 7000)
                    menu.ok = False
                    food -= 300
                    wood -= 225
                    can_build = False
                    grids[board.grid_pos] = False
                    structures.append((barracks, self.pos[0], self.pos[1], self.cell, 'barracks'))
                    structures_save[self.cell] = ('barracks', self.pos[0], self.pos[1], self.cell)
                else:
                    pygame.time.set_timer(type_error, 3000)
                    warn_word = "У вас недостаточно ресурсов для строительства!"
                    menu.ok = False
                    warn, error = True, True
        else:
            pygame.draw.rect(screen, (0, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))


class BuildUniversity(BUildFarm):
    def __init__(self, position: tuple, butHeigth: int = 40, butWidth: int = 150, text: str = "Кнопка"):
        super().__init__(position, butHeigth, butWidth, text)
        self.pos = menu.get_pos()
        self.cell = menu.get_cell()

    def render(self, screen):
        mousePos = pygame.mouse.get_pos()
        if self.mouse_in(mousePos):
            pygame.draw.rect(screen, (103, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
            if pygame.mouse.get_pressed()[0] and self.mouse_in(mousePos):
                global university, food, wood, type_university, can_build, grids, board, warn, warn_word, error
                if food >= 300 and wood >= 225:
                    university = Build(load_image('university.png'), 3, 1, self.pos[0], self.pos[1] - 20, all_sprites,
                            type_university)
                    pygame.time.set_timer(type_university, 9000)
                    menu.ok = False
                    food -= 300
                    wood -= 225
                    can_build = False
                    grids[board.grid_pos] = False
                    structures.append((barracks, self.pos[0], self.pos[1], self.cell, 'university'))
                    structures_save[self.cell] = ('university', self.pos[0], self.pos[1], self.cell)
                else:
                    pygame.time.set_timer(type_error, 3000)
                    warn_word = "У вас недостаточно ресурсов для строительства!"
                    menu.ok = False
                    warn, error = True, True
        else:
            pygame.draw.rect(screen, (0, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))


class BuildGoldMine(BUildFarm):
    def __init__(self, position: tuple, butHeigth: int = 40, butWidth: int = 150, text: str = "Кнопка"):
        super().__init__(position, butHeigth, butWidth, text)
        self.pos = menu.get_pos()
        self.cell = menu.get_cell()

    def render(self, screen):
        mousePos = pygame.mouse.get_pos()
        if self.mouse_in(mousePos):
            pygame.draw.rect(screen, (103, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
            if pygame.mouse.get_pressed()[0] and self.mouse_in(mousePos):
                global goldmine, food, wood, type_goldmine, can_build, grids, board, stone
                if food >= 175 and wood >= 200 and stone >= 100:
                    goldmine = Build(load_image('goldmine1.png'), 3, 1, self.pos[0], self.pos[1], all_sprites,
                                     type_goldmine)
                    pygame.time.set_timer(type_goldmine, 5000)
                    menu.ok = False
                    food -= 175
                    wood -= 200
                    stone -= 100
                    can_build = False
                    grids[board.grid_pos] = False
                    structures.append((goldmine, self.pos[0], self.pos[1], self.cell, 'goldmine'))
                    structures_save[self.cell] = ('goldmine', self.pos[0], self.pos[1], self.cell)
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
        self.ironmine = ['Железный -', '- 175', '- 75', 'рудник']
        self.quarry = ['Каменоломня -', '- 175', '- 75']
        self.barracks = ['Казармы - ', '- 300', '- 225']
        self.university = ['Университет -', '- 300', ' -225']
        self.ok = False
        self.lx = lx
        self.ly = ly
        self.side = side
        self.bx = buildx
        self.by = buildy

    def get_pos(self):
        return self.bx, self.by

    def get_cell(self):
        global board
        return board.grid_pos

    def show_list(self):
        ms = pygame.mouse.get_pos()
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
                font = pygame.font.SysFont('arial', 16)
                butfr = BUildFarm(position=(self.x + 10, self.y + 5), butHeigth=60, butWidth=175, text='')
                butfr.render(self.screen)
                self.screen.blit(self.fdres, (self.x + 70, self.y + 10))
                self.screen.blit(self.wdres, (self.x + 70, self.y + 40))
                string_rendered = font.render(self.food[0], True, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = self.y + 10
                intro_rect.x = self.x + 10
                screen.blit(string_rendered, intro_rect)
                string_rendered = font.render(self.food[1], True, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = self.y + 10
                intro_rect.x = self.x + 100
                screen.blit(string_rendered, intro_rect)
                string_rendered = font.render(self.food[2], True, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = self.y + 40
                intro_rect.x = self.x + 100

                butml = BuildMill(position=(self.x + 10, self.y + 75), butHeigth=60, butWidth=175, text='')
                butml.render(self.screen)
                self.screen.blit(self.fdres, (self.x + 100, self.y + 80))
                self.screen.blit(self.wdres, (self.x + 100, self.y + 110))
                screen.blit(string_rendered, intro_rect)
                string_rendered = font.render(self.mill[0], True, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = self.y + 80
                intro_rect.x = self.x + 10
                screen.blit(string_rendered, intro_rect)
                string_rendered = font.render(self.mill[1], True, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = self.y + 80
                intro_rect.x = self.x + 130
                screen.blit(string_rendered, intro_rect)
                string_rendered = font.render(self.mill[2], True, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = self.y + 110
                intro_rect.x = self.x + 130
                screen.blit(string_rendered, intro_rect)

                butbr = BuildBarracks(position=(self.x + 10, self.y + 145), butHeigth=60, butWidth=175, text='')
                butbr.render(self.screen)
                self.screen.blit(self.fdres, (self.x + 90, self.y + 150))
                self.screen.blit(self.wdres, (self.x + 90, self.y + 180))
                screen.blit(string_rendered, intro_rect)
                string_rendered = font.render(self.barracks[0], True, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = self.y + 150
                intro_rect.x = self.x + 10
                screen.blit(string_rendered, intro_rect)
                string_rendered = font.render(self.barracks[1], True, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = self.y + 150
                intro_rect.x = self.x + 120
                screen.blit(string_rendered, intro_rect)
                string_rendered = font.render(self.barracks[2], True, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = self.y + 180
                intro_rect.x = self.x + 120
                screen.blit(string_rendered, intro_rect)

                butuv = BuildUniversity(position=(self.x + 10, self.y + 215), butHeigth=60, butWidth=175, text='')
                butuv.render(self.screen)
                self.screen.blit(self.fdres, (self.x + 120, self.y + 220))
                self.screen.blit(self.wdres, (self.x + 120, self.y + 250))
                screen.blit(string_rendered, intro_rect)
                string_rendered = font.render(self.university[0], True, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = self.y + 220
                intro_rect.x = self.x + 10
                screen.blit(string_rendered, intro_rect)
                string_rendered = font.render(self.university[1], True, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = self.y + 220
                intro_rect.x = self.x + 145
                screen.blit(string_rendered, intro_rect)
                string_rendered = font.render(self.university[2], True, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = self.y + 250
                intro_rect.x = self.x + 145
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

                font = pygame.font.SysFont('arial', 16)
                butfr = BuildIronMine(position=(self.x + 10, self.y + 5), butHeigth=60, butWidth=175, text='')
                butfr.render(self.screen)
                self.screen.blit(self.fdres, (self.x + 100, self.y + 10))
                self.screen.blit(self.wdres, (self.x + 100, self.y + 40))
                string_rendered = font.render(self.ironmine[0], True, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = self.y + 10
                intro_rect.x = self.x + 10
                screen.blit(string_rendered, intro_rect)
                string_rendered = font.render(self.ironmine[3], True, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = self.y + 40
                intro_rect.x = self.x + 10
                screen.blit(string_rendered, intro_rect)
                string_rendered = font.render(self.ironmine[1], True, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = self.y + 10
                intro_rect.x = self.x + 130
                screen.blit(string_rendered, intro_rect)
                string_rendered = font.render(self.ironmine[2], True, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = self.y + 40
                intro_rect.x = self.x + 130
                screen.blit(string_rendered, intro_rect)

                butfr1 = BuildQuarry(position=(self.x + 10, self.y + 75), butHeigth=60, butWidth=187, text='')
                butfr1.render(self.screen)
                self.screen.blit(self.fdres, (self.x + 130, self.y + 80))
                self.screen.blit(self.wdres, (self.x + 130, self.y + 110))
                string_rendered = font.render(self.quarry[0], True, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = self.y + 80
                intro_rect.x = self.x + 10
                screen.blit(string_rendered, intro_rect)
                string_rendered = font.render(self.quarry[1], True, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = self.y + 80
                intro_rect.x = self.x + 160
                screen.blit(string_rendered, intro_rect)
                string_rendered = font.render(self.quarry[2], True, (255, 255, 255))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = self.y + 110
                intro_rect.x = self.x + 160
                screen.blit(string_rendered, intro_rect)

        if (self.side == 1) and \
                (not (ms[0] >= self.lx and ms[0] <= self.x + 200 and ms[1] >= self.y and ms[1] <= self.ly + 50)):
            self.ok = False

        elif (self.side == 2) and \
                (not (ms[0] <= self.lx and ms[0] >= self.x and ms[1] >= self.y and ms[1] <= self.ly + 50)):
            self.ok = False


def Plauge(plaugers):
    chanse = random.randint(0, 100)
    global population
    if chanse < 5:
        population -= population // 2
    elif chanse < 25:
        population -= plaugers


def saveGame():
    global structures_save
    limit1 = limit
    cur.execute(f"""DELETE FROM Buildings 
            WHERE id > 1""")
    cur.execute(f"""DELETE FROM resourses WHERE id > 0""")
    cur.execute(f"""INSERT INTO resourses(food, foodplus, wood, woodplus, stone, stoneplus, iron, ironplus,
             gold, goldplus, population, populationplus, happiness, science, scienceplus, limit1, days)
             VALUES ({food}, {foodplus}, {wood}, {woodplus}, {stone}, {stoneplus}, {iron}, {ironplus}, {gold}
             , {goldplus}, {population}, {populationplus}, {happiness}, {science}, {scienceplus}, {limit1}, {days})""")
    for i in structures_save:
        if structures_save[i] != 0:
            type1 = structures_save[i][0]
            x1 = structures_save[i][1]
            y1 = structures_save[i][2]
            cell1 = structures_save[i][3]
            n = 1
            n += 1
            cur.execute(f"""INSERT INTO Buildings(type, x, y, cellx, celly) VALUES ('{type1}', {x1}, {y1},
            {cell1[0]},{cell1[1]})""")
            con.commit()


def draw_sprites():
    all_sprites.draw(screen)


for i in structures_save:
    if structures_save[i] != 0:
        a = structures_save[i]
        if a[0] == 'farm':
            all_sprites.add(Build(load_image('finishedfarm.png'), 1, 1, a[1] + 20, a[2], all_sprites, type_farm))
        elif a[0] == 'mill':
            all_sprites.add(Build(load_image('finishedmill.png'), 1, 1, a[1], a[2], all_sprites, type_mill))
        elif a[0] == 'village':
            all_sprites.add(Build(load_image('finishedvillage.png'), 1, 1, a[1], a[2], all_sprites, type_village))
        elif a[0] == 'quarry':
            all_sprites.add(Build(load_image('finishedquarry.png'), 1, 1, a[1], a[2], all_sprites, type_quarry))
        elif a[0] == 'ironmine':
            all_sprites.add(Build(load_image('finishedironmine.png'), 1, 1, a[1], a[2], all_sprites, type_ironmine))
        elif a[0] == 'goldmine':
            all_sprites.add(Build(load_image('finishedgoldmine.png'), 1, 1, a[1], a[2], all_sprites, type_goldmine))
        elif a[0] == 'university':
            all_sprites.add(Build(load_image('finisheduniversity.png'), 1, 1, a[1], a[2] - 20, all_sprites, type_university))
        elif a[0] == 'barracks':
            all_sprites.add(Build(load_image('finishedbarracks.png'), 1, 1, a[1], a[2] - 30, all_sprites, type_barracks))

        food = cur.execute('''SELECT food FROM resourses''').fetchall()[0][0]
        foodplus = cur.execute('''SELECT foodplus FROM resourses''').fetchall()[0][0]
        wood = cur.execute('''SELECT wood FROM resourses''').fetchall()[0][0]
        woodplus = cur.execute('''SELECT woodplus FROM resourses''').fetchall()[0][0]
        stone = cur.execute('''SELECT stone FROM resourses''').fetchall()[0][0]
        stoneplus = cur.execute('''SELECT stoneplus FROM resourses''').fetchall()[0][0]
        iron = cur.execute('''SELECT iron FROM resourses''').fetchall()[0][0]
        ironplus = cur.execute('''SELECT ironplus FROM resourses''').fetchall()[0][0]
        gold = cur.execute('''SELECT gold FROM resourses''').fetchall()[0][0]
        goldplus = cur.execute('''SELECT goldplus FROM resourses''').fetchall()[0][0]
        population = cur.execute('''SELECT population FROM resourses''').fetchall()[0][0]
        populationplus = cur.execute('''SELECT populationplus FROM resourses''').fetchall()[0][0]
        science = cur.execute('''SELECT science FROM resourses''').fetchall()[0][0]
        scienceplus = cur.execute('''SELECT scienceplus FROM resourses''').fetchall()[0][0]
        happiness = cur.execute('''SELECT happiness FROM resourses''').fetchall()[0][0]
        limit = cur.execute('''SELECT limit1 FROM resourses''').fetchall()[0][0]
        days = cur.execute('''SELECT days FROM resourses''').fetchall()[0][0]


board = Board(20, 20)
# board.set_view(0, 0, 100)

pygame.time.set_timer(type_res, 1000)
pygame.time.set_timer(type_days, 60000)

menu = BuildMenu(screen, 0, 0, 0, 0, 0, 0, 0)
farm = Build(load_image('farm_3.png'), 3, 1, -300, -300, all_sprites, type_farm)
mill = Build(load_image('mill.png'), 3, 1, -300, -300, all_sprites, type_mill)
ironmine = Build(load_image('ironmine.png'), 3, 1, -300, -300, all_sprites, type_ironmine)
quarry = Build(load_image('quarry.png'), 3, 1, -300, -300, all_sprites, type_quarry)
barracks = Build(load_image('barracks.png'), 3, 1, -300, -300, all_sprites, type_barracks)
university = Build(load_image('university.png'), 3, 1, -300, -300, all_sprites, type_university)
castle = Castle_cl(load_image('castle/castle_anim2.png'), 5, 1, 960, 650, castle_sprites)
structures.append((castle, 960, 650, (12, 2), 'castle'))

pygame.time.set_timer(type_event, 20000)
pygame.time.set_timer(type_castle, 150)

# pygame.mixer.music.load('data/music/witcher3.mp3')
# pygame.mixer.music.set_volume(0.05)
# pygame.mixer.music.play(-1)

warn_width, warn_color, warn_word, farmcord, ironminecord, quarrycord, barrackscord = 340, (255, 0, 0), "", (0, 0),\
                                                                                      (0, 0), (0, 0), (0, 0)

while running:
    x = 0
    warn_rect, warn_polygon = [], []

    update_bg()

    if finish:
        print('finish')
        terminate()

    if menu.ok:
        draw_polygon([screen, (255, 255, 255), board.iso_poly1, 3])
        draw_polygon([screen, (255, 255, 255), board.iso_poly2, 3])

    if not warn and not menu.ok:
        if draw_board_ok:
            draw_board()

    if warn:
        info = [warn_word]

        if board.grid_pos in buildings and can_build == False:
            info = ["Сейчас строится здание, подождите!"]
        # elif board.grid_pos in buildings and can_build == True:
        #     info = ["На этом месте уже стоит постройка!"]

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
        elif info[0] == "У вас недостаточно ресурсов для строительства!":
            warn_width = 470

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
                if not error:
                    warn = False

            ry_c, rx_c = -34, 5 - warn_width
            warn_rect = [screen, (103, 0, 0), (rx - warn_width, ry - 35, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - warn_width, ry - 50, 200 + warn_width, 100), 1)
            warn_polygon = [screen, warn_color, board.iso_poly2, 3]

        elif board.grid_pos[0] == 3 and board.grid_pos[1] == -1:
            coords1 = board.iso_poly2[3]
            rx, ry = coords1
            if ((mx > rx + warn_width + 200) or (mx < rx) or (my > ry + 53) or (my < ry - 53)):
                if not error:
                    warn = False

            ry_c, rx_c = -34, 205
            warn_rect = [screen, (103, 0, 0), (rx + 200, ry - 35, warn_width, 35), ry, rx, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx, ry - 50, 200 + warn_width, 100), 1)
            warn_polygon = [screen, warn_color, board.iso_poly2, 3]

        elif (board.grid_pos[0] == 17 and board.grid_pos[1] <= 3) or \
                (board.grid_pos[0] == 18 and board.grid_pos[1] <= 3) or \
                (board.grid_pos[0] == 19 and board.grid_pos[1] <= 3) or \
                (board.grid_pos[0] == 20 and board.grid_pos[1] <= 3) or \
                (board.grid_pos[0] == 11 and board.grid_pos[1] == 3):
            coords1 = board.iso_poly1[3]
            rx, ry = coords1
            if ((mx > rx + 200) or (mx < rx - warn_width) or (my > ry + 53) or (my < ry - 53)):
                if not error:
                    warn = False

            ry_c, rx_c = -34, 5 - warn_width
            warn_rect = [screen, (103, 0, 0), (rx - warn_width, ry - 35, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - warn_width, ry - 50, 200 + warn_width, 100), 1)
            warn_polygon = [screen, warn_color, board.iso_poly1, 3]

        elif ((board.grid_pos[0] == 0 or board.grid_pos[0] == 1) and board.grid_pos[1] == 0) or \
                (board.grid_pos[0] == 1 and board.grid_pos[1] == 1):  # draw right down iso_poly1
            coords1 = board.iso_poly1[0]
            rx, ry = coords1
            if ((mx > rx + warn_width) or (mx < rx - 100) or (my > ry + 123) or (my < ry)):
                if not error:
                    warn = False

            ry_c, rx_c = 105, 5
            warn_rect = [screen, (103, 0, 0), (rx, ry + 100, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - 100, ry, warn_width + 100, 135), 1)
            warn_polygon = [screen, warn_color, board.iso_poly1, 3]

        elif board.grid_pos[0] == 2 and (board.grid_pos[1] == 1 or board.grid_pos[1] == 2):
            coords1 = board.iso_poly1[0]
            rx, ry = coords1
            if ((mx > rx + warn_width) or (mx < rx - 100) or (my > ry + 123) or (my < ry)):
                if not error:
                    warn = False

            ry_c, rx_c = 105, 5
            warn_rect = [screen, (103, 0, 0), (rx, ry + 100, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - 100, ry, warn_width + 100, 135), 1)
            warn_polygon = [screen, warn_color, board.iso_poly1, 3]

        elif (board.grid_pos[0] == 1 or board.grid_pos[0] == 0 or board.grid_pos[0] == 2) \
                and (board.grid_pos[1] == -1):  # right iso_poly2
            coords1 = board.iso_poly2[2]
            rx, ry = coords1
            if ((mx > rx + warn_width) or (mx < rx - 100) or (my > ry + 34) or (my < ry - 83)):
                if not error:
                    warn = False

            ry_c, rx_c = 8, 5
            warn_rect = [screen, (103, 0, 0), (rx, ry, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - 100, ry - 100, warn_width + 102, 136), 1)
            warn_polygon = [screen, warn_color, board.iso_poly2, 3]

        elif (board.grid_pos[0] == 2 or board.grid_pos[0] == 3) and board.grid_pos[1] == -2:
            coords1 = board.iso_poly2[2]
            rx, ry = coords1
            if ((mx > rx + warn_width) or (mx < rx - 100) or (my > ry + 34) or (my < ry - 83)):
                if not error:
                    warn = False

            ry_c, rx_c = 8, 5
            warn_rect = [screen, (103, 0, 0), (rx, ry, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - 100, ry - 100, warn_width + 102, 136), 1)
            warn_polygon = [screen, warn_color, board.iso_poly2, 3]

        elif (board.grid_pos[0] == 3 or board.grid_pos[0] == 4) and board.grid_pos[1] == -3:
            coords1 = board.iso_poly2[2]
            rx, ry = coords1
            if ((mx > rx + warn_width) or (mx < rx - 100) or (my > ry + 34) or (my < ry - 83)):
                if not error:
                    warn = False

            ry_c, rx_c = 8, 5
            warn_rect = [screen, (103, 0, 0), (rx, ry, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - 100, ry - 100, warn_width + 102, 136), 1)
            warn_polygon = [screen, warn_color, board.iso_poly2, 3]

        elif (board.grid_pos[0] == 3 or board.grid_pos[0] == 4 or board.grid_pos[0] == 5) and board.grid_pos[1] == -4:
            coords1 = board.iso_poly2[2]
            rx, ry = coords1
            if ((mx > rx + warn_width) or (mx < rx - 100) or (my > ry + 34) or (my < ry - 83)):
                if not error:
                    warn = False

            ry_c, rx_c = 8, 5
            warn_rect = [screen, (103, 0, 0), (rx, ry, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - 100, ry - 100, warn_width + 102, 136), 1)
            warn_polygon = [screen, warn_color, board.iso_poly2, 3]

        elif (board.grid_pos[0] == 5 or board.grid_pos[0] == 6) and board.grid_pos[1] == -5:
            coords1 = board.iso_poly2[2]
            rx, ry = coords1
            if ((mx > rx + warn_width) or (mx < rx - 100) or (my > ry + 34) or (my < ry - 83)):
                if not error:
                    warn = False

            ry_c, rx_c = 8, 5
            warn_rect = [screen, (103, 0, 0), (rx, ry, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - 100, ry - 100, warn_width + 102, 136), 1)
            warn_polygon = [screen, warn_color, board.iso_poly2, 3]

        elif (board.grid_pos[0] == 7 or board.grid_pos[0] == 6) and board.grid_pos[1] == -6:
            coords1 = board.iso_poly2[2]
            rx, ry = coords1
            if ((mx > rx + warn_width) or (mx < rx - 100) or (my > ry + 34) or (my < ry - 83)):
                if not error:
                    warn = False

            ry_c, rx_c = 8, 5
            warn_rect = [screen, (103, 0, 0), (rx, ry, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - 100, ry - 100, warn_width + 102, 136), 1)
            warn_polygon = [screen, warn_color, board.iso_poly2, 3]

        elif (board.grid_pos[0] == 8 or board.grid_pos[0] == 7) and board.grid_pos[1] == -7:
            coords1 = board.iso_poly2[2]
            rx, ry = coords1
            if ((mx > rx + warn_width) or (mx < rx - 100) or (my > ry + 34) or (my < ry - 83)):
                if not error:
                    warn = False

            ry_c, rx_c = 8, 5
            warn_rect = [screen, (103, 0, 0), (rx, ry, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - 100, ry - 100, warn_width + 102, 136), 1)
            warn_polygon = [screen, warn_color, board.iso_poly2, 3]

        elif (board.grid_pos[0] == 8 or board.grid_pos[0] == 9) and board.grid_pos[1] == -8:
            coords1 = board.iso_poly2[2]
            rx, ry = coords1
            if ((mx > rx + 100) or (mx < rx - warn_width) or (my > ry + 34) or (my < ry - 83)):
                if not error:
                    warn = False

            ry_c, rx_c = 8, -warn_width
            warn_rect = [screen, (103, 0, 0), (rx - warn_width, ry, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - warn_width, ry - 100, warn_width + 102, 136), 1)
            warn_polygon = [screen, warn_color, board.iso_poly2, 3]

        elif (board.grid_pos[0] == 10 or board.grid_pos[0] == 9) and board.grid_pos[1] == -9:
            coords1 = board.iso_poly2[2]
            rx, ry = coords1
            if ((mx > rx + 100) or (mx < rx - warn_width) or (my > ry + 34) or (my < ry - 83)):
                if not error:
                    warn = False

            ry_c, rx_c = 8, -warn_width
            warn_rect = [screen, (103, 0, 0), (rx - warn_width, ry, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - warn_width, ry - 100, warn_width + 102, 136), 1)
            warn_polygon = [screen, warn_color, board.iso_poly2, 3]

        elif (board.grid_pos[0] == 16 or board.grid_pos[0] == 15) and board.grid_pos[1] == 0:  # draw left iso_poly1
            coords1 = board.iso_poly1[1]
            rx, ry = coords1
            if ((mx > rx) or (mx < rx - warn_width - 200) or (my > ry + 53) or (my < ry - 53)):
                if not error:
                    warn = False

            ry_c, rx_c = -34, -warn_width - 195
            warn_rect = [screen, (103, 0, 0), (rx - 200 - warn_width, ry - 35, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - warn_width - 200, ry - 50, 200 + warn_width, 100), 1)
            warn_polygon = [screen, warn_color, board.iso_poly1, 3]

        else:  # iso_poly1
            coords1 = board.iso_poly1[1]
            rx, ry = coords1
            if ((mx > rx + warn_width) or (mx < rx - 200) or (my > ry + 53) or (my < ry - 53)):
                if not error:
                    warn = False

            ry_c, rx_c = - 34, 5
            warn_rect = [screen, (103, 0, 0), (rx, ry - 35, warn_width, 35), rx, ry, ry_c, rx_c]
            pygame.draw.rect(screen, (255, 0, 0), (rx - 200, ry - 50, 200 + warn_width, 100), 1)
            warn_polygon = [screen, warn_color, board.iso_poly1, 3]

    draw_sprites()
    show_info(pygame.mouse.get_pos(), screen)

    res_values = [str(round(food)), str(round(wood)), str(round(stone)), str(round(iron)), str(round(gold)),
                  str(round(science)), str(round(population)), str(round(happiness)) + '%', str(round(days))]
    coords = 80
    font = pygame.font.SysFont('arial', 40)

    if len(warn_rect) != 0:
        draw_rect(warn_rect)
    if len(warn_polygon) != 0:
        draw_polygon(warn_polygon)

    castle_sprites.draw(screen)
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
                        if board.grid_pos == (17, 0) or board.grid_pos == (18, 0) or \
                                board.grid_pos == (19, 1) or board.grid_pos == (18, 1):
                            cord = board.iso_poly1[3]
                            x1 = cord[0] - 200
                            y1 = cord[1]
                            lx = board.iso_poly1[1][0]
                            ly = board.iso_poly1[1][1]
                            stayx = x1 + 245
                            stayy = y1 - 50
                            side = 2
                            if y1 >= 540:
                                y1 -= 300
                            else:
                                y1 -= 50
                                ly += 250
                            menu = BuildMenu(screen, x1, y1, lx, ly, 2, stayx, stayy)
                        elif board.grid_pos[1] >= 0:
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

            elif event.button == 3:
                saveGame()

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

        if event.type == type_quarry:
            if quarry.n == 1:
                stoneplus += 10
                can_build = True
            quarry.update()

        if event.type == type_barracks:
            if barracks.n == 1:
                is_army = True
                army += 100
                army_level += 1
                can_build = True
            barracks.update()

        if event.type == type_university:
            if university.n == 1:
                scienceplus += 5
                can_build = True
            university.update()

        if event.type == type_ironmine:
            if ironmine.n == 1:
                # ironplus += 10
                goldplus += 10
                can_build = True
            ironmine.update()

        if event.type == type_res:
            food += foodplus
            wood += woodplus
            iron += ironplus
            stone += stoneplus
            gold += goldplus
            science += scienceplus
            global_changes()

        if event.type == type_days:
            days += 1

        if event.type == type_event:
            Revolt(chance_revolt)
            Raids(chance_raid)

        if event.type == type_castle:
            castle.update()

        if event.type == type_error:
            error = False

    for i in range(0, len(resourses)):
        screen.blit(resourses[i], (x, y))
        if i != len(resourses) - 1:
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

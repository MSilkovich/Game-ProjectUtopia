import pygame
from SETTINGS import MYEVENTTYPE_farm, farm_sprites, load_image, screen
from Buildings import Farm
from INSTANCES import board


class BUildFarm:
    def __init__(self, position: tuple, butHeigth: int = 40, butWidth: int = 150, text: str = "Кнопка"):
        self.position = position
        self.width = butWidth
        self.heigth = butHeigth
        self.text = text
        self.menu = menu
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
            pygame.draw.rect(screen, (0, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
            if pygame.mouse.get_pressed()[0] and self.mouse_in(mousePos):
                global farm, food, wood
                farm = Farm(load_image('farm.png'), 3, 1, self.pos[0], self.pos[1], farm_sprites, MYEVENTTYPE_farm)
                pygame.time.set_timer(MYEVENTTYPE_farm, 3000)
                self.menu.ok = False
                food -= 50
                wood -= 200
        elif pygame.mouse.get_pressed() and self.mouse_in(mousePos):
            pygame.draw.rect(screen, (2, 0, 0), (50, 50, 200, 200))
        else:
            pygame.draw.rect(screen, (3, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
        self.font = pygame.font.SysFont('arial', 18)
        valueSurf = self.font.render(f"{self.text}", True, (51, 51, 51))
        textx = self.position[0] + (self.width / 2) - (valueSurf.get_rect().width / 2)
        texty = self.position[1] + (self.heigth / 2) - (valueSurf.get_rect().height / 2)
        screen.blit(valueSurf, (textx, texty))


class BuildMenu:
    def __init__(self, screen, x, y, lx, ly, side, buildx, buildy):
        self.x = x
        self.y = y
        self.width = 200
        self.heigth = 350
        self.position = (board.iso_poly1[3][0] + self.width, board.iso_poly2[3][1] + self.heigth)
        self.screen = screen
        self.food = ['Ферма -', load_image('buildfarm.png'), load_image('woodres.png'), '- 50', '- 100']
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
            but = BUildFarm(position=(self.x + 10, self.y + 10), butHeigth=40, butWidth=55, text='Ферма-')
            but.render(self.screen)
            self.screen.blit(self.food[1], (self.x + 70, self.y + 10))
            self.screen.blit(self.food[2], (self.x + 70, self.y + 40))
            string_rendered = font.render(self.food[3], 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = self.y + 10
            intro_rect.x = self.x + 100
            self.screen.blit(string_rendered, intro_rect)
            string_rendered = font.render(self.food[4], 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = self.y + 40
            intro_rect.x = self.x + 100
            self.screen.blit(string_rendered, intro_rect)
        if (self.side == 1) and \
                (not (ms[0] >= self.lx and ms[0] <= self.x + 200 and ms[1] >= self.y and ms[1] <= self.ly + 50)):
            self.ok = False
        elif (self.side == 2) and \
                (not (ms[0] <= self.lx and ms[0] >= self.x and ms[1] >= self.y and ms[1] <= self.ly + 50)):
            self.ok = False


menu = BuildMenu(screen, 0, 0, 0, 0, 0, 0, 0)
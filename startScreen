import pygame
import os
import sys

pygame.init()
clock = pygame.time.Clock()
start = True
start1 = True
n = 0

FPS = 60

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
                global start, start1
                start = False
                start1 = False
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


class BackButton(StartButton):
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
                global start1
                start1 = False
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
                global start1
                start1 = True
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
                btn_start1 = StartButton((100, 450), butHeigth=100, butWidth=200, text='К игре!')
                btn_back = BackButton((400, 450), butHeigth=100, butWidth=200, text='На главную.')
                while start1:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            terminate()
                    btn_start1.render(scr1)
                    btn_back.render(scr1)
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
    size = WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode(size)
    fon = pygame.transform.scale(load_image('fon.png'), (WIDTH, HEIGHT))
    pygame.font.get_fonts()
    font = pygame.font.SysFont('arial', 80)
    text_coord = 50
    string_rendered = font.render(intro_text[0], 1, (103, 0, 0))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord
    intro_rect.x = 100
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)
    btn_start = StartButton((100, 200), butHeigth=50, butWidth=250, text='Старт')
    btn_continue = ConButton((100, 500), butHeigth=50, butWidth=250, text='Продолжить')
    btn_desc = DescriptionButton((100, 350), butHeigth=50, butWidth=250, text='Описание')
    # btn_settings = Button((100, 550), butHeigth=100, butWidth=400, text='Настройки')
    global start
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        screen.blit(fon, (0, 0))
        screen.blit(string_rendered, intro_rect)
        btn_start.render(screen)
        btn_continue.render(screen)
        btn_desc.render(screen)
        # btn_settings.render(screen)
        pygame.display.flip()
        clock.tick(FPS)

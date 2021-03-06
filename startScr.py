import pygame
from SETTINGS import *
from Buildings import Castle_cl

pygame.init()
clock = pygame.time.Clock()
start1 = True
start = True
n = 0
king_sprites = pygame.sprite.Group()
king = Castle_cl(load_image('king.png'), 5, 1, 470, 250, king_sprites)
FPS = 60

pygame.time.set_timer(type_king, 400)


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
            pygame.draw.rect(screen, (90, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
            if pygame.mouse.get_pressed()[0] and self.mouse_in(mousePos):
                pygame.draw.rect(screen, (51, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
                global start, start1
                start = False
                start1 = False
                print(start, 3)
        else:
            pygame.draw.rect(screen, (122, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
        self.font = pygame.font.Font(pygame.font.get_default_font(), 30)
        valueSurf = self.font.render(f"{self.text}", True, (255, 255, 255))
        textx = self.position[0] + (self.width / 2) - (valueSurf.get_rect().width / 2)
        texty = self.position[1] + (self.heigth / 2) - (valueSurf.get_rect().height / 2)
        screen.blit(valueSurf, (textx, texty))


class ConButton(StartButton):
    def __init__(self, position, butHeigth, butWidth, text):
        super().__init__(position)
        self.position = position
        self.width = butWidth
        self.heigth = butHeigth
        self.text = text

    def render(self, screen):
        mousePos = pygame.mouse.get_pos()
        if self.mouse_in(mousePos):
            pygame.draw.rect(screen, (90, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
            if pygame.mouse.get_pressed()[0] and self.mouse_in(mousePos):
                pygame.draw.rect(screen, (51, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
                global start, food, foodplus, wood, woodplus, stone, stonplus, gold, goldplus, iron, ironres, \
                    population, populationplus, science, scienceplus, happiness, limit, days, \
                    structures_save, structures
                result = cur.execute('''SELECT * FROM Buildings''').fetchall()
                for elem in result:
                    grids[(elem[4], elem[5])] = False
                    structures_save[(elem[4], elem[5])] = (elem[1], elem[2], elem[3], (elem[4], elem[5]))
                start = False
        else:
            pygame.draw.rect(screen, (122, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
        self.font = pygame.font.Font(pygame.font.get_default_font(), 30)
        valueSurf = self.font.render(f"{self.text}", True, (255, 255, 255))
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
            pygame.draw.rect(screen, (90, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
            if pygame.mouse.get_pressed()[0] and self.mouse_in(mousePos):
                pygame.draw.rect(screen, (51, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
                global start1
                start1 = False

        else:
            pygame.draw.rect(screen, (122, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
        self.font = pygame.font.Font(pygame.font.get_default_font(), 30)
        valueSurf = self.font.render(f"{self.text}", True, (255, 255, 255))
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
            pygame.draw.rect(screen, (90, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
            if pygame.mouse.get_pressed()[0] and self.mouse_in(mousePos):
                pygame.draw.rect(screen, (51, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
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
                fon1 = pygame.transform.scale(load_image('fon.png'), (siz1[0], siz1[1]))

                btn_start1 = StartButton((100, 475), butHeigth=100, butWidth=200, text='К игре!')
                btn_back = BackButton((400, 475), butHeigth=100, butWidth=200, text='На главную.')
                scr1.blit(fon1, (0, 0))

                while start1:
                    scr1.blit(fon1, (0, 0))

                    for line in intro_text:
                        if text_coord < 425:
                            if line[-1] == '!':
                                line = line.rstrip('!')
                                string_rendered = font.render(line, 1, (125, 0, 0))
                                intro_rect = string_rendered.get_rect()
                                text_coord += 10
                                intro_rect.top = text_coord
                                intro_rect.x = 150
                                text_coord += intro_rect.height
                                scr1.blit(string_rendered, intro_rect)
                            else:
                                string_rendered = font.render(line, 1, (102, 0, 0))
                                intro_rect = string_rendered.get_rect()
                                text_coord += 10
                                intro_rect.top = text_coord
                                intro_rect.x = 100
                                text_coord += intro_rect.height
                                scr1.blit(string_rendered, intro_rect)

                    cursor_rect.center = pygame.mouse.get_pos()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            terminate()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                start1 = False
                    btn_start1.render(scr1)
                    btn_back.render(scr1)

                    if pygame.mouse.get_focused():
                        scr1.blit(mouse, cursor_rect)

                    if pygame.mouse.get_pressed()[0]:
                        scr1.blit(mouse1, cursor_rect)

                    text_coord = 25
                    pygame.display.flip()
                    clock.tick(FPS)
        else:
            pygame.draw.rect(screen, (122, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
        self.font = pygame.font.Font(pygame.font.get_default_font(), 30)
        valueSurf = self.font.render(f"{self.text}", True, (255, 255, 255))
        textx = self.position[0] + (self.width / 2) - (valueSurf.get_rect().width / 2)
        texty = self.position[1] + (self.heigth / 2) - (valueSurf.get_rect().height / 2)
        screen.blit(valueSurf, (textx, texty))


def terminate():
    pygame.quit()
    sys.exit()

def start_screen():
    global maxdays, start
    intro_text = ['Проект утопия', 'Максимально прожито дней:', str(maxdays)]
    size = WIDTH, HEIGHT = 900, 600
    screen1 = pygame.display.set_mode(size)
    fon1 = pygame.transform.scale(load_image('fon.png'), (WIDTH, HEIGHT))
    pygame.font.get_fonts()
    font = pygame.font.SysFont('arial', 80)
    font1 = pygame.font.SysFont('arial', 30)
    text_coord = 50
    string_rendered = font.render(intro_text[0], 1, (103, 0, 0))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord
    intro_rect.x = 100
    text_coord += intro_rect.height

    screen1.blit(string_rendered, intro_rect)
    text_coord = 200
    string_rendered2 = font1.render(intro_text[1], 1, (103, 0, 0))
    intro_rect2 = string_rendered2.get_rect()
    intro_rect2.top = text_coord
    intro_rect2.x = 375
    screen1.blit(string_rendered2, intro_rect2)
    string_rendered1 = font1.render(intro_text[2], 1, (103, 0, 0))
    intro_rect1 = string_rendered1.get_rect()
    intro_rect1.top = text_coord
    intro_rect1.x = 785
    screen1.blit(string_rendered, intro_rect1)

    btn_start = StartButton((100, 200), butHeigth=50, butWidth=250, text='Новая игра')
    btn_continue = ConButton((100, 500), butHeigth=50, butWidth=250, text='Продолжить')
    btn_desc = DescriptionButton((100, 350), butHeigth=50, butWidth=250, text='Описание')
    # btn_settings = Button((100, 550), butHeigth=100, butWidth=400, text='Настройки')

    # global start
    start = True
    print(start, 1)
    while start:
        cursor_rect.center = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == type_king:
                king.update()

        screen1.blit(fon1, (0, 0))
        screen1.blit(string_rendered, intro_rect)
        screen1.blit(string_rendered1, intro_rect1)
        screen1.blit(string_rendered2, intro_rect2)
        btn_start.render(screen1)
        btn_continue.render(screen1)
        btn_desc.render(screen1)

        king_sprites.draw(screen1)

        if pygame.mouse.get_focused():
            screen1.blit(mouse, cursor_rect)

        if pygame.mouse.get_pressed()[0]:
            screen1.blit(mouse1, cursor_rect)
        # btn_settings.render(screen)
        pygame.display.flip()
        clock.tick(FPS)

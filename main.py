import pygame
import os
import sys


pygame.init()
size = WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

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

def start_screen():
    intro_text = ['Проект утопия',
                  'Описание:!',
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

    # fon = pygame.transform.scale(load_image('фон.jpg'), (WIDTH, HEIGHT))
    # screen.blit(fon, (0, 0)) пока изображения нет
    font = pygame.font.Font(None, 30)
    text_coord = 50
    n = 0
    for line in intro_text:
        if n == 0:
            string_rendered = font.render(line, 1, (0, 125, 125))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 300
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
            n = 1
        elif line[-1] == '!':
            line = line.rstrip('!')
            string_rendered = font.render(line, 1, (125, 0, 0))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 80
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        else:
            string_rendered = font.render(line, 1, (125, 0, 0))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 40
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)

start_screen()
size = WIDTH, HEIGHT = 1920, 1200
screen = pygame.display.set_mode(size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
    pygame.display.flip()
    clock.tick(FPS)
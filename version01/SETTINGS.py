import pygame as pg, os, sys
import copy
import sqlite3

TILE_SIZE = 100

type_farm = pg.USEREVENT + 1
type_castle = pg.USEREVENT + 2
type_res = pg.USEREVENT + 3
type_mill = pg.USEREVENT + 4
type_days = pg.USEREVENT + 5
type_quarry = pg.USEREVENT + 6
type_ironmine = pg.USEREVENT + 7
type_barracks = pg.USEREVENT + 8
type_university = pg.USEREVENT
type_goldmine = pg.USEREVENT + 10
type_village = pg.USEREVENT + 11
type_error = pg.USEREVENT
type_event = pg.USEREVENT
type_pausemenu = pg.USEREVENT
type_endpause = pg.USEREVENT

grids = {(12, 4): True, (4, 0): True, (8, -9): False, (5, 1): True, (8, 0): True, (10, -3): True, (19, 0): False,
         (11, -4): True, (17, 3): True, (10, 6): True, (9, 8): False, (11, 5): True, (2, 2): False, (15, -4): False,
         (6, -7): False, (13, 8): False, (15, 5): False, (6, 2): True, (7, 1): True, (18, 1): True, (12, -3): True,
         (4, 2): True, (8, -7): False, (10, -10): False, (9, -8): False, (5, 3): True, (8, 2): True, (19, 2): False,
         (9, 1): True, (0, -1): False, (11, -2): True, (11, -1): True, (11, 7): True, (13, 1): True, (15, -2): True,
         (6, -5): False, (15, -1): True, (7, -6): False, (6, 4): True, (7, 3): True, (18, 3): False, (4, -5): False,
         (5, -4): False, (8, -5): True, (10, -8): True, (9, -6): True, (11, -9): False, (5, 5): False, (8, 4): True,
         (17, -2): False, (9, 3): True, (0, 0): False, (2, -3): False, (11, 0): True, (13, -6): False, (11, 9): True,
         (13, 3): True, (15, 0): True, (6, -3): True, (7, -4): True, (6, 6): False, (7, 5): True, (3, 1): True,
         (5, -2): True, (5, -1): True, (10, -6): True, (9, -4): True, (11, -7): True, (8, -3): True, (14, 1): True,
         (17, 0): True, (9, 5): True, (11, 2): True, (13, -4): True, (13, 5): True, (15, 2): True, (16, 1): True,
         (7, -2): True, (7, -1): True, (18, -2): False, (18, -1): False, (7, 7): False, (20, 1): False, (14, -6): False,
         (12, 6): True, (3, 3): False, (5, 0): True, (14, 3): True, (17, 2): True, (9, -2): True, (11, -5): True,
         (9, -1): True, (9, 7): True, (11, 4): True, (13, -2): True, (15, -5): False, (13, -1): True, (10, 8): False,
         (13, 7): True, (15, 4): True, (6, 1): True, (16, 3): True, (7, 0): True, (18, 0): True, (19, -1): False,
         (3, -4): False, (14, -4): True, (8, -8): False, (9, -9): False, (14, 5): True, (5, 2): True, (4, 4): False,
         (12, 8): True, (9, 0): True, (11, -3): True, (17, 4): False, (9, 9): False, (10, 1): True, (1, -1): False,
         (1, -2): False, (6, -6): False, (15, -3): True, (7, -7): False, (16, -4): False, (13, 0): True, (10, 10): False,
         (16, 5): False, (7, 2): True, (18, 2): False, (15, 6): False, (12, 1): True, (3, -2): False, (5, -5): False,
         (4, -3): False, (3, -1): True, (9, -7): True, (14, -2): True, (5, 4): True, (14, -1): True, (17, -3): False,
         (9, 2): True, (14, 7): False, (13, -7): False, (8, 6): True, (10, 3): True, (1, 0): False, (13, 2): True,
         (16, -2): True, (7, -5): True, (16, -1): True, (7, 4): True, (12, -6): True, (12, 3): True, (3, 0): True,
         (5, -3): True, (14, 0): True, (9, -5): True, (10, -4): True, (13, -5): True, (8, 8): False, (10, 5): True,
         (13, 4): True, (2, 1): True, (16, 0): True, (7, -3): True, (17, -1): True, (20, 0): False, (12, -4): True,
         (12, 5): True, (3, 2): True, (14, 2): True, (4, 1): True, (8, 1): True, (10, -2): True, (10, -1): True,
         (13, -3): True, (19, 1): True, (10, 7): True, (11, 6): True, (16, 2): True, (6, 3): True, (12, -2): True,
         (14, -5): False, (12, -1): True, (9, -10): False, (14, 4): True, (12, 7): False, (4, 3): True, (8, -6): True,
         (10, -9): False, (8, 3): True, (10, 0): True, (7, -8): False, (10, 9): True, (11, 8): True, (16, 4): False,
         (6, -4): True, (6, 5): True, (12, 0): True, (3, -3): False, (5, -6): False, (4, -4): False, (14, -3): True,
         (12, 9): False, (14, 6): True, (8, -4): True, (10, -7): True, (11, -8): False, (8, 5): True, (10, 2): True,
         (9, 4): True, (11, 1): True, (2, -2): False, (2, -1): False, (16, -3): False, (11, 10): False, (15, 1): True,
         (6, -2): True, (6, -1): True, (12, -7): False, (7, 6): True, (12, 2): False, (4, -2): True, (4, -1): True,
         (17, 1): True, (8, -2): True, (10, -5): True, (9, -3): True, (11, -6): True, (8, -1): True, (8, 7): True,
         (10, 4): True, (1, 1): False, (11, 3): True, (2, 0): True, (9, 6): True, (13, 6): True, (15, 3): True,
         (6, 0): True, (12, -5): True, (12, -8): False}

structures_save = copy.copy(grids)

army = 0
food, wood, stone, iron, gold, science, population, happiness, days, limit = \
    500, 400, 200, 100, 200, 0, 300, 60, 0, 400
foodplus, woodplus, stoneplus, ironplus, goldplus, scienceplus, populationplus = 1, 1, 0, 0, 1, 0, 1

structures = []

for i in grids:
    structures_save[i] = 0
con = sqlite3.connect("data/Save.db")
cur = con.cursor()

record = 0


def load_image(name):
    fullname = os.path.join('data/images', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    return image


def terminate():
    con.close()
    pg.quit()
    sys.exit()


pause_cycle, pause1_cycle, cont = False, False, False

start = True

mountains = [(10, 10), (10, 9), (10, 8), (11, 10), (11, 9), (11, 8), (12, 9), (12, 8), (12, 7), (13, 8), (13, 7),
             (13, 6), (14, 6), (14, 7)]

can_build, is_army, army_height, army_width, info_army, army_level, finish = True, False, 40, 400, [], 0, False

mouse, mouse1 = load_image('cursor.png'), load_image('cursor1.png')
cursor_rect = mouse.get_rect()
mouse_sprite = pg.sprite.Sprite()

import pygame as pg


class Castle(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.animation = [
            pg.image.load('data/castle/castle.png'),
            pg.image.load('data/castle/castle_n2.png'),
            pg.image.load('data/castle/castle_n3.png'),
            pg.image.load('data/castle/castle_n4.png'),
            pg.image.load('data/castle/castle_n5.png')
                          ]
        self.cur_image = 0
        self.image = self.animation[self.cur_image]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):

        self.cur_image += 0.1

        if self.cur_image >= len(self.animation):
            self.cur_image = 0

        self.image = self.animation[int(self.cur_image)]
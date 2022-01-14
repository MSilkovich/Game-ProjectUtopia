import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Farm(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, sprite_group, event):
        super().__init__(sprite_group)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.n = 0
        self.type = event


    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        if self.n < 2:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            self.n += 1
        else:
            pygame.time.set_timer(self.type, 0)


class Mill(Farm):
    def __init__(self, sheet, columns, rows, x, y, sprite_group, event):
        super().__init__(sheet, columns, rows, x, y, sprite_group, event)

    def update(self):
        if self.n < 2:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            self.n += 1
        else:
            pygame.time.set_timer(self.type, 0)


class Quarry(Farm):
    def init(self, sheet, columns, rows, x, y, sprite_group, event):
        super().__init__(sheet, columns, rows, x, y, sprite_group, event)

    def update(self):
        if self.m < 2:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            self.m += 1
        else:
            pygame.time.set_timer(self.type, 0)


class Castle_cl(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, sprites):
        super().__init__(sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                            sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

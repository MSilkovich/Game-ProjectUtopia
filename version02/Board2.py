import pygame as pg
from SETTINGS import TILE_SIZE


class Board:
    def __init__(self, width, height, grid_length_x=21, grid_length_y=20,
                 left=10, top=10):
        self.grid_length_x = grid_length_x
        self.grid_length_y = grid_length_y
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = left
        self.top = top
        self.cell_size = 30
        self.world = self.create_world()
        self.temp_tile = None
        self.grid_pos = (0, 0)
        self.iso_poly1 = [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)]
        self.iso_poly2 = [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)]

    def update(self):
        mouse_pos = pg.mouse.get_pos()
        self.grid_pos = self.mouse_to_grid(mouse_pos[0], mouse_pos[1])
        try:
            self.iso_poly = self.world[self.grid_pos[0]][self.grid_pos[1]]["iso_poly"]
            self.temp_tile = {
                "iso_poly": self.iso_poly
            }
        except IndexError:
                pass

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def create_world(self):
        world = []

        for grid_x in range(self.grid_length_x):
            world.append([])
            for grid_y in range(self.grid_length_y):
                world_tile = self.grid_to_world(grid_x, grid_y)
                world[grid_x].append(world_tile)

        return world

    def grid_to_world(self, grid_x, grid_y):

        rect = [
            (grid_x * TILE_SIZE, grid_y * TILE_SIZE),
            (grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE),
            (grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE),
            (grid_x * TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE)
        ]

        iso_poly = [self.cart_to_iso(x, y) for x, y in rect]

        minx = min([x for x, y in iso_poly])
        miny = min([y for x, y in iso_poly])

        tile = ""

        out = {
            "grid": [grid_x, grid_y],
            "cart_rect": rect,
            "iso_poly": iso_poly,
            "render_pos": [minx, miny],
            "tile": tile
        }

        return out

    def cart_to_iso(self, x, y):
        iso_x = x - y + 1000
        iso_y = (x + y) / 2 - 320
        return iso_x, iso_y

    def mouse_to_grid(self, x, y):
        # transform to world position
        world_x = x
        world_y = y
        # transform to cart
        cart_y = (2 * world_y - world_x) / 2
        cart_x = cart_y + world_x
        # transform to grid coordinates
        grid_x = int(cart_x // TILE_SIZE)
        grid_y = int(cart_y // TILE_SIZE)
        return grid_x, grid_y

    def draw(self, screen):
        # for x in range(self.grid_length_x):
        #     for y in range(self.grid_length_y):
        #
        #         p = self.world[x][y]["iso_poly"]
        #         p = [(x + self.width / 2, y + self.height / 4) for x, y in p]
        #         pygame.draw.polygon(screen, (255, 0, 0), p, 1) # drawing grid

        if self.temp_tile is not None:
            iso_poly = self.temp_tile["iso_poly"]
            self.iso_poly1 = [(x - 990, y + 305) for x, y in iso_poly] # left_side первая координата - нижний угол, вторая - правый угол, третья - верхний угол, четвертая - левый угол
            self.iso_poly2 = [(x + 1010, y - 695) for x, y in iso_poly] # right_side первая координата - верхний угол, вторая - правый угол, третья - нижний угол, четвертая - левый угол
            if self.grid_pos[1] <= -1:
                if self.grid_pos[0] == 19 and self.grid_pos[1] <= -1:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly2, 3)
                elif self.grid_pos[0] == 18 and self.grid_pos[1] <= -1:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly2, 3)
                elif self.grid_pos[0] == 17 and self.grid_pos[1] <= -2:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly2, 3)
                elif self.grid_pos[0] == 16 and self.grid_pos[1] <= -3:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly2, 3)
                elif self.grid_pos[0] == 15 and self.grid_pos[1] <= -4:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly2, 3)
                elif self.grid_pos[0] == 14 and self.grid_pos[1] <= -5:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly2, 3)
                elif self.grid_pos[0] == 13 and self.grid_pos[1] <= -6:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly2, 3)
                elif self.grid_pos[0] == 12 and self.grid_pos[1] <= -7:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly2, 3)
                elif self.grid_pos[0] == 11 and self.grid_pos[1] <= -8:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly2, 3)
                elif self.grid_pos[0] == 10 and self.grid_pos[1] <= -9:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly2, 3)
                elif self.grid_pos[0] == 9 and self.grid_pos[1] <= -8:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly2, 3)
                elif self.grid_pos[0] == 8 and self.grid_pos[1] <= -7:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly2, 3)
                elif self.grid_pos[0] == 7 and self.grid_pos[1] <= -6:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly2, 3)
                elif self.grid_pos[0] == 6 and self.grid_pos[1] <= -5:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly2, 3)
                elif self.grid_pos[0] == 5 and self.grid_pos[1] <= -4:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly2, 3)
                elif self.grid_pos[0] == 4 and self.grid_pos[1] <= -3:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly2, 3)
                elif self.grid_pos[0] == 3 and self.grid_pos[1] <= -2:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly2, 3)
                elif self.grid_pos[0] == 2 and self.grid_pos[1] <= -1:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly2, 3)
                elif self.grid_pos[0] == 1 and self.grid_pos[1] <= -1:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly2, 3)
                elif self.grid_pos[0] == 0 and self.grid_pos[1] <= -1:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly2, 3)
                else:
                    pg.draw.polygon(screen, (255, 255, 255), self.iso_poly2, 3)

            elif self.grid_pos[1] >= 0:
                if self.grid_pos[0] == 20 and self.grid_pos[1] <= 1:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly1, 3)
                elif self.grid_pos[0] == 19 and self.grid_pos[1] == 0:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly1, 3)
                elif self.grid_pos[0] == 19 and self.grid_pos[1] == 2:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly1, 3)
                elif self.grid_pos[0] == 18 and self.grid_pos[1] <= 3 and self.grid_pos[1] > 1:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly1, 3)
                elif self.grid_pos[0] == 17 and self.grid_pos[1] == 4:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly1, 3)
                elif self.grid_pos[0] == 16 and (self.grid_pos[1] == 5 or self.grid_pos[1] == 4):
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly1, 3)
                elif self.grid_pos[0] == 15 and (self.grid_pos[1] == 6 or self.grid_pos[1] == 5):
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly1, 3)
                elif self.grid_pos[0] == 14 and (self.grid_pos[1] == 7):
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly1, 3)
                elif self.grid_pos[0] == 13 and (self.grid_pos[1] == 8):
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly1, 3)
                elif self.grid_pos[0] == 12 and (self.grid_pos[1] == 9 or self.grid_pos[1] == 7):
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly1, 3)
                elif self.grid_pos[0] == 11 and (self.grid_pos[1] == 10):
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly1, 3)
                elif self.grid_pos[0] == 10 and (self.grid_pos[1] == 10 or self.grid_pos[1] == 8):
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly1, 3)
                elif self.grid_pos[0] == 9 and self.grid_pos[1] >= 8:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly1, 3)
                elif self.grid_pos[0] == 8 and self.grid_pos[1] == 8:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly1, 3)
                elif self.grid_pos[0] == 7 and self.grid_pos[1] == 7:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly1, 3)
                elif self.grid_pos[0] == 6 and self.grid_pos[1] == 6:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly1, 3)
                elif self.grid_pos[0] == 5 and self.grid_pos[1] == 5:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly1, 3)
                elif self.grid_pos[0] == 4 and self.grid_pos[1] == 4:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly1, 3)
                elif self.grid_pos[0] == 3 and self.grid_pos[1] == 3:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly1, 3)
                elif self.grid_pos[0] == 2 and self.grid_pos[1] == 2:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly1, 3)
                elif self.grid_pos[0] == 1 and self.grid_pos[1] <= 1:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly1, 3)
                elif self.grid_pos[0] == 0 and self.grid_pos[1] == 0:
                    pg.draw.polygon(screen, (255, 0, 0), self.iso_poly1, 3)
                else:
                    pg.draw.polygon(screen, (255, 255, 255), self.iso_poly1, 3)
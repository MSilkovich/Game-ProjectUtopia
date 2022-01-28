import pygame
from SETTINGS import *


class QuitButton:
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
                terminate()
        else:
            pygame.draw.rect(screen, (122, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
        self.font = pygame.font.Font(pygame.font.get_default_font(), 23)
        valueSurf = self.font.render(f"{self.text}", True, (255, 255, 255))
        textx = self.position[0] + (self.width / 2) - (valueSurf.get_rect().width / 2)
        texty = self.position[1] + (self.heigth / 2) - (valueSurf.get_rect().height / 2)
        screen.blit(valueSurf, (textx, texty))


# class ContButton(QuitButton):
#     def __init__(self, position: tuple, butHeigth: int = 40, butWidth: int = 150, text: str = "Кнопка",
#                  pause_cycle: bool = "", pause1_cycle : bool = ""):
#         super().__init__(position)
#         self.position = position
#         self.width = butWidth
#         self.heigth = butHeigth
#         self.text = text
#         self.pause_cycle = pause_cycle
#         self.pause1_cycle = pause_cycle
#
#     def render(self, screen):
#         mousePos = pygame.mouse.get_pos()
#         if self.mouse_in(mousePos):
#             pygame.draw.rect(screen, (90, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
#             if pygame.mouse.get_pressed()[0] and self.mouse_in(mousePos):
#                 pygame.draw.rect(screen, (51, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
#                 self.pause1_cycle = True
#                 self.pause_cycle = False
#         else:
#             pygame.draw.rect(screen, (122, 0, 0), (self.position[0], self.position[1], self.width, self.heigth))
#         self.font = pygame.font.Font(pygame.font.get_default_font(), 23)
#         valueSurf = self.font.render(f"{self.text}", True, (255, 255, 255))
#         textx = self.position[0] + (self.width / 2) - (valueSurf.get_rect().width / 2)
#         texty = self.position[1] + (self.heigth / 2) - (valueSurf.get_rect().height / 2)
#         screen.blit(valueSurf, (textx, texty))
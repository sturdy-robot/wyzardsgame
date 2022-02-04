import pygame
from pygame.sprite import AbstractGroup
from typing import Union


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, tilesize: int, color: Union[str, tuple], *groups: AbstractGroup):
        super().__init__(*groups)
        self.image = pygame.Surface((tilesize, tilesize))
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill(color)

    def scroll(self, scroll_x, scroll_y):
        self.rect.x += scroll_x
        self.rect.y += scroll_y

    def update(self, scroll_x, scroll_y):
        self.scroll(scroll_x, scroll_y)

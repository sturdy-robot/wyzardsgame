import pygame
from typing import Union, Any


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, tilesize: int, color: Union[str, tuple], *groups: Any):
        super().__init__(*groups)
        self.image = pygame.Surface((tilesize, tilesize))
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill(color)


class ObstacleTile(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, tilesize: int, color: Union[str, tuple], *groups: Any):
        super().__init__(*groups)
        self.image = pygame.Surface((tilesize, tilesize))
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill(color)
        self.hitbox = self.rect.inflate(0, -6)

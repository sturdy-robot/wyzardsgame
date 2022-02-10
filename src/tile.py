import pygame
from typing import Union, Any


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, image: str, *groups: Any):
        super().__init__(*groups)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(topleft=pos)


class ObstacleTile(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, image: str, *groups: Any):
        super().__init__(*groups)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)

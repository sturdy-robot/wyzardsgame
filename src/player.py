import pygame
from pygame.sprite import AbstractGroup


class Player(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, *groups: AbstractGroup):
        super().__init__(*groups)
        self.image = pygame.Surface((16, 32))
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2()
        self.image.fill('blue')
        self.speed_x = 0
        self.speed_y = 0

    def get_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.direction.y = -1
            if event.key == pygame.K_DOWN:
                self.direction.y = 1
            if event.key == pygame.K_LEFT:
                self.direction.x = -1
            if event.key == pygame.K_RIGHT:
                self.direction.x = 1

        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                self.direction.y = 0
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                self.direction.x = 0

    def update_position(self):
        self.rect.x += self.direction.x * self.speed_x
        self.rect.y += self.direction.y * self.speed_y

    def update(self, event):
        self.get_input(event)
        self.update_position()

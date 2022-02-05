import pygame
from pygame.sprite import AbstractGroup


class Player(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, *groups: AbstractGroup):
        super().__init__(*groups)
        self.image = pygame.Surface((16, 32))
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -6)
        self.direction = pygame.math.Vector2()
        self.image.fill('blue')
        self.speed = 5

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * self.speed
        self.hitbox.y += self.direction.y * self.speed
        self.rect.center = self.hitbox.center

    def update(self):
        self.get_input()
        self.move()

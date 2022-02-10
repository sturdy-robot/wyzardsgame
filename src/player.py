import pygame
from typing import Any


class Player(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, *groups: Any):
        super().__init__(*groups)
        self.image = pygame.image.load('assets/character/character.png')
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.direction = pygame.math.Vector2()

        self.stats = {
            "health": 100,
            "mana": 50,
            "attack": 10,
            "magic": 4,
            "speed": 5
        }
        self.health = self.stats["health"]
        self.mana = self.stats["mana"]
        self.speed = self.stats["speed"]

    def collision(self, direction, obstacle_sprites):
        if direction == 1:
            for sprite in obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
        if direction == 0:
            for sprite in obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

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

    def move(self, obstacle_sprites):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * self.speed
        self.collision(1, obstacle_sprites)
        self.hitbox.y += self.direction.y * self.speed
        self.collision(0, obstacle_sprites)
        self.rect.center = self.hitbox.center

    def update(self, obstacle_sprites):
        self.get_input()
        self.move(obstacle_sprites)

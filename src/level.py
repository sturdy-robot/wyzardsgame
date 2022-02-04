import pygame
from player import Player
from tile import Tile
from typing import Union
from pathlib import Path


class Level:
    def __init__(self, level_file: Union[str, Path]):
        self.levelfile = level_file
        self.tilesize = 16
        self.tiles = pygame.sprite.Group()
        self.__player = pygame.sprite.GroupSingle()
        self.setup()
        self.display = pygame.display.get_surface()
        self.world_shift_x = 0
        self.world_shift_y = 0
        self.scroll = 5

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, player: pygame.sprite.Sprite):
        self.__player.add(player)

    def setup(self):
        self.open_level_file()

    def open_level_file(self):
        with open(self.levelfile, 'r') as fp:
            leveldata = fp.read().splitlines()
            self.parse_level_data(leveldata)

    def parse_level_data(self, leveldata: list):
        for i, row in enumerate(leveldata):
            for j, cell in enumerate(row):
                x = j * self.tilesize
                y = i * self.tilesize
                if cell == '.':
                    tile = Tile((x, y), self.tilesize, "green")
                    self.tiles.add(tile)
                elif cell == 'P':
                    self.player = Player((x, y))
                elif cell == 't':
                    tile = Tile((x, y), self.tilesize, "yellow")
                    self.tiles.add(tile)
                elif cell == 'x':
                    tile = Tile((x, y), self.tilesize, "gray")
                    self.tiles.add(tile)

    def world_scroll_x(self):
        screen_width, screen_height = self.display.get_size()
        if self.player.sprite.rect.centerx < screen_width / 2.8 and self.player.sprite.direction.x < 0:
            self.world_shift_x = self.scroll
            self.player.sprite.speed_x = 0
        elif self.player.sprite.rect.centerx > screen_width - (screen_width / 2.8) and self.player.sprite.direction.x > 0:
            self.world_shift_x = -self.scroll
            self.player.sprite.speed_x = 0
        else:
            self.world_shift_x = 0
            self.player.sprite.speed_x = self.scroll

    def world_scroll_y(self):
        screen_width, screen_height = self.display.get_size()
        if self.player.sprite.rect.centery < screen_height / 2.8 and self.player.sprite.direction.y < 0:
            self.world_shift_y = self.scroll
            self.player.sprite.speed_y = 0
        elif self.player.sprite.rect.centery > screen_height - (screen_height / 2.8) and self.player.sprite.direction.y > 0:
            self.world_shift_y = -self.scroll
            self.player.sprite.speed_y = 0
        else:
            self.world_shift_y = 0
            self.player.sprite.speed_y = self.scroll

    def update_render(self, display):
        self.tiles.draw(display)
        self.player.draw(display)

    def update(self, event):
        self.player.update(event)
        self.world_scroll_x()
        self.world_scroll_y()
        self.tiles.update(self.world_shift_x, self.world_shift_y)

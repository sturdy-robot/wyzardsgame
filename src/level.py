import pygame
from player import Player
from tile import Tile, ObstacleTile
from typing import Union, Sequence
from pathlib import Path
from ui import UI


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self, *sprites: Union[pygame.sprite.Sprite, Sequence[pygame.sprite.Sprite]]):
        super().__init__(*sprites)
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        w, h = self.display_surface.get_size()
        self.half_width = w // 2
        self.half_height = h // 2

    def custom_draw(self, player, back_tiles):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for tile in back_tiles:
            offset_pos = tile.rect.topleft - self.offset
            self.display_surface.blit(tile.image, offset_pos)

        for sprite in sorted(self.sprites(), key=lambda spr: spr.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)


class Level:
    def __init__(self, level_file: Union[str, Path]):
        self.levelfile = level_file
        self.tilesize = 32
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_tiles = pygame.sprite.Group()
        self.back_tiles = pygame.sprite.Group()
        self.__player = pygame.sprite.GroupSingle()
        self.setup()
        self.display = pygame.display.get_surface()
        self.ui = UI()

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, player: Player):
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
                if cell == 'P':
                    Player((x, y), [self.player, self.visible_sprites])
                elif cell == 't':
                    ObstacleTile((x, y), 'assets/tiles/gold.png', [self.obstacle_tiles, self.visible_sprites])
                elif cell == 'x':
                    ObstacleTile((x, y), 'assets/tiles/rock.png', [self.obstacle_tiles, self.visible_sprites])
                Tile((x, y), "assets/tiles/grass.png", self.back_tiles)

    def update(self):
        self.back_tiles.update()
        self.player.update(self.obstacle_tiles)
        self.obstacle_tiles.update()
        self.visible_sprites.custom_draw(self.player.sprite, self.back_tiles)
        self.ui.display(self.player.sprite)


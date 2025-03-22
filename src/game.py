import pygame

from sprites.background import Background
from sprites.player import Player

class Game:
    def __init__(self):
        self.__background = Background()
        self.__player = Player()
        self.__all_sprites = pygame.sprite.Group(self.__background, self.__player)

    def draw(self, surface):
        self.__all_sprites.draw(surface)

    def update(self, dt):
        self.__all_sprites.update(dt)

    def walk(self, direction):
        self.__player.walk(direction)

    def stop_player(self):
        self.__player.stop()

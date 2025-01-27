import pygame
from settings import *
from Pathfinder import Pathfinder


class Object(pygame.sprite.Sprite):
    def __init__(self, new_pos):
        super().__init__()
        self.pos = new_pos
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect(topleft = self.pos)
        self.image.fill("blue")
        self.collide = False

    def update(self):
        self.collisions(player_sprites)

    def access_guard_pos(self):
        from main import new_game
        obj = new_game.get_guard_pos()
        return obj

    def call_find_path(self):
        from main import new_game
        new_game.guard.find_path(self.rect.centerx, self.rect.centery)

    def collisions(self, player_sprites):
        for i in player_sprites:
            if i.rect.colliderect(self.rect):
                self.call_find_path()
                
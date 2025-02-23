import pygame
from settings import *


class Object(pygame.sprite.Sprite):
    def __init__(self, new_pos, new_guard):
        super().__init__()
        self.pos = new_pos
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect(topleft = self.pos)
        self.image.fill("grey")
        self.collide = False
        self.guard = new_guard

    def update(self):
        self.collisions(player_sprites)

    def access_guard_pos(self):
        from main import new_game
        obj = new_game.get_guard_pos()
        return obj


    def collisions(self, player_sprites):
        if not self.collide:
            for i in player_sprites:
                if i.rect.colliderect(self.rect):
                    self.collide = True
                    self.guard.find_path(self.rect.centerx, self.rect.centery)

                
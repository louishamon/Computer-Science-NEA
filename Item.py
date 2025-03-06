import pygame
from settings import *

class Item(pygame.sprite.Sprite):
    def __init__(self, new_pos):
        super().__init__()
        self.pos = new_pos
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect(topleft = self.pos)
        self.image.fill("red")
        self.collide = False

    def update(self):
        self.collisions(player_sprites)

    def collisions(self, player_sprites):
        if not self.collide:
            for i in player_sprites:
                if i.rect.colliderect(self.rect):
                    self.collide = True
                    i.keycard = True
                    self.kill()
import pygame
from settings import *

class Vault(pygame.sprite.Sprite):
    def __init__(self, new_pos):
        super().__init__()
        self.pos = new_pos
        self.image = pygame.Surface((70, 70))
        self.rect = self.image.get_rect(topleft = self.pos)
        self.image.fill("gold")
        self.collide = False
        self.winner = False

    def update(self):
        self.collisions(player_sprites)

    def collisions(self, player_sprites):
        if not self.collide:
            for i in player_sprites:
                if i.rect.colliderect(self.rect):
                    self.collide = True
                    if i.keycard:
                        self.winner = True
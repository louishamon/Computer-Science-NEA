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

    def update(self):
        self.collisions(player_sprites)

    def access_guard_pos(self):
        from main import new_game
        obj = new_game.get_guard_pos()
        return obj

    def collisions(self, player_sprites):
        for i in player_sprites:
            if i.rect.colliderect(self.rect):
                #print("collision")
                pathfinder = Pathfinder(game_map, self.access_guard_pos(), (int(self.rect.centerx), int(self.rect.centery)))
                pathfinder.find_path()
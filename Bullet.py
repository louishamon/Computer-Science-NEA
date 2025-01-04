import pygame
import math
from settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, new_damage, new_angle, new_x, new_y, new_team):
        super().__init__()
        self.damage = new_damage
        self.angle = new_angle
        self.pos = (new_x, new_y)
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect(topleft = self.pos)
        self.image.fill("black")
        self.rect.center = (new_x, new_y)
        self.speed = 50
        self.x_vel = self.speed * math.cos(math.radians(self.angle))
        self.y_vel = self.speed * math.sin(math.radians(self.angle))
        self.team = new_team

    def update(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        self.collisions(collision_objects, guard_sprites)

    def collisions(self, collision_objects, guard_sprites):
        for i in collision_objects:
            if i.rect.colliderect(self.rect):
                self.kill()
        for i in guard_sprites:
            if i.rect.colliderect(self.rect) and self.team == "player":
                i.hp -= self.damage
                print(i.hp)
                self.kill()
                
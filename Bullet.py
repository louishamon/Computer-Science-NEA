import pygame
import math
from settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, new_damage, new_angle, new_x, new_y, new_team, new_shooter):
        super().__init__()
        self.damage = new_damage
        self.angle = new_angle
        self.pos = (new_x, new_y)
        self.team = new_team
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect(topleft = self.pos)
        self.image.fill(self.get_colour())
        self.rect.center = (new_x, new_y)
        self.speed = 40
        self.x_vel = self.speed * math.cos(math.radians(self.angle))
        self.y_vel = self.speed * math.sin(math.radians(self.angle))
        self.seen = False
        self.shooter = new_shooter

    def get_colour(self):
        if self.damage == 0:
            return "red"
        else:
            return "black"
    

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
                self.kill()
        for i in player_sprites:
            if i.rect.colliderect(self.rect) and self.team == "sight":
                #if pygame.time.get_ticks() - self.shooter.previous_path_time > 1000:
                    #self.shooter.previous_path_time = pygame.time.get_ticks()
                self.shooter.find_path(i.rect.centerx, i.rect.centery)
                print(self.shooter.path)
                self.kill()
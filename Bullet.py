import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, new_damage, new_angle, new_x, new_y):
        self.damage = new_damage
        self.angle = new_angle
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect(topleft = self.pos)
        self.image.fill("black")
        self.rect.center = (new_x, new_y )
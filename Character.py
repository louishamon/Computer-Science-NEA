import pygame

class Character(pygame.sprite.Sprite):
  def __init__(self, size, pos):
    super().__init__()
    self.movement_speed = 4
    self.current_weapon = None
    self.hp = 100
    self.image = self.image = pygame.Surface((size[0], size[1]))
    self.rect = self.image.get_rect(topleft = pos)
    self.x_direction = 0
    self.y_direction = 0

  def die(self):
    if self.hp == 0:
      self.kill()

  def x_collisions(self, wall_sprites):
    for i in wall_sprites:
      if i.rect.colliderect(self.rect):
        if self.x_direction > 0:
          self.rect.right = i.rect.left
        else:
          self.rect.left = i.rect.right


  def y_collisions(self, wall_sprites):
    for i in wall_sprites:
      if i.rect.colliderect(self.rect):
        if self.y_direction < 0:
          self.rect.top = i.rect.bottom
        else:
          self.rect.bottom = i.rect.top
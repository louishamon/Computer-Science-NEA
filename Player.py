from Character import *
import pygame

class Player(Character):
  def __init__(self, new_size, new_pos):
    super().__init__(new_size, new_pos)
    self.disguise = None
    self.ammo = 30
    self.gun_held = (30, 2)
    self.keycard = False
    self.vault_keycard = False
    self.usb = False
    self.suspicious = False

  def update(self):
    self.get_input()
    self.rect.x += self.x_direction
    self.rect.y += self.y_direction
    #self.x_collisions(wall_sprites)
    #self.y_collisions(wall_sprites)
  
  def get_input(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
      self.x_direction = self.movement_speed
    elif keys[pygame.K_a]:
      self.x_direction = -self.movement_speed
    else:
      self.x_direction = 0
    if keys[pygame.K_w]:
      self.y_direction = -self.movement_speed
    elif keys[pygame.K_s]:
      self.y_direction = self.movement_speed
    else:
      self.y_direction = 0
from Character import *
from settings import *
import pygame

class Player(Character):
  def __init__(self, new_pos):
    super().__init__(new_pos)
    self.image_setup = pygame.image.load("survivor_no_background.png").convert_alpha()
    self.image = pygame.transform.scale(self.image_setup, (60, 40))
    self.base_player_image = self.image
    self.hitbox_rect = self.base_player_image.get_rect(topleft = self.pos)
    self.rect = self.hitbox_rect.copy()
    self.disguise = None
    self.ammo = 30
    self.gun_held = (30, 2)
    self.keycard = False
    self.vault_keycard = False
    self.usb = False
    self.suspicious = False
    self.rot = 0
    
    
    

  def update(self):
    self.get_input()
    self.rect.x += self.x_direction
    self.x_collisions(collision_objects)
    self.rect.y += self.y_direction
    self.y_collisions(collision_objects)
    
  
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

  def rotation(self):
    pass
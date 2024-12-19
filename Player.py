from Character import *
from settings import *
import pygame
import math

class Player(Character):
  def __init__(self, new_pos):
    super().__init__(new_pos)
    self.image_setup = pygame.image.load("survivor_no_background.png").convert_alpha()
    self.image = pygame.transform.scale(self.image_setup, (60, 40))
    self.base_player_image = self.image
    self.rect = self.image.get_rect(topleft = self.pos)
    self.hitbox_rect = player_hitbox
    self.hitbox_rect.center = self.rect.center
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
    self.hitbox_rect.centerx += self.x_direction  
    self.player_x_collisions(collision_objects)
    self.hitbox_rect.centery += self.y_direction
    self.player_y_collisions(collision_objects)
    self.rotation()
    self.rect.center = self.hitbox_rect.center
    
  
    
  
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

  def player_x_collisions(self, wall_sprites):
    for i in wall_sprites:
      if i.rect.colliderect(self.hitbox_rect):
        if self.x_direction > 0:
          self.hitbox_rect.right = i.rect.left
        else:
          self.hitbox_rect.left = i.rect.right


  def player_y_collisions(self, wall_sprites):
    for i in wall_sprites:
      if i.rect.colliderect(self.hitbox_rect):
        if self.y_direction < 0:
          self.hitbox_rect.top = i.rect.bottom
        else:
          self.hitbox_rect.bottom = i.rect.top

  
  def rotation(self):
    mouse_pos = pygame.mouse.get_pos()
    x_difference = mouse_pos[0] - self.rect.center[0]
    y_difference = mouse_pos[1] - self.rect.center[1]
    self.angle = math.degrees(math.atan2(y_difference, x_difference))
    self.image = pygame.transform.rotate(self.base_player_image, -self.angle)
    self.rect = self.image.get_rect(center = self.hitbox_rect.center)
    self.rect.center = self.hitbox_rect.center
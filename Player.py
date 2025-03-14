from Character import *
from settings import *
import pygame
import math
from Bullet import Bullet
from assets import *

class Player(Character):
  def __init__(self, new_pos):
    self.reset(new_pos)

  def reset(self, new_pos):
    super().__init__(new_pos)
    self.image_setup = pygame.image.load("assets/survivor_no_background.png").convert_alpha() # imports the image and converts for better performance
    self.image = pygame.transform.scale(self.image_setup, (60, 40)) # changing dimensions of image
    self.base_player_image = self.image
    self.rect = self.image.get_rect(topleft = self.pos) # creates player rectangle using the image dimensions
    self.hitbox_rect = player_hitbox # creates the hitbox rectangle to handle collisions
    self.hitbox_rect.center = self.rect.center
    self.disguise = False # stores the disguise currently worn by the player for guards to ignore them
    self.ammo = 30
    self.gun_held = (30, 2)
    self.keycard = True # stores if the player has a keycard
    self.vault_keycard = False # stores if the player has a vault keycard
    self.usb = False
    self.suspicious = False
    self.is_shooting = False
    self.shoot_cooldown = 10
    

  def update(self): # update method for player to run any methods that need to be run every frame
    self.get_input()
    self.hitbox_rect.centerx += self.x_direction # 
    self.player_x_collisions(collision_objects)
    self.hitbox_rect.centery += self.y_direction
    self.player_y_collisions(collision_objects)
    self.rotation()
    self.rect.center = self.hitbox_rect.center
    self.shoot(self.rect.centerx, self.rect.centery, self.get_angle())
    self.die()
  
  
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
    if pygame.mouse.get_pressed() == (1, 0, 0):
      self.is_shooting = True
    else:
      self.is_shooting = False

      
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

  def get_angle(self):
    mouse_pos = pygame.mouse.get_pos()
    x_difference = mouse_pos[0] - self.rect.center[0]
    y_difference = mouse_pos[1] - self.rect.center[1]
    self.angle = math.degrees(math.atan2(y_difference, x_difference))
    return self.angle

  
  def rotation(self):
    self.image = pygame.transform.rotate(self.base_player_image, -self.get_angle())
    self.rect = self.image.get_rect(center = self.hitbox_rect.center)
    self.rect.center = self.hitbox_rect.center

  def shoot(self, x, y, angle):
    if self.is_shooting == False:
      self.shoot_cooldown -= 1
      return
    else:
      if self.shoot_cooldown > 0:
        self.shoot_cooldown -= 1
        return
      else:
          self.shoot_cooldown = 10
          self.bullet = Bullet(30, self.get_angle(), self.rect.centerx, self.rect.centery, "player", self)
          bullet_sprites.add(self.bullet)
          

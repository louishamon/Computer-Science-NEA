import pygame
from Character import *
from Game import *
from settings import *

class Guard(Character):
  def __init__(self, new_pos, new_type, new_x_direction, new_y_direction):
    super().__init__(new_pos)
    self.held_item = None
    self.type = new_type
    self.combat = None
    self.image = pygame.Surface((50, 50))
    self.rect = self.image.get_rect(topleft = self.pos)
    self.image.fill("yellow")
    self.x_direction = new_x_direction
    self.y_direction = new_y_direction
    self.chase_track = False
  
  def movement(self): # movement method for guards, when moving, the rect position must follow so the coordinates of each guard can be tracked
    self.rect.x += self.x_direction
    self.rect.y += self.y_direction
    
  def patrol_x_collisions(self, wall_sprites): # controls x collisions for when the guard is patrolling, allowing guards to bounce off walls
    for i in wall_sprites:
      if i.rect.colliderect(self.rect):
        self.x_direction = -self.x_direction # inverts direction to bouce back the opposite direction

  def patrol_y_collisions(self, wall_sprites): # controls y collisions for when the guard is patrolling, allowing guards to bounce off walls
    for i in wall_sprites:
      if i.rect.colliderect(self.rect):
        self.y_direction = -self.y_direction
  
  def chase(self):
    pass

  def update(self): # update method for guards to run any methods that need to be run every frame
    self.movement()
    if self.chase_track:
      self.x_collisions(collision_objects)
      self.y_collisions(collision_objects)
    else:
      self.patrol_x_collisions(collision_objects)
      self.patrol_y_collisions(collision_objects)

  def shoot(self):
    pass

  def held_item_gen(self):
    pass

  def drop(self):
    pass
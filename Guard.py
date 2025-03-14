import pygame
import math
from Character import *
from Game import *
from settings import *
from Bullet import *
from Item import *
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
from random import randint


class Guard(Character):
  def __init__(self, new_pos, new_type, new_direction, new_disguise):
    super().__init__(new_pos)
    self.held_item = None
    self.type = new_type
    self.image = pygame.Surface((50, 50))
    self.rect = self.image.get_rect(topleft = self.pos)
    self.disguise = new_disguise
    if self.type == ("vault"):
      self.image.fill("black")
    elif self.disguise:
      self.image.fill("forest green")
    else:
      self.image.fill("yellow")
    self.direction = new_direction
    self.chase_track = False
    self.path = []
    self.path_rects_group = []
    self.previous_path_time = 0
    self.sight_bullet = None
    self.previous_shot = 0
    self.last_seen = None
    
  
  def movement(self): # movement method for guards, when moving, the rect position must follow so the coordinates of each guard can be tracked
    x_pos = self.pos[0] + self.direction[0]
    y_pos = self.pos[1] + self.direction[1]
    self.pos = (x_pos, y_pos)
    self.rect.center = self.pos

  def chase_movement(self): # movement method for guards when chasing the player
    player_pos = self.access_player_pos()
    if player_pos[0] > self.rect.centerx:
      self.direction = (guard_movement_speed, self.direction[1])
    elif player_pos[0] < self.rect.centerx:
      self.direction = (-guard_movement_speed, self.direction[1])
    if player_pos[1] > self.rect.centery:
      self.direction = (self.direction[0], guard_movement_speed)
    elif player_pos[1] < self.rect.centery:
      self.direction = (self.direction[0], -guard_movement_speed)

  def patrol_collisions(self, wall_sprites): # controls x collisions for when the guard is patrolling, allowing guards to bounce off walls
    for i in wall_sprites:
      if i.rect.colliderect(self.rect):
        if self.direction[0] < 0:
          self.rect.left = i.rect.right
          self.direction = (-self.direction[0], self.direction[1])
        elif self.direction[0] > 0:
          self.rect.right = i.rect.left
          self.direction = (-self.direction[0], self.direction[1])
        elif self.direction[1] < 0:
          self.rect.top = i.rect.bottom
          self.direction = (self.direction[0], -self.direction[1])
        elif self.direction[1] > 0:
          self.rect.bottom = i.rect.top
          self.direction = (self.direction[0], -self.direction[1])
  
  def chase_x_collisions(self, wall_sprites):
    for i in wall_sprites:
      if i.rect.colliderect(self.rect):
        if self.direction[0] > 0:
          self.direction = (0, self.direction[1])
          self.rect.right = i.rect.left
        else:
          self.rect.left = i.rect.right
    for i in player_sprites:
      if i.rect.colliderect(self.rect):
        if self.disguise:
          i.disguise = True
        self.hp = 0


  def chase_y_collisions(self, wall_sprites):
    for i in wall_sprites:
      if i.rect.colliderect(self.rect):
        if self.direction[1] < 0:
          self.direction = (self.direction[0], 0)
          self.rect.top = i.rect.bottom
        else:
          self.rect.bottom = i.rect.top
  

  def update(self): # update method for guards to run any methods that need to be run every frame
    self.movement()
    self.path_collisions()
    if not self.held_item:
      self.held_item_gen()
    if not self.path:
      self.previous_path_time = pygame.time.get_ticks()
      self.player_detection()
    else:
      pass

    self.near_path_target()

    if self.chase_track:
      self.chase_movement()
      self.path = []
    elif self.last_seen and not self.chase_track and not self.path:
      self.find_path(self.last_seen[0], self.last_seen[1])
    

    self.shoot()

    if self.chase_track:
      self.chase_y_collisions(collision_objects)
      self.chase_x_collisions(collision_objects)
    else:
      self.patrol_collisions(collision_objects)

    if self.hp <= 0:
      self.drop()
    self.die()


  def held_item_gen(self):
    num = randint(1, 3)
    if num == 1:
      self.held_item = "keycard"
    else:
      self.held_item = "empty"
    

  def drop(self):
    if self.held_item == "keycard":
      item = Item(self.rect.center)
      item_sprites.add(item)
      from main import new_game
      new_game.all_sprites.add(item)


  def path_rects(self):
    if self.path:
      for node in self.path:
        x = (node[0] * 70) + 35
        y = (node[1] * 70) + 35
        rect = pygame.Rect(x-3, y-3, 6, 6)
        self.path_rects_group.append(rect)

  def path_direction(self):
    if self.path_rects_group:
      if len(self.path_rects_group) > 1:
        start = pygame.Vector2(self.pos[0], self.pos[1])
        end = pygame.Vector2(self.path_rects_group[0].center)
        vector = end - start
        angle = math.degrees(math.atan2(-vector[1], vector[0]))
        angle = (angle +90) % 360
        x_direction = guard_movement_speed * math.sin(math.radians(angle))
        y_direction = guard_movement_speed * math.cos(math.radians(angle))
        self.direction = (x_direction, y_direction)
        self.direction = self.direction[0], self.direction[1]
      else:
        self.direction = pygame.Vector2(0, 0)
    else:
      self.direction = pygame.Vector2(0, 0)

  def path_collisions(self):
    temp_path = self.path
    if self.path_rects_group and self.path:
      for index, node in enumerate(self.path_rects_group):
        if index == len(self.path_rects_group) + 1:
          break
        if node.collidepoint(self.rect.center):
          del self.path_rects_group[0]
          del self.path[0]
          self.direction = pygame.Vector2(0, 0)
          self.player_detection()
          if temp_path == self.path:
            self.path_direction()
    else:
      self.path = []
      

  def find_path(self, end_x, end_y):
    ## code to find the path and return list containing coordinates of path
    self.path_rects_group = []
    grid = Grid(matrix = game_map, inverse=True)
    start = grid.node(self.rect.centerx // 70 ,self.rect.centery // 70)
    end = grid.node(end_x // 70, end_y // 70)
    finder = AStarFinder()
    route,_ = finder.find_path(start, end, grid)
    self.path = [(node.x, node.y) for node in route]
    self.path_rects()
    grid.cleanup()
    ## code to move guard along path
    if self.path:
      self.path_direction()
    else:
      self.direction = pygame.Vector2(0, 0)
      #self.path = []


  def access_player_pos(self):
    from main import new_game
    obj = new_game.get_player_pos()
    return obj
  

  def player_detection(self):
    player_pos = self.access_player_pos()
    x_difference = player_pos[0] - self.rect.centerx
    y_difference = player_pos[1] - self.rect.centery
    angle = math.degrees(math.atan2(y_difference, x_difference))
    bullet = Bullet(0, angle, self.rect.centerx, self.rect.centery, "sight", self)
    bullet_sprites.add(bullet)
      
    
  def shoot(self):
    if self.chase_track:
      if pygame.time.get_ticks() - self.previous_shot > 500:
        self.previous_shot = pygame.time.get_ticks()
        player_pos = self.access_player_pos()
        x_difference = player_pos[0] - self.rect.centerx
        y_difference = player_pos[1] - self.rect.centery
        angle = math.degrees(math.atan2(y_difference, x_difference))
        bullet = Bullet(25, angle, self.rect.centerx, self.rect.centery, "guard", self)
        bullet_sprites.add(bullet)


  def near_path_target(self):
    if self.path:
      x_difference = self.path[0][0] - self.rect.centerx
      y_difference = self.path[0][1] - self.rect.centery
      sum_of_squares = (x_difference ** 2) + (y_difference ** 2)
      distance = math.sqrt(sum_of_squares)
      if distance < 140:
        self.path = []
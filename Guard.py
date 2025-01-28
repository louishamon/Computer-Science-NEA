import pygame
import math
from Character import *
from Game import *
from settings import *
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

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
    self.rect.centerx += self.x_direction
    self.rect.centery += self.y_direction
    if self.chase_track:
      self.y_collisions(collision_objects)
      self.x_collisions(collision_objects)
    else:
      self.patrol_x_collisions(collision_objects)
      self.patrol_y_collisions(collision_objects)
    self.die()

  def shoot(self):
    pass

  def held_item_gen(self):
    pass

  def drop(self):
    pass
    

  def find_path(self, end_x, end_y):
    ## code to find the path and return list containing coordinates of path
    grid = Grid(matrix = game_map, inverse=True)
    start = grid.node(self.rect.centerx // 70 ,self.rect.centery // 70)
    end = grid.node(end_x // 70, end_y // 70)
    finder = AStarFinder()
    route,_ = finder.find_path(start, end, grid)
    path = [(node.x, node.y) for node in route]
    print(path)
    grid.cleanup()
    ## code to move guard along path
    for node in path:
      print(f"starting coords {self.rect.centerx, self.rect.centery}")
      x_coord = node[0] * 70 + 35
      y_coord = node[1] * 70 + 35

      print(f"x, y coords {x_coord, y_coord}")
      print(f"angle should be 0 {math.degrees(math.atan2(-5, -5))}")

      x_difference = x_coord - self.rect.center[0]
      y_difference = y_coord - self.rect.center[1]
      print(f"x difference {x_difference} y difference {y_difference}")
      angle = math.degrees(math.atan2(y_difference, x_difference))
      
      print(f"angle {angle}")

      self.x_direction = guard_movement_speed * math.cos(math.radians(angle))
      self.y_direction = guard_movement_speed * math.sin(math.radians(angle))
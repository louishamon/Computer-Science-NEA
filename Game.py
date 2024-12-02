import pygame
from Character import *
from settings import *
from Player import *
from Barriers import *
from Guard import *
from splash_screen import *

class Game:
  def __init__(self, screen_width, screen_height, new_object_sprites):
    self.size = (screen_width, screen_height)
    self.screen = pygame.display.set_mode(self.size)
    self.is_running = True
    self.alarm = False
    self.all_sprites = pygame.sprite.Group()
    self.player_sprites = pygame.sprite.Group()
    self.guard_sprites = pygame.sprite.Group()
    self.object_sprites = new_object_sprites
  
  
  def play(self, screen, game_map):
    pygame.init()
    self.create_object()
    clock = pygame.time.Clock()
    run = True
    splash_page = Splash(2000, self)
    splash_page.run()
    self.draw_map(game_map, self.object_sprites)
    while run:
      screen.fill("white")
      self.all_sprites.draw(screen)
      pygame.display.update()
      clock.tick(60)
      self.player.update()
      self.guard.update()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          quit()

  def quit(self, screen):
    pygame.display.quit()
    pygame.quit()

  def create_object(self):
    self.player = Player((110,110))
    self.all_sprites.add(self.player)
    self.player_sprites.add(self.player)

    self.guard = Guard((640,320), "guard", 0, guard_movement_speed)
    self.all_sprites.add(self.guard)
    self.guard_sprites.add(self.guard)
    
  def draw_map(self, game_map, collision_objects):
    for row_index, row in enumerate(game_map):
      for col_index, col in enumerate(row):
        if col == "X":
          base_wall = Base_wall((block_width, block_height), (col_index * block_width, row_index * block_height))
          collision_objects.add(base_wall)
          self.all_sprites.add(base_wall)
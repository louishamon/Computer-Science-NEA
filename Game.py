import pygame
from Character import *
from settings import *
from Player import *
from Barriers import *
from Guard import *
from splash_screen import *
from Bullet import *
from Object import *

class Game:
  def __init__(self, screen_width, screen_height, new_collision_sprites, new_bullet_sprites, new_guard_sprites, new_player_sprites, new_object_sprites):
    self.size = (screen_width, screen_height)
    self.screen = pygame.display.set_mode(self.size)
    self.is_running = True
    self.alarm = False
    self.all_sprites = pygame.sprite.Group()
    self.player_sprites = new_player_sprites
    self.guard_sprites = new_guard_sprites
    self.collision_sprites = new_collision_sprites
    self.bullet_sprites = new_bullet_sprites
    self.object_sprites = new_object_sprites
  
  
  def play(self, screen, game_map): # sets up the game including the drawing of objects, splash screen and mainly the game loop
    pygame.init()
    self.create_object()
    clock = pygame.time.Clock()
    run = True
    splash_page = Splash(1000, self) # instantiates an object from splash page with a timer
    splash_page.run() # plays the splash page
    self.draw_map(game_map, self.collision_sprites)
    while run:
      screen.fill("white") # blanks the whole screen before all objects are drawn again in the updated form
      self.all_sprites.add(*bullet_sprites)
      self.all_sprites.draw(screen)
      #pygame.draw.rect(self.screen, "black", self.player, 2)
      #pygame.draw.rect(self.screen, "yellow", self.player.hitbox_rect, 2)
      pygame.display.update()
      clock.tick(60)
      self.player.update()
      self.guard.update()
      self.guard2.update()
      self.bullet_sprites.update()
      self.object_sprites.update()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          quit()

  def quit(self, screen): # allows game to be exited using the X button in the top right
    pygame.display.quit()
    pygame.quit()

  def create_object(self): # method to contain instantiation of player and guard sprites
    self.player = Player((110,110))
    self.all_sprites.add(self.player)
    self.player_sprites.add(self.player)

    self.guard = Guard((640,320), "guard", 0, guard_movement_speed)
    self.all_sprites.add(self.guard)
    self.guard_sprites.add(self.guard)
    self.guard2 = Guard((840,220), "guard", guard_movement_speed, 0)
    self.all_sprites.add(self.guard2)
    self.guard_sprites.add(self.guard2)
    
    self.object = Object((70, 560))
    self.all_sprites.add(self.object)
    self.object_sprites.add(self.object)
    
    
  def draw_map(self, game_map, collision_objects): # method to use the list containing the location of basewall objects to draw to the screen
    for row_index, row in enumerate(game_map):
      for col_index, col in enumerate(row):
        if col == 1:
          base_wall = Base_wall((block_width, block_height), (col_index * block_width, row_index * block_height))
          collision_objects.add(base_wall)
          self.all_sprites.add(base_wall)

  def get_guard_pos(self):
    return (self.guard.rect.centerx, self.guard.rect.centery)
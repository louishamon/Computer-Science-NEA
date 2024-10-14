import pygame
from settings import *

class Game:
  def __init__(self, screen_width, screen_height):
    self.size = (screen_width, screen_height)
    self.screen = pygame.display.set_mode(self.size)
    self.is_running = True
    self.alarm = False
    self.all_sprites = pygame.sprite.Group()
    self.player_sprites = pygame.sprite.Group()
    self.enemy_sprites = pygame.sprite.Group()
    self.wall_sprites = pygame.sprite.Group()
    self.object_sprites = pygame.sprite.Group()
  
  
  def play(self, screen):
    pygame.init()
    clock = pygame.time.Clock()
    run = True
    while run:
      screen.fill("white")
      self.all_sprites.draw(screen)
      pygame.display.update()
      clock.tick(60)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          quit()

  def quit(self, screen):
    pygame.display.quit()
    pygame.quit()
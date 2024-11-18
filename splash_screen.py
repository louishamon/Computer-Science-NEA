import pygame
from Game import *
from main import *

class Splash():
  def __init__(self, new_display_time):
    self.image = pygame.image.load("splash_page.webp").convert()
    self.display_time = new_display_time
    self.screen = new_game.screen
    self.clock = pygame.time.Clock()

  def run(self):
    run = True
    start_time = pygame.time.get_ticks()
    while run:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
      time = pygame.time.get_ticks() - start_time
      self.screen.blit(self.image, (0, 0))
      pygame.display.flip()
      self.clock.tick(60)
      if time >= self.display_time:
        run = False
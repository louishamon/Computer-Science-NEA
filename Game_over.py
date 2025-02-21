import pygame
from Game import *
from Button import *

class Game_over():
    def __init__(self, new_game):
        self.image = pygame.image.load("game over screen silent robbery.jpg").convert()
        self.screen = new_game.screen
        self.clock = pygame.time.Clock()

    def run(self):
        run = True
        restart = Button(705, 755, "restart button silent robbery.jpg")
        restart.draw()
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.screen.blit(self.image, (0, 0))
            if restart.click_check():
                pass
            pygame.display.flip()
            self.clock.tick(60)
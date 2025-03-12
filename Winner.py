import pygame
from Game import *
from Button import *

class Winner():
    def __init__(self, new_game):
        self.image = pygame.image.load("assets/you win screen.jpg").convert()
        self.screen = new_game.screen
        self.clock = pygame.time.Clock()

    def run(self):
        run = True
        self.screen.blit(self.image, (0, 0))
        restart = Button(773, 712, "assets/play again button.jpg")
        restart.draw()
        quit = Button(850, 838, "assets/quit button.jpg")
        quit.draw()
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if restart.click_check():
                run = False
            if quit.click_check():
                return True
            pygame.display.flip()
            self.clock.tick(60)
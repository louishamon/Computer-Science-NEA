from Game import Game
from Character import Character
from settings import *
import pygame

pygame.init()
new_game = Game(screen_width, screen_height, collision_objects, bullet_sprites) # instantiating game passing in settings and the collision_objects sprite group
pygame.display.set_caption("Silent Robbery") # setting the window caption
new_game.play(new_game.screen, game_map) # running the play method from game to start the game loop


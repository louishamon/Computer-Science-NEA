from Game import Game
from Character import Character
from settings import *
import pygame

pygame.init()
new_game = Game(screen_width, screen_height, collision_objects)
new_game.play(new_game.screen, game_map)


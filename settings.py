import pygame

screen_width = 1792
screen_height = 1024
screen = pygame.display.set_mode((screen_width, screen_height))

block_width = 70
block_height = 70

guard_movement_speed = 2

player_hitbox = pygame.Rect(0, 0, 70, 70)

game_map = [
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "", "", "", "", "X", "", "", "", "", "", "", "", "", "", "", "", "", "", "X"],
    ["X", "", "", "", "", "X", "", "", "X", "X", "X", "", "", "", "", "", "", "", "X"],
    ["X", "", "", "", "", "X", "", "", "", "", "X", "", "", "", "", "X", "", "", "", "X"],
    ["X", "", "", "", "", "X", "", "", "", "", "X", "X", "X", "X", "X", "X", "", "", ""],
    ["X", "X", "X", "", "", "", "", "", "", "", "X", "", "", "", "", "X", "", "", "X", "X", "X"],
    ["X", "", "", "", "", "", "", "", "", "", "X", "", "", "", "", "", "", "", "X"],
    ["X", "", "", "", "", "", "X", "X", "X", "X", "X", "X", "", "", "", "", "X", "X", "", "X"],
    ["X", "", "", "", "X", "X", "X", "", "", "", "", "", "X", "", "", "", "", "X", "", "X"],
    ["X", "", "", "X", "", "", "", "", "", "", "X", "", "X", "", "", "X", "", "", "X"],
    ["X", "X", "X", "", "", "X", "X", "", "", "X", "", "", "X", "", "", "", "", "", "X"],
    ["X", "", "X", "", "", "X", "", "X", "", "X", "X", "", "X", "", "", "X", "", "", "X"],
    ["X", "", "X", "X", "X", "", "X", "", "", "", "X", "X", "", "", "X", "", "", "X", "X"],
    ["X", "", "", "", "", "X", "", "", "", "X", "", "", "X", "", "", "", "", "X", "X"],
    ["X", "", "X", "X", "X", "X", "X", "", "X", "X", "X", "X", "", "X", "X", "X", "X", "X", "X"],
    ["X", "", "", "", "", "", "X", "", "", "X", "", "", "X", "", "", "X", "", "X", "X"],
    ["X", "X", "X", "", "", "X", "", "X", "", "", "", "", "X", "X", "X", "X", "X", "X", "X", "X"]
]

collision_objects = pygame.sprite.Group()
import pygame
from Character import *
from settings import *
from Player import *
from Barriers import *
from Guard import *
from splash_screen import *
from Bullet import *
from Object import *
from Game_over import *
from Button import *
from Vault import *
from Winner import *

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

        while run:
            screen.fill("white") # blanks the whole screen before all objects are drawn again in the updated form  
            self.bullet_sprites.draw(screen)
            self.all_sprites.draw(screen)
            #pygame.draw.rect(self.screen, "black", self.player, 2)
            #pygame.draw.rect(self.screen, "yellow", self.player.hitbox_rect, 2)
            pygame.display.update()
            self.bullet_sprites.update()
            self.all_sprites.update()
            if self.player.hp < 1:
                for sprite in self.all_sprites:
                    sprite.kill()
                self.game_over()
                self.create_object()
            if self.vault.winner:
                for sprite in self.all_sprites:
                    sprite.kill()
                if self.winner():
                    quit()
                self.create_object()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            clock.tick(60)


    def winner(self):
        screen.fill("white")
        winner = Winner(self)
        if winner.run():
            return True


    def game_over(self):
        screen.fill("white")
        game_over = Game_over(self)
        game_over.run()

    
    def quit(self, screen): # allows game to be exited using the X button in the top right
        pygame.display.quit()
        pygame.quit()


    def create_object(self): # method to contain instantiation of player and guard sprites
        self.draw_map(game_map, self.collision_sprites)

        self.player = Player((110,110))
        self.all_sprites.add(self.player)
        self.player_sprites.add(self.player)

        self.guard = Guard((650,250), "guard", (0, guard_movement_speed), False)
        self.all_sprites.add(self.guard)
        self.guard_sprites.add(self.guard)
        self.guard2 = Guard((840,240), "guard", (guard_movement_speed, 0), True)
        self.all_sprites.add(self.guard2)
        self.guard_sprites.add(self.guard2)
        self.guard3 = Guard((100, 500), "guard", (0, guard_movement_speed), False)
        self.all_sprites.add(self.guard3)
        self.guard_sprites.add(self.guard3)
        self.guard4 = Guard((1600, 180), "guard", (guard_movement_speed, 0), False)
        self.all_sprites.add(self.guard4)
        self.guard_sprites.add(self.guard4)
        self.guard5 = Guard((1700, 800), "guard", (0, guard_movement_speed), False)
        self.all_sprites.add(self.guard5)
        self.guard_sprites.add(self.guard5)
        self.guard6 = Guard((1550, 940), "guard", (guard_movement_speed, 0), False)
        self.all_sprites.add(self.guard6)
        self.guard_sprites.add(self.guard6)
        self.guard7 = Guard((945, 650), "guard", (0, guard_movement_speed), False)
        self.all_sprites.add(self.guard7)
        self.guard_sprites.add(self.guard7)
        self.guard8 = Guard((600, 585), "vault", (guard_movement_speed, 0), False)
        self.all_sprites.add(self.guard8)
        self.guard_sprites.add(self.guard8)
        self.guard9 = Guard((600, 955), "vault", (guard_movement_speed, 0), False)
        self.all_sprites.add(self.guard9)
        self.guard_sprites.add(self.guard9)

        self.object = Object((240, 70), self.guard)
        self.all_sprites.add(self.object)
        self.object_sprites.add(self.object)
        self.object2 = Object((770, 350), self.guard8)
        self.all_sprites.add(self.object2)
        self.object_sprites.add(self.object2)

        self.vault = Vault((70, 840))
        self.all_sprites.add(self.vault)

    def draw_map(self, game_map, collision_objects): # method to use the list containing the location of basewall objects to draw to the screen
        for row_index, row in enumerate(game_map):
            for col_index, col in enumerate(row):
                if col == 1:
                    base_wall = Base_wall((block_width, block_height), (col_index * block_width, row_index * block_height))
                    collision_objects.add(base_wall)
                    self.all_sprites.add(base_wall)

    def get_guard_pos(self):
        return (self.guard.rect.centerx, self.guard.rect.centery)
    
    def get_player_pos(self):
        return (self.player.rect.centerx, self.player.rect.centery)

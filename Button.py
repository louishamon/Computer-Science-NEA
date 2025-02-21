import pygame

class Button:
    def __init__(self, x, y, new_image):
        self.image = pygame.image.load(new_image).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    
    def get_screen(self):
        from main import new_game
        obj = new_game.screen
        return obj

    def draw(self):
        screen = self.get_screen()
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def click_check(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed() == (1, 0, 0) and not self.clicked:
                self.clicked = True
                return True
                
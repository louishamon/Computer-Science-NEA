from settings import *

class Base_wall(pygame.sprite.Sprite):
    def __init__(self, size, pos):
        super().__init__()
        self.image = pygame.Surface((size[0] , size[1]))
        self.image.fill("blue")
        self.rect = self.image.get_rect(topleft = pos)
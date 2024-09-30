class Character(pygame.sprite.Sprite):
  def __init__(self, size, pos):
    super().__init__()
    self.movement_speed = 4
    self.current_weapon = None
    self.hp = 100
    self.image = self.image = pygame.Surface((size[0], size[1]))
    self.rect = self.image.get_rect(topleft = pos)
    self.x_direction = 0
    self.y_direction = 0
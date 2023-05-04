import pygame

class Chest(pygame.sprite.Sprite):
  def __init__(self, scale, screen, pos):
    pygame.sprite.Sprite.__init__(self)
    self.animation_list = []
    self.scale = scale
    self.screen = screen
    self.frame_index = 0
    for i in range(4):
      temp = pygame.image.load(f'./sprites/chest/chest_{i}.png').convert_alpha()
      self.animation_list.append(pygame.transform.scale(temp, (temp.get_width()*self.scale, temp.get_height()*self.scale)))
    self.img = self.animation_list[self.frame_index]
    self.rect = self.img.get_rect()
    self.image = self.img
    self.rect.x = pos.x
    self.rect.y = pos.y
      
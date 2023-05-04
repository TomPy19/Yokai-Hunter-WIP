import pygame
from bin.Character import Character

class Boss(Character):
  def __init__(self, scale, screen, speed, health, x, y):
    super().__init__(scale, screen)
    self.boss = True
    self.scale = scale
    self.screen = screen
    self.speed = speed
    self.health = health
    self.max_health = health
    self.image = pygame.image.load(f'./sprites/bird/bird.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (self.image.get_width()*2*self.scale, self.image.get_height()*2*self.scale))
    self.rect = self.image.get_rect()
    self.hp_bar = pygame.rect.Rect(10, screen.get_height() - (screen.get_height() / 40 + 10), screen.get_width() - 20, screen.get_height() / 40)
    self.max_bar = self.hp_bar.width
    self.rect.x = x
    self.rect.y = y
    self.pos = pygame.Vector2(x, y)

  def chase_player(self, player):
      if self.rect.center[1] > player.rect.center[1]:
        self.rect.y -= self.speed
      if self.rect.center[1] < player.rect.center[1]:
        self.rect.y += self.speed
      if self.rect.center[0] < player.rect.center[0]:
        self.rect.x += self.speed
        if self.dir == 0:
          self.dir = 4
      if self.rect.center[0] > player.rect.center[0]:
        self.rect.x -= self.speed
        if self.dir == 4:
          self.dir = 0

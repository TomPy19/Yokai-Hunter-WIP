import pygame

class Talisman(pygame.sprite.Sprite):
	def __init__(self, scale, screen, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.scale = scale
		self.screen = screen
		self.image = pygame.image.load(f'./sprites/items/talisman.png').convert_alpha()
		self.image = pygame.transform.scale(self.image, (self.image.get_width()*self.scale, self.image.get_height()*self.scale))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
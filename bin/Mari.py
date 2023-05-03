import pygame
from bin.Character import Character

class Mari(Character):
	def __init__(self, scale, screen):
		super().__init__(scale, screen)
		for i in range(4):
			temp = pygame.image.load(f'./sprites/mari/mari_step_{i}.png').convert_alpha()
			self.animation_list.append(pygame.transform.scale(temp, (temp.get_width()*self.scale, temp.get_height()*self.scale)))
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()
		self.img = self.animation_list[self.frame_index]
		self.speed = scale*1.5
		self.rect = self.img.get_rect()
		self.pos = pygame.Vector2((self.screen.get_width() / 2) - (self.rect.width / 2), (self.screen.get_height() / 2) - (self.rect.height / 2))
		self.rect.x = self.pos.x
		self.rect.y = self.pos.y
		self.looking = 0

	def draw(self):
		self.img = pygame.transform.flip(self.img, self.looking, False)
		self.screen.blit(self.img, (self.rect.x, self.rect.y))
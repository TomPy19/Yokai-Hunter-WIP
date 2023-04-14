import pygame
from bin.Character import Character

class Mari(Character):
	def __init__(self, scale, screen):
		super().__init__(scale, screen)
		temp_list = []
		for i in range(4):
			temp = pygame.image.load(f'./sprites/mari/mari_step_{i}.png').convert_alpha()
			temp_list.append(pygame.transform.scale(temp, (temp.get_width()*self.scale, temp.get_height()*self.scale)))
		self.animation_list.append(temp_list)
		temp_list = []
		for i in range(4):
			temp = pygame.image.load(f'./sprites/mari/mari_side_{i}.png').convert_alpha()
			temp_list.append(pygame.transform.scale(temp, (temp.get_width()*self.scale, temp.get_height()*self.scale)))
		self.animation_list.append(temp_list)
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()
		self.img = self.animation_list[self.action][self.frame_index]
		self.pos = pygame.Vector2((self.screen.get_width() / 2) - (self.img.get_width() / 2), (self.screen.get_height() / 2) - (self.img.get_height() / 2))
		self.speed = scale*1.5
		self.rect = self.img.get_rect()
		self.rect.x = self.pos.x
		self.rect.y = self.pos.y
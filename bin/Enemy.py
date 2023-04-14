import pygame
from bin.Character import Character

class Enemy(Character):
	def __init__(self, scale, enemy, pos, screen):
		super().__init__(scale, screen)
		temp_list = []
		self.enemy = enemy
		for i in range(2):
			temp = pygame.image.load(f'./sprites/{self.enemy}/{self.enemy}_move_{i}.png').convert_alpha()
			temp_list.append(pygame.transform.scale(temp, (temp.get_width()*self.scale, temp.get_height()*self.scale)))
		self.animation_list.append(temp_list)
		self.frame_index = 0
		self.action = 0
		self.update_time = pygame.time.get_ticks()
		self.img = self.animation_list[self.action][self.frame_index]
		self.rect = self.img.get_rect()
		self.rect.x = pos.x
		self.rect.y = pos.y
		self.speed = scale*.75
		self.image = self.img
		self.alive = True

	def chase_player(self, player):
		if self.rect.y > player.pos.y:
			self.rect.y -= self.speed
		if self.rect.y < player.pos.y:
			self.rect.y += self.speed
		if self.rect.x < player.pos.x:
			self.rect.x += self.speed
			if self.dirx == 1:
				self.img = pygame.transform.flip(self.img, True, False)
				self.dir = 0
		if self.rect.x > player.pos.x:
			self.rect.x -= self.speed
			if self.dirx == -1:
				self.img = pygame.transform.flip(self.img, True, False)
				self.dir = 1

	def check_alive(self):
		if not self.alive:
			self.kill()
		return False
import pygame
from bin.Character import Character

class Enemy(Character):
	def __init__(self, scale, enemy, pos, screen, speed, health, ani_cd):
		super().__init__(scale, screen)
		self.enemy = enemy
		for i in range(4):
			temp = pygame.image.load(f'./sprites/{self.enemy}/{self.enemy}_{i}.png').convert_alpha()
			self.animation_list.append(pygame.transform.scale(temp, (temp.get_width()*self.scale, temp.get_height()*self.scale)))
		self.update_time = pygame.time.get_ticks()
		self.img = self.animation_list[self.frame_index]
		self.rect = self.img.get_rect()
		self.rect.x = pos.x
		self.rect.y = pos.y
		self.speed = scale*speed
		self.health = health
		self.alive = True
		self.ani_cd = ani_cd

	def chase_player(self, player):
		if self.rect.y > player.pos.y:
			self.rect.y -= self.speed
		if self.rect.y < player.pos.y:
			self.rect.y += self.speed
		if self.rect.x < player.pos.x:
			self.rect.x += self.speed
			if self.dir == 0:
				self.dir = 4
		if self.rect.x > player.pos.x:
			self.rect.x -= self.speed
			if self.dir == 4:
				self.dir = 0

	def check_alive(self):
		if not self.health <= 0:
			self.kill()
		return False
	
	def draw(self):
		if self.dir == 3 or self.dir == 4 or self.dir == 5:
			self.img = pygame.transform.flip(self.img, True, False)
		self.screen.blit(self.img, (self.rect.x, self.rect.y))

	def animate_move(self, cd):
		if pygame.time.get_ticks() - self.update_time > cd:
			self.update_time = pygame.time.get_ticks()
			self.frame_index += 1
		if self.frame_index >= len(self.animation_list):
			self.frame_index = 0
		self.img = self.animation_list[self.frame_index]
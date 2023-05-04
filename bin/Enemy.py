import pygame, math
from bin.Character import Character

class Enemy(Character):
	def __init__(self, scale, enemy, pos, screen, speed, health, ani_cd):
		super().__init__(scale, screen)
		self.boss = False
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
		self.ani_cd = ani_cd

	def find_further(self, enemy, player):
		ed = math.sqrt(pow((enemy.rect.centerx - player.rect.centerx), 2) + pow((enemy.rect.centery - player.rect.centery), 2))
		sd = math.sqrt(pow((self.rect.centerx - player.rect.centerx), 2) + pow((self.rect.centery - player.rect.centery), 2))
		if ed > sd:
			return enemy
		else:
			return self

	def chase_player(self, player, group):
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
		touching = pygame.sprite.spritecollide(self, group, False)
		if touching:
			for enemy in touching:
				enemy = self.find_further(enemy, player)
				if enemy.rect.center[1] > player.rect.center[1]:
					enemy.rect.y += enemy.speed
				if enemy.rect.center[1] < player.rect.center[1]:
					enemy.rect.y -= enemy.speed
				if enemy.rect.center[0] < player.rect.center[0]:
					enemy.rect.x -= enemy.speed
					if enemy.dir == 0:
						enemy.dir = 4
				if enemy.rect.center[0] > player.rect.center[0]:
					enemy.rect.x += enemy.speed
					if enemy.dir == 4:
						enemy.dir = 0
	
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
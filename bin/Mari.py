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
		self.last_damaged = pygame.time.get_ticks()
		self.img = self.animation_list[self.frame_index]
		self.speed = scale*1.5
		self.rect = self.img.get_rect()
		self.pos = pygame.Vector2((self.screen.get_width() / 2) - (self.rect.width / 2), (self.screen.get_height() / 2) - (self.rect.height / 2))
		self.rect.x = self.pos.x
		self.rect.y = self.pos.y
		self.looking = 0
		self.health = 25
		self.max_health = 25
		self.killed = 0
		self.hp_bar = pygame.rect.Rect(self.rect.left-15, self.rect.top-(self.rect.height/6 + 2), self.rect.width+30, self.rect.height/6)
		self.max_bar = self.hp_bar.width
		self.bar_outline = pygame.rect.Rect(self.rect.left-16, self.rect.top-(self.rect.height/6 + 3), self.rect.width+32, self.rect.height/6+2)

	def draw(self):
		self.img = pygame.transform.flip(self.img, self.looking, False)
		pygame.draw.rect(self.screen, pygame.Color('black'), self.bar_outline)
		pygame.draw.rect(self.screen, pygame.Color('red'), self.hp_bar)
		self.screen.blit(self.img, (self.rect.x, self.rect.y))

	def check_collision(self, enemy_group, item_group):
		enemies = pygame.sprite.spritecollide(self, enemy_group, False)
		if enemies:
			for enemy in enemies:
				if pygame.time.get_ticks() - self.last_damaged > 500:
					if self.health > 0:
						if enemy.boss:
							self.health -= 5
						else: self.health -= 1
						self.last_damaged = pygame.time.get_ticks()
						p = (self.health / self.max_health)
						self.hp_bar.width = self.max_bar * p
					else:
						return True
				if enemy.rect.y > self.pos.y:
					enemy.rect.y += enemy.speed
				if enemy.rect.y < self.pos.y:
					enemy.rect.y -= enemy.speed
				if enemy.rect.x < self.pos.x:
					enemy.rect.x -= enemy.speed
					if enemy.dir == 0:
						enemy.dir = 4
				if enemy.rect.x > self.pos.x:
					enemy.rect.x += enemy.speed
					if enemy.dir == 4:
						enemy.dir = 0

		items = pygame.sprite.spritecollide(self, item_group, False)
		if items:
			self.health += 5
			if self.health > self.max_health:
				self.health = self.max_health
			p = (self.health / self.max_health)
			self.hp_bar.width = self.max_bar * p
			items[0].kill()
		
		return False

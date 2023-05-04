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
		self.health = 30
		self.max_health = 30
		self.hp_bar = pygame.rect.Rect(self.rect.left-15, self.rect.top-(self.rect.height/6 + 2), self.rect.width+30, self.rect.height/6)

	def draw(self):
		self.img = pygame.transform.flip(self.img, self.looking, False)
		pygame.draw.rect(self.screen, pygame.Color('red'), self.hp_bar)
		self.screen.blit(self.img, (self.rect.x, self.rect.y))

	def check_collision(self, group):
		if pygame.time.get_ticks() - self.last_damaged > 500:
			enemies = pygame.sprite.spritecollide(self, group, False)
			if enemies:
				for enemy in enemies:
					self.health -= 1
					self.hp_bar.width *= (self.health / self.max_health)
				self.last_damaged = pygame.time.get_ticks()
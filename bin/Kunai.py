import pygame, math

class Kunai(pygame.sprite.Sprite):
	def __init__(self, player, scale, screen):
		pygame.sprite.Sprite.__init__(self)
		self.screen = screen
		self.scale = scale
		self.fixed_speed = 4*self.scale
		self.current_speed = self.fixed_speed
		self.cd = 1000
		self.img = pygame.image.load(f'./sprites/knife/kunai.png').convert_alpha()
		self.img = pygame.transform.scale(self.img, (self.img.get_width()*scale*2/3, self.img.get_height()*scale*2/3))
		self.dirx = 0
		self.diry = 0
		self.dir = player.dir
		self.pos = pygame.Vector2(0,0)
		self.orient(player)
		self.update_time = pygame.time.get_ticks()
		self.rect = self.img.get_rect()
		self.rect.x = self.pos.x
		self.rect.y = self.pos.y
		self.image = self.img

	def orient(self, player):
		if self.dir == 0:
			self.dirx = 1
			self.diry = 0
			self.img = pygame.transform.rotate(self.img, -45)
			self.pos = pygame.Vector2((self.screen.get_width() / 2) + (player.img.get_width() / 2), 
			     (self.screen.get_height() / 2) - (self.img.get_height() / 2))
		if self.dir == 1:
			self.dirx = 1
			self.diry = -1
			self.img = self.img
			self.pos = pygame.Vector2((self.screen.get_width() / 2) + (player.img.get_width() / 2), 
			     (self.screen.get_height() / 2) - (self.img.get_height()) - (player.img.get_height() / 2))
		if self.dir == 2:
			self.dirx = 0
			self.diry = -1
			self.img = pygame.transform.rotate(self.img, 45)
			self.pos = pygame.Vector2((self.screen.get_width() / 2) - (self.img.get_width() / 2), 
			     (self.screen.get_height() / 2) - (self.img.get_height()) - (player.img.get_height() / 2))
		if self.dir == 3:
			self.dirx = -1
			self.diry = -1
			self.img = pygame.transform.rotate(self.img, 90)
			self.pos = pygame.Vector2((self.screen.get_width() / 2) - (player.img.get_width() / 2) - self.img.get_width(), 
			(self.screen.get_height() / 2) - (self.img.get_height()) - (player.img.get_height() / 2))
		if self.dir == 4:
			self.dirx = -1
			self.diry = 0
			self.img = pygame.transform.rotate(self.img, 135)
			self.pos = pygame.Vector2((self.screen.get_width() / 2) - (player.img.get_width() / 2) - self.img.get_width(), 
			(self.screen.get_height() / 2) - (self.img.get_height() / 2))
		if self.dir == 5:
			self.dirx = -1
			self.diry = 1
			self.img = pygame.transform.rotate(self.img, 180)
			self.pos = pygame.Vector2((self.screen.get_width() / 2) - (player.img.get_width() / 2) - self.img.get_width(), 
			(self.screen.get_height() / 2) + (player.img.get_height() / 2))
		if self.dir == 6:
			self.dirx = 0
			self.diry = 1
			self.img = pygame.transform.rotate(self.img, -135)
			self.pos = pygame.Vector2((self.screen.get_width() / 2) - (self.img.get_width() / 2), 
			(self.screen.get_height() / 2) + (player.img.get_height() / 2))
		if self.dir == 7:
			self.dirx = 1
			self.diry = 1
			self.img = pygame.transform.rotate(self.img, -90)
			self.pos = pygame.Vector2((self.screen.get_width() / 2) + (player.img.get_width() / 2), 
			(self.screen.get_height() / 2) + (player.img.get_height() / 2))

	def update(self, group):
		# print(self.dir)
		if self.dir == 1 or self.dir == 3 or self.dir == 5 or self.dir == 7:
			self.current_speed = self.fixed_speed * self.fixed_speed / math.sqrt(pow(self.fixed_speed, 2)*2)
		else:
			self.current_speed = self.fixed_speed
		# print(self.current_speed)
		self.detect_collision(group)
		if self.rect.right < self.screen.get_width()/2 + 360*self.scale and self.rect.left > self.screen.get_width()/2 - 360*self.scale and self.rect.top < self.screen.get_height()/2 + 360*self.scale and self.rect.bottom > self.screen.get_height()/2 - 360*self.scale:
			self.rect.x += (self.dirx * self.current_speed)
			self.rect.y += (self.diry * self.current_speed)
		else:
			self.kill()

	def draw(self):
		self.screen.blit(self.img, self.pos)

	def detect_collision(self, group):
		enemies = pygame.sprite.spritecollide(self, group, False)
		if pygame.sprite.spritecollide(self, group, False):
			group.remove(enemies[0])
			self.kill()
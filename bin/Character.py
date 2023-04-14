import pygame

class Character(pygame.sprite.Sprite):
	def __init__(self, scale, screen):
		pygame.sprite.Sprite.__init__(self)
		self.screen = screen
		self.dirx = 0
		self.diry = 0
		self.dir = 0
		self.action = 0
		self.animation_list = []
		self.frame_index = 0
		self.scale = scale
		self.is_moving = False
		self.moving = [False, False, False, False]

	def draw(self):
		if self.dir == 3 or self.dir == 4 or self.dir == 5:
			if self.dir == 4 and self.moving[2] == False:
				self.img = pygame.transform.flip(self.img, True, False)
			self.img = pygame.transform.flip(self.img, True, False)
		self.screen.blit(self.img, (self.rect.x, self.rect.y))

	def check_moving(self):
		for i in range(len(self.moving)):
			if self.moving[i] == True:
				if self.moving[0] or self.moving[2]:
					self.action = 1
				else:
					self.action = 0
				return True
		self.frame_index = 0
		self.action = 0
		self.update_time = pygame.time.get_ticks()
		self.img = self.animation_list[self.action][self.frame_index]
		return False
			
	def update_action(self):
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()
		self.img = self.animation_list[self.action][self.frame_index]

	def animate_move(self, cd):
		if pygame.time.get_ticks() - self.update_time > cd:
			self.update_time = pygame.time.get_ticks()
			self.frame_index += 1
		if self.frame_index >= len(self.animation_list[self.action]):
			self.frame_index = 0
		self.img = self.animation_list[self.action][self.frame_index]
			
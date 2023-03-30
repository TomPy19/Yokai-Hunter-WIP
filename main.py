import pygame, sys, os, csv

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
rectWidth, rectHeight = 100, 100

pygame.init()

scale = 2
screen = pygame.display.set_mode(SCREEN_SIZE)
# screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
pygame.display.set_caption("Yokai Hunter")

# enemy = pygame.image.load("./sprites/lamp/chuuchin_obake_1.png")
# enemy = pygame.transform.scale(enemy, (enemy.get_width()*scale, enemy.get_height()*scale))

background = pygame.image.load("./map.png").convert()
background = pygame.transform.scale(background, (background.get_width()*2*scale, background.get_height()*2*scale))

clock = pygame.time.Clock()
speed = 0

enemy_pos = pygame.Vector2(0, 0)
map_pos = pygame.Vector2((background.get_width() - screen.get_width()) / -2, (background.get_height() - screen.get_height()) / -2)

dir = 0
enemy_dir = 0
frame_index = 0
action = 0

class Character(pygame.sprite.Sprite):
	def __init__(self, scale):
		pygame.sprite.Sprite.__init__(self)
		self.dir = 0
		self.action = 0
		self.animation_list = []
		self.frame_index = 0
		self.scale = scale
		
	def update_action(self, new_action):
		if new_action is not self.action:
			self.action = new_action
			self.frame_index = 0
			self.update_time = pygame.time.get_ticks()
			self.img = self.animation_list[self.frame_index]
			if player.dir:
				player.img = pygame.transform.flip(player.img, True, False)

	def animate_move(self, cd):
		if self.action:
			self.img = self.animation_list[self.frame_index]
			if pygame.time.get_ticks() - self.update_time > cd:
				self.update_time = pygame.time.get_ticks()
				self.frame_index += 1
			if self.frame_index >= len(self.animation_list):
				self.frame_index = 0

class Mari(Character):
	def __init__(self, scale):
		super().__init__(scale)
		for i in range(4):
			temp = pygame.image.load(f'./sprites/mari/mari_step_{i}.png').convert_alpha()
			self.animation_list.append(pygame.transform.scale(temp, (temp.get_width()*self.scale, temp.get_height()*self.scale)))
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()
		self.img = self.animation_list[self.frame_index]
		self.pos = pygame.Vector2((screen.get_width() / 2) - (self.img.get_width() / 2), (screen.get_height() / 2) - (self.img.get_height() / 2))
		self.speed = scale*1.5

class Enemy(Character):
	def __init__(self, scale, enemy, pos):
		super().__init__(scale)
		for i in range(2):
			temp = pygame.image.load(f'./sprites/{enemy}/{enemy}_move_{i}.png').convert_alpha()
			self.animation_list.append(pygame.transform.scale(temp, (temp.get_width()*self.scale, temp.get_height()*self.scale)))
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()
		self.img = self.animation_list[self.frame_index]
		self.pos = pos
		self.action = 1
		self.speed = scale*.75

	def chase_player(self, player):
		if self.pos.y > player.pos.y:
			self.pos.y -= self.speed
		if self.pos.y < player.pos.y:
			self.pos.y += self.speed
		if self.pos.x < player.pos.x:
			self.pos.x += self.speed
			if self.dir:
				self.img = pygame.transform.flip(self.img, True, False)
				self.dir = 0
		if self.pos.x > player.pos.x:
			self.pos.x -= self.speed
			if not self.dir:
				self.img = pygame.transform.flip(self.img, True, False)
				self.dir = 1

player = Mari(scale)
obake = Enemy(scale, 'obake', pygame.Vector2(0,0))

moving_left = False
moving_right = False
moving_up = False
moving_down = False
moving = False

while True:
	screen.blit(background, map_pos)
	
	for event in pygame.event.get():
		keys = pygame.key.get_pressed()
		if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.VIDEORESIZE:
			player.pos = pygame.Vector2((screen.get_width() / 2) - (player.img.get_width() / 2), (screen.get_height() / 2) - (player.img.get_height() / 2))
			player = Mari(1)
		if event.type == pygame.KEYDOWN:
			if keys[pygame.K_LEFT]:
				moving_left = True
			if keys[pygame.K_RIGHT]:
				moving_right = True
			if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
				moving_up = True
			if keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
				moving_down = True
		if event.type == pygame.KEYUP:
			if not keys[pygame.K_LEFT]:
				moving_left = False
			if not keys[pygame.K_RIGHT]:
				moving_right = False
			if not keys[pygame.K_UP]:
				moving_up = False
			if not keys[pygame.K_DOWN]:
				moving_down = False

		if moving_left or moving_right or moving_down or moving_up:
			moving = True
			if moving_left and moving_right and not moving_down and not moving_up:
				moving = False
			if moving_down and moving_up and not moving_left and not moving_right:
				moving = False
		else:
			moving = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		if map_pos.y <= 0:
			map_pos.y += player.speed
			obake.pos.y += player.speed
	if keys[pygame.K_DOWN]:
		if map_pos.y >= -1 * background.get_height() + screen.get_height():
			map_pos.y -= player.speed
			obake.pos.y -= player.speed
	if keys[pygame.K_LEFT]:
		if map_pos.x <= 0:
			map_pos.x += player.speed
			obake.pos.x += player.speed
		player.dir = 1
	if keys[pygame.K_RIGHT]:
		if map_pos.x >= -1 * background.get_width() + screen.get_width():
			map_pos.x -= player.speed
			obake.pos.x -= player.speed
		player.dir = 0

	if moving:
		player.update_action(1)
	else:
		player.update_action(0)

	if player.action:
		player.animate_move(100)
		if player.dir:
			player.img = pygame.transform.flip(player.img, True, False)
	screen.blit(player.img, player.pos)

	obake.animate_move(250)
	obake.chase_player(player)
	screen.blit(obake.img, obake.pos)
	
	screen.blit(pygame.font.SysFont("Arial-Bold", 48).render(str(int(clock.get_fps())), 1, pygame.Color('red')), (0,0))
	clock.tick(60)

	pygame.display.update()
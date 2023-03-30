import pygame, sys, os, csv

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
rectWidth, rectHeight = 100, 100

pygame.init()

scale = 3

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Yokai Hunter")

# mari = pygame.image.load("./sprites/mari/mari_step_1.png")
# mari = pygame.transform.scale(mari, (mari.get_width()*scale,mari.get_height()*scale))

mari_move_animation = []
for i in range(4):
	temp = pygame.image.load(f'./sprites/mari/mari_step_{i}.png')
	mari_move_animation.append(pygame.transform.scale(temp, (temp.get_width()*scale, temp.get_height()*scale)))

enemy = pygame.image.load("./sprites/lamp/chuuchin_obake_1.png")
enemy = pygame.transform.scale(enemy, (enemy.get_width()*scale, enemy.get_height()*scale))

background = pygame.image.load("./map.png")
background = pygame.transform.scale(background, (background.get_width()*scale, background.get_height()*scale))

clock = pygame.time.Clock()
speed = 0

enemy_pos = pygame.Vector2(0, 0)
map_pos = pygame.Vector2(background.get_width() / 2 * -1, background.get_height() / 2 * -1)

dir = 0
enemy_dir = 0
update_time = pygame.time.get_ticks()
frame_index = 0
action = 0

class Mari(pygame.sprite.Sprite):
	def __init__(self, scale):
		pygame.sprite.Sprite.__init__(self)
		self.dir = 0
		self.action = 0
		self.animation_list = []
		for i in range(4):
			temp = pygame.image.load(f'./sprites/mari/mari_step_{i}.png')
			self.animation_list.append(pygame.transform.scale(temp, (temp.get_width()*scale, temp.get_height()*scale)))
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()
		self.mari = self.animation_list[self.frame_index]
		self.pos = pygame.Vector2(screen.get_width() / 2-64, screen.get_height() / 2-64)
		
	def update_action(self, new_action):
		if new_action is not self.action:
			self.action = new_action
			self.frame_index = 0
			self.update_time = pygame.time.get_ticks()

	def animate_move(self):
		ANIMATION_COOLDOWN = 100
		if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
			self.update_time = pygame.time.get_ticks()
			self.frame_index += 1
		if self.frame_index >= len(self.animation_list):
			self.frame_index = 0

player = Mari(scale)

while True:
	screen.blit(background, map_pos)
	screen.blit(enemy, enemy_pos)
	
	# if flip:
	# 	mari = pygame.transform.flip(mari, True, False)
	# 	flip = False
	screen.blit(player.mari, player.pos)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		map_pos.y += 3 * speed
		enemy_pos.y += 3 * speed
		player.update_action(1)
	else:
		player.update_action(0)
	if keys[pygame.K_DOWN]:
		map_pos.y -= 3 * speed
		enemy_pos.y -= 3 * speed
		player.update_action(1)
	else:
		player.update_action(0)
	if keys[pygame.K_LEFT]:
		map_pos.x += 3 * speed
		enemy_pos.x += 3 * speed
		if not player.dir and not keys[pygame.K_RIGHT]:
			mari = pygame.transform.flip(player.mari, True, False)
			player.dir = 1
		player.update_action(1)
	else:
		player.update_action(0)
	if keys[pygame.K_RIGHT]:
		map_pos.x -= 3 * speed
		enemy_pos.x -= 3 * speed
		if player.dir and not keys[pygame.K_LEFT]:
			mari = pygame.transform.flip(player.mari, True, False)
			player.dir = 0
		player.update_action(1)
	else:
		player.update_action(0)

	if enemy_pos.y > player.pos.y:
		enemy_pos.y -= speed
	if enemy_pos.y < player.pos.y:
		enemy_pos.y += speed
	if enemy_pos.x < player.pos.x:
		enemy_pos.x += speed
		if enemy_dir:
			enemy = pygame.transform.flip(enemy, True, False)
			enemy_dir = 0
	if enemy_pos.x > player.pos.x:
		enemy_pos.x -= speed
		if not enemy_dir:
			enemy = pygame.transform.flip(enemy, True, False)
			enemy_dir = 1
	
	if action:
		player.animate_move()

	pygame.display.update()
	
	speed = clock.tick(60) / 10
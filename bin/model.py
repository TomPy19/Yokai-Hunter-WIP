import pygame, random
from bin.Enemy import Enemy

def check_dirs(player, moving):
	if moving[0]:
		player.dirx = 1
	if moving[1]:
		player.diry = -1
	if moving[2]:
		player.dirx = -1
	if moving[3]:
		player.diry = 1
	if not moving[1] and not moving[3]:
		player.diry = 0
	if not moving[2] and not moving[0]:
		player.dirx = 0

def spawn_enemy(cd, spawn_time, screen, default_enemy, enemy_group):
	if pygame.time.get_ticks() - spawn_time > cd:
		spawn_time = pygame.time.get_ticks()
		min = int((screen.get_width() / 2) + default_enemy.img.get_width())
		randx = (screen.get_width() / 2) + random.randint(min, min+100) * pow(-1, random.randint(1,2))
		randy = (screen.get_height() / 2) + random.randint(min, min+100) * pow(-1, random.randint(1,2))
		obake = Enemy(default_enemy.scale, 'obake', pygame.Vector2(randx, randy), screen)
		enemy_group.add(obake)
		# print(f'Enemy Spawned at {randx}, {randy}')
	return spawn_time
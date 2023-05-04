import pygame, random
from bin.Enemy import Enemy
from bin.Chest import Chest

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

def spawn_enemy(cd, spawn_time, screen, scale, enemy_group):
	if pygame.time.get_ticks() - spawn_time > cd:
		spawn_time = pygame.time.get_ticks()
		min = int((screen.get_width() / 2))
		randx = (screen.get_width() / 2) + random.randint(min, min+100) * pow(-1, random.randint(1,2))
		randy = (screen.get_height() / 2) + random.randint(min, min+100) * pow(-1, random.randint(1,2))
		weights = [0,0,0,0,0,0,1,1,1,2]
		rand_enemy = random.choice(weights)
		enemies = [{
			'type': 'obake',
			'health': 2,
			'speed': .75,
			'ani_cd': 250
		}, {
			'type': 'yuurei',
			'health': 1,
			'speed': 1,
			'ani_cd': 150
		}, {
			'type': 'kappa',
			'health': 3,
			'speed': .5,
			'ani_cd': 350
		}]
		enemy = Enemy(scale, enemies[rand_enemy]['type'], pygame.Vector2(randx, randy), screen, 
									enemies[rand_enemy]['speed'], enemies[rand_enemy]['health'], enemies[rand_enemy]['ani_cd'])
		enemy_group.add(enemy)
	return spawn_time

def spawn_chests(screen, scale, chest_group):
	min = int((screen.get_width() / 2))
	for i in range(20):
		randx = (screen.get_width() / 2) + random.randint(min, min+100) * pow(-1, random.randint(1,2))
		randy = (screen.get_height() / 2) + random.randint(min, min+100) * pow(-1, random.randint(1,2))
		chest = Chest(scale, screen, pygame.Vector2(randx, randy))
		chest_group.add(chest)
	return chest_group

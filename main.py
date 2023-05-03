import pygame, sys, math
from bin.controller import *
from bin.Enemy import *
from bin.Kunai import *
from bin.Mari import *
from bin.model import *
from bin.view import *
from bin.ui import *

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
rectWidth, rectHeight = 100, 100

pygame.init()

moving = [False, False, False, False]

screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
scale = math.sqrt(screen.get_width() * screen.get_height()) / 480
pygame.display.set_caption("Yokai Hunter")
screen.set_colorkey(pygame.color.Color('black'))

screen.blit(pygame.font.SysFont("Arial-Bold", 80).render("LOADING...", 1, pygame.Color('white')), (0,0))
background = pygame.image.load("./map.png").convert()
background = pygame.transform.scale(background, (background.get_width()*2*scale, background.get_height()*2*scale))

i_time = pygame.time.get_ticks()
clock = pygame.time.Clock()
speed = 0

map_pos = pygame.Vector2((background.get_width() - screen.get_width()) / -2, (background.get_height() - screen.get_height()) / -2)

player = Mari(scale, screen)
knife = Kunai(player, scale, screen)
weapon_group = pygame.sprite.Group()
weapon_group.add(knife)
enemy_group = pygame.sprite.Group()
spawn_time = pygame.time.get_ticks()

while True:
	screen.blit(background, map_pos)
	controls(map_pos, player, enemy_group, weapon_group, background, screen)
	
	for event in pygame.event.get():
		keys = pygame.key.get_pressed()
		if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.VIDEORESIZE:
			scale = math.sqrt(screen.get_width() * screen.get_height()) / 480
			player = Mari(scale, screen)
			new_group = pygame.sprite.Group()
			for sprite in enemy_group:
				new_group.add(Enemy(scale, sprite.enemy, pygame.Vector2(sprite.rect.x, sprite.rect.y)), screen)
			enemy_group = new_group
			background = pygame.transform.scale(background, (background.get_width()*scale, background.get_height()*scale))
			map_pos = pygame.Vector2((background.get_width() - screen.get_width()) / -2, (background.get_height() - screen.get_height()) / -2)
			

	if enemy_group.sprites:
		for sprite in enemy_group:
			sprite.animate_move(250)
			sprite.chase_player(player)
			sprite.draw()

	player.is_moving = player.check_moving()
	if player.is_moving:
		player.animate_move(100)
	
	if pygame.time.get_ticks() - knife.update_time > knife.cd:
		knife = Kunai(player, scale, screen)
		weapon_group.add(knife)
	weapon_group.update(enemy_group)
	weapon_group.draw(screen)
	player.draw()
	spawn_time = spawn_enemy(1000, spawn_time, screen, scale, enemy_group)
	
	screen.blit(pygame.font.SysFont("Arial-Bold", 48).render(str(int(clock.get_fps())), 1, pygame.Color('red')), (0,0))
	UpdateClock(i_time, screen)
	clock.tick(60)

	pygame.display.update()
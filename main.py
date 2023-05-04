import pygame, sys, math
from bin.controller import *
from bin.Enemy import *
from bin.Kunai import *
from bin.Mari import *
from bin.model import *
from bin.view import *
from bin.ui import *
from bin.Boss import *

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
rectWidth, rectHeight = 100, 100

pygame.init()

moving = [False, False, False, False]

screen = pygame.display.set_mode(SCREEN_SIZE)
scale = math.sqrt(screen.get_width() * screen.get_height()) / 480
pygame.display.set_caption("Yokai Hunter")
screen.set_colorkey(pygame.color.Color('black'))

screen.blit(pygame.font.SysFont("Arial-Bold", 80).render("LOADING...", 1, pygame.Color('white')), (0,0))
background = pygame.image.load("./map.png").convert()
background = pygame.transform.scale(background, (background.get_width()*scale, background.get_height()*scale))

i_time = pygame.time.get_ticks()
clock = pygame.time.Clock()
speed = 0

map_pos = pygame.Vector2((background.get_width() - screen.get_width()) / -2, (background.get_height() - screen.get_height()) / -2)

player = Mari(scale, screen)
knife = Kunai(player, scale, screen)
weapon_group = pygame.sprite.Group()
weapon_group.add(knife)
enemy_group = pygame.sprite.Group()
enemy_spawn_time = pygame.time.get_ticks()
talisman_group = pygame.sprite.Group()
item_spawn_time = pygame.time.get_ticks()
boss_ex = Boss(scale, screen, 1, 30, 0, 0)
spawn_boss_time = False
boss_event = False
game_end = False
won = False
lost = False

while True:
	screen.blit(background, map_pos)
	for event in pygame.event.get():
		keys = pygame.key.get_pressed()
		if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()

	if not game_end:
		controls(map_pos, player, enemy_group, weapon_group, talisman_group, background, screen)
		if enemy_group.sprites():
			if not boss_event:
				for sprite in enemy_group:
					sprite.animate_move(sprite.ani_cd)
					sprite.kill()
					sprite.chase_player(player, enemy_group)
					enemy_group.add(sprite)
					sprite.draw()
				enemy_spawn_time = spawn_enemy(2000, enemy_spawn_time, screen, scale, enemy_group)
			else:
				boss = enemy_group.sprites()[0]
				boss.chase_player(player)
				enemy_group.draw(screen)
				if boss.health == 0:
					won = True
		else:
			enemy_spawn_time = spawn_enemy(0, enemy_spawn_time, screen, scale, enemy_group)
		
		player.is_moving = player.check_moving()
		if player.is_moving:
			player.animate_move(100)

		if pygame.time.get_ticks() - knife.update_time > knife.cd:
			knife = Kunai(player, scale, screen)
			weapon_group.add(knife)
		weapon_group.update(enemy_group, player)
		weapon_group.draw(screen)
		lost = player.check_collision(enemy_group, talisman_group)
		player.draw()
		item_spawn_time = spawn_talisman(item_spawn_time, screen, scale, talisman_group)
		talisman_group.draw(screen)

		# screen.blit(pygame.font.SysFont("Arial-Bold", 48).render(str(int(clock.get_fps())), 1, pygame.Color('red')), (0,0))
		if spawn_boss_time:
			enemy_group.empty()
			spawn_boss(screen, scale, enemy_group)
			spawn_boss_time = False
			boss_event = True
		spawn_boss_time = UpdateClock(i_time, screen, boss_event, spawn_boss_time, enemy_group.sprites()[0], player)
		clock.tick(60)

		if lost or won:
			game_end = True


	display_loss(screen, lost, player)
	display_win(screen, won, player)

	pygame.display.update()
import pygame

def controls(map_pos, player, enemy_group, background, screen):
  for i in range(len(player.moving)):
    player.moving[i] = False

  keys = pygame.key.get_pressed()

  if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
    player.dir = 1
    if map_pos.y <= 0:
      map_pos.y += player.speed
      for sprite in enemy_group:
        sprite.rect.y += player.speed
      player.moving[1] = True
    if map_pos.x >= -1 * background.get_width() + screen.get_width():
      map_pos.x -= player.speed
      for sprite in enemy_group:
        sprite.rect.x -= player.speed
      player.moving[0] = True
    return
  elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
    player.dir = 3
    if map_pos.y <= 0:
      map_pos.y += player.speed
      for sprite in enemy_group:
        sprite.rect.y += player.speed
      player.moving[1] = True
    if map_pos.x <= 0:
      map_pos.x += player.speed
      for sprite in enemy_group:
        sprite.rect.x += player.speed
      player.moving[2] = True
    return
  elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
    player.dir = 5
    if map_pos.y >= -1 * background.get_height() + screen.get_height():
      map_pos.y -= player.speed
      for sprite in enemy_group:
        sprite.rect.y -= player.speed
      player.moving[3] = True
    if map_pos.x <= 0:
      map_pos.x += player.speed
      for sprite in enemy_group:
        sprite.rect.x += player.speed
      player.moving[2] = True
    return
  elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
    player.dir = 7
    if map_pos.y >= -1 * background.get_height() + screen.get_height():
      map_pos.y -= player.speed
      for sprite in enemy_group:
        sprite.rect.y -= player.speed
      player.moving[3] = True
    if map_pos.x >= -1 * background.get_width() + screen.get_width():
      map_pos.x -= player.speed
      for sprite in enemy_group:
        sprite.rect.x -= player.speed
      player.moving[0] = True
    return
  elif keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
    player.dir = 0
    if map_pos.x >= -1 * background.get_width() + screen.get_width():
      map_pos.x -= player.speed
      for sprite in enemy_group:
        sprite.rect.x -= player.speed
      player.moving[0] = True
    return
  elif keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
    player.dir = 4
    if map_pos.x <= 0:
      map_pos.x += player.speed
      for sprite in enemy_group:
        sprite.rect.x += player.speed
      player.moving[2] = True
    return
  elif keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
    player.dir = 2
    if map_pos.y <= 0:
      map_pos.y += player.speed
      for sprite in enemy_group:
        sprite.rect.y += player.speed
      player.moving[1] = True
    return
  elif keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
    player.dir = 6
    if map_pos.y >= -1 * background.get_height() + screen.get_height():
      map_pos.y -= player.speed
      for sprite in enemy_group:
        sprite.rect.y -= player.speed
      player.moving[3] = True
    return
  else: return
  
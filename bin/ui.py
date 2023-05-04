import pygame

def UpdateClock(clock, screen, boss_event, spawn_boss_time, boss, player):
  current_ticks = pygame.time.get_ticks()
  current_time = (current_ticks - clock)/1000
  mins = int(current_time/60)
  secs = int(current_time%60)

  if boss_event:
    title = pygame.font.SysFont("Arial-Bold", 64).render(f"VERMILION BIRD", 1, pygame.Color('white'))
    title_rect = title.get_rect()
    screen.blit(title, (640-(title_rect.width/2), screen.get_height() - (screen.get_height() / 40 + title_rect.height + 10)))
    pygame.draw.rect(screen, pygame.Color('red'), boss.hp_bar)
  
  timer = pygame.font.SysFont("Arial-Bold", 64).render(f"{mins:02d}" + ':' + f"{secs:02d}", 1, pygame.Color('white'))
  timer_rect = timer.get_rect()
  screen.blit(timer, (640-(timer_rect.width/2),10))

  killed = pygame.font.SysFont("Arial-Bold", 52).render(f"SCORE: {player.killed}", 1, pygame.Color('white'))
  screen.blit(killed, (10, 10))
  
  spawn_boss_time = mins >= 5 and not boss_event
  return spawn_boss_time
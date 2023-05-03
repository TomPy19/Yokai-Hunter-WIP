import pygame

def UpdateClock(clock, screen):
  current_ticks = pygame.time.get_ticks()
  current_time = (current_ticks - clock)/1000
  mins = int(current_time/60)
  secs = int(current_time%60)

  timer = pygame.font.SysFont("Arial-Bold", 64).render(f"{mins:02d}" + ':' + f"{secs:02d}", 1, pygame.Color('white'))
  timer_rect = timer.get_rect()

  screen.blit(timer, (640-(timer_rect.width/2),20))
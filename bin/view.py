import pygame

def display_loss(screen, lost, player):
  if lost:
    death_text = pygame.font.SysFont("Arial-Bold", 128).render("YOU DIED", 1, pygame.Color('white'))
    death_text_rect = death_text.get_rect()
    subtext = pygame.font.SysFont("Arial-Bold", 64).render(f'But you still killed {player.killed} yokai!', 1, pygame.Color('white'))
    subtext_rect = subtext.get_rect()
    screen.blit(death_text, (screen.get_width()/2 - death_text_rect.width/2, screen.get_height()/2 - death_text_rect.height - 5))
    screen.blit(subtext, (screen.get_width()/2 - subtext_rect.width/2, screen.get_height()/2 + 5))

def display_win(screen, won, player):
  if won:
    death_text = pygame.font.SysFont("Arial-Bold", 128).render("YOU SAVED HUMANITY", 1, pygame.Color('white'))
    death_text_rect = death_text.get_rect()
    subtext = pygame.font.SysFont("Arial-Bold", 64).render(f'And you killed {player.killed} yokai!', 1, pygame.Color('white'))
    subtext_rect = subtext.get_rect()
    screen.blit(death_text, (screen.get_width()/2 - death_text_rect.width/2, screen.get_height()/2 - death_text_rect.height - 5))
    screen.blit(subtext, (screen.get_width()/2 - subtext_rect.width/2, screen.get_height()/2 + 5))
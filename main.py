import pygame, sys

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
rectWidth, rectHeight = 100, 100

pygame.init()

surface = pygame.display.set_mode(SCREEN_SIZE)

rect = pygame.Rect(200, 200, 100, 100)

mari = pygame.image.load("./mari.png")
mari = pygame.transform.scale(mari, (128,128))

while True:
	surface.fill((255,255,255))

	# pygame.draw.rect(surface, (255,0,0), rect)
	surface.blit(mari, (100, 100))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
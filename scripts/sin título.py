import pygame
from spriteTexto import *
import random
import suite



BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
pygame.init()
screen = pygame.display.set_mode((800, 800))

ROJOCLARO = (255,   0,   0)
ROJO = (155,   0,   0)
VERDECLARO = (  0, 255,   0)
VERDE = (  0, 155,   0)
AZULCLARO = (  0,   0, 255)
AZUL = (  0,   0, 155)
BLANCO = (255, 255, 255)
NEGRO= (0, 0, 0)

colores=[ROJOCLARO,VERDECLARO,AZULCLARO,VERDE]
screen.fill(random.choice(colores))
imagen= Texto((100,100), BASICFONT,"hola", "hola")
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			suite.terminate()
	screen.fill(ROJO)
	xy=pygame.mouse.get_pos()
	while imagen.toca(xy[0],xy[1]):
		imagen.handle_event(event,screen)
		screen.blit(imagen.texto,imagen.rect)
		pygame.display.flip()
	screen.blit(imagen.texto,imagen.rect)
	pygame.display.flip()
	

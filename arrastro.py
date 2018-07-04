import pygame
from pygame.locals import *
 
pygame.init()
 
pantalla = pygame.display.set_mode((1000,1000),0,32)
imagen = pygame.image.load("mario.png")
 
x = 10
y = 10
tupla=()
reloj = pygame.time.Clock()
while True:
	for eventos in pygame.event.get():
		if eventos.type == pygame.QUIT:
			exit()
	if pygame.mouse.get_pressed()[0]==1:
		x,y = pygame.mouse.get_pos()
		x-=400
		y-=200
		pantalla.blit(imagen,(x,y))
		pygame.display.flip()
	pantalla.blit(imagen,(x,y))
	pygame.display.update()
	reloj.tick(25)
	pantalla.fill((0,0,0))
	

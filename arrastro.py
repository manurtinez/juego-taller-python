import pygame
from pygame.locals import *
 
pygame.init()
WHITE = (255, 255, 255)
#pygame.Color(255, 255, 255, 128)
pantalla = pygame.display.set_mode((1000,1000),0,32)
imagen = pygame.image.load("prueba.png")
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
		x-=300
		y-=250
		rectangulo=pygame.Rect(x,y, imagen.get_rect()[2], imagen.get_rect()[3])
		pygame.draw.rect(pantalla,pygame.Color(0, 0, 0),rectangulo)
		pantalla.blit(imagen,(x,y))

		pygame.display.update()
		
	pantalla.blit(imagen,(x,y))
	pygame.display.update()

	pantalla.fill((255,0,0))
	

# -*- coding: utf-8 -*-
import time
import pygame
from player import *

pygame.init()

# Definimos algunas variables que usaremos en nuestro código

ancho_ventana = 1000
alto_ventana = 800
screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Tutorial sprites Piensa 3D")
clock = pygame.time.Clock()
letra_A= Imagen((ancho_ventana-900, alto_ventana-700), "kate.png")



player = Imagen((ancho_ventana/2, alto_ventana/2),"kate.png")
player.image=pygame.transform.rotozoom(player.image,0,.8)
game_over = False

persona=True

while game_over == False:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True
	x,y=pygame.mouse.get_pos()
	if pygame.mouse.get_pressed()[0]:
		if letra_A.toca (x,y):
			print("player2")
			if letra_A.rect.colliderect(player.rect):
				if player.arrastra:
					print("soy Persona y empiezo con P")
					player.arrastra=False
			
		elif player.toca(x,y):
			player.handle_event(event)
		
	
	screen.fill(pygame.Color('gray'))
	if player.arrastra:
		screen.blit(player.image, player.rect)
	
	screen.blit(letra_A.image, letra_A.rect) 
	pygame.display.flip()
	clock.tick(20)

pygame.quit ()

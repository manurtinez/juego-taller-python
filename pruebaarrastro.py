# -*- coding: utf-8 -*-
import time
import pygame
from spriteImagen import *

pygame.init()

# Definimos algunas variables que usaremos en nuestro código

ancho_ventana = 1600
alto_ventana = 900
screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Tutorial sprites Piensa 3D")
clock = pygame.time.Clock()
letra_A= Imagen((ancho_ventana-900, alto_ventana-700), "kate.png")


player2 = Imagen((ancho_ventana/3, alto_ventana/3), "kate.png")
player = Imagen((ancho_ventana/2, alto_ventana/2),"kate.png")
player.image=pygame.transform.rotozoom(player.image,0,.8)
player2.image=pygame.transform.rotozoom(player.image,0,.8)
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
			elif letra_A.rect.colliderect(player2.rect):
				if player2.arrastra:
					player2.arrastra = False
			
		else: 
			if player2.toca(x,y):
				player2.handle_event(event)
			else:
				if player.toca(x,y):
					player.handle_event(event)
	
	screen.fill(pygame.Color('gray'))
	if player.arrastra:
		screen.blit(player.image, player.rect)
	if player2.arrastra:
		screen.blit(player2.image, player2.rect)
	
	screen.blit(letra_A.image, letra_A.rect) 
	pygame.display.flip()
	clock.tick(200)

pygame.quit ()

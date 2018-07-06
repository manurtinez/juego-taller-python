# -*- coding: utf-8 -*-

import pygame

class Imagen(pygame.sprite.Sprite):
	def __init__(self, position,imagen):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagen)
		self.rect = self.image.get_rect()
		self.rect.topleft=position
		self.nombre=imagen
		self.arrastra=True
	
	def toca(self,x,y):
		return self.rect.collidepoint(x,y)
	
	def set_rect(self,ancho,alto):
		self.rect.width=ancho
		self.rect.height=alto
		
	def update(self):
		if pygame.mouse.get_pressed()[0]:
			x,y =pygame.mouse.get_pos()
			if self.toca(x,y):
				print("toca")
			x-=100
			y-=100
			
			self.rect.x=x
			self.rect.y=y    #deberia ser dependiendo el rectangulo donde se haga click
			pygame.display.flip()
	
	def handle_event(self, event):
		if event.type == pygame.QUIT:
			game_over = True
		
		if event.type == pygame.MOUSEMOTION:
			self.update()
				

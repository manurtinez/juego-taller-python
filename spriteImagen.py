# -*- coding: utf-8 -*-

import pygame
import os
from pygame.locals import *
class Imagen(pygame.sprite.Sprite):
	def __init__(self, position,imagen, nombre, path= os.getcwd()):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagen)
		self.rect = self.image.get_rect()
		self.rect_aux=self.rect
		self.rect.topleft=position
		self.nombre= nombre
		self.arrastra=True
	
	def toca2(self,rectangulo):
		return self.rect.colliderect(rectangulo)
	def set_rect_aux(self,tupla):
		self.rect_aux=tupla
	def toca(self, x, y):
		return self.rect.collidepoint(x,y)
	
	def set_rect(self,ancho,alto):
		self.rect.width=ancho
		self.rect.height=alto
	def get_rect(self):
		return self.rect
		
	def update(self,pantalla):
		if pygame.mouse.get_pressed()[0]:
			x,y =pygame.mouse.get_pos()
			x-=100
			y-=100	
			self.rect.x=x
			self.rect.y=y
		if self.rect.left < 0:
			self.rect.left = 0
		elif self.rect.right > 1320:
			self.rect.right = 1320
		if self.rect.top <= 0:
			self.rect.top = 0
		elif self.rect.bottom >= 720:
			self.rect.bottom = 720  
			
	def handle_event(self, event,pantalla):
		if event.type == pygame.QUIT:
			game_over = True
		
		if event.type == pygame.MOUSEMOTION:
			self.update(pantalla)
		

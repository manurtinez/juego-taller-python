import pygame, sys, os
from pygame.locals import *


WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
BRIGHTRED = (255,   0,   0)
RED = (155,   0,   0)
BRIGHTGREEN = (  0, 255,   0)
GREEN = (  0, 155,   0)
BRIGHTBLUE = (  0,   0, 255)
BLUE = (  0,   0, 155)
BRIGHTYELLOW = (255, 255,   0)
YELLOW = (155, 155,   0)
DARKGRAY = ( 40,  40,  40)

ANCHOVENTANA = 640
ALTOVENTANA = 480

def main():
	pygame.init()
	dibujarVentana()
	while True:
		chequearQuit()

def dibujarVentana():
	pantalla = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA))
	pygame.display.set_caption('Prueba')
	pantalla.fill(BRIGHTGREEN)
	pygame.display.update()

def terminate():
	pygame.quit()
	sys.exit()

def chequearQuit():
	for event in pygame.event.get(QUIT):
		terminate()
	for event in pygame.event.get(KEYUP):
		if event.key == K_ESCAPE:
			terminate()
		pygame.event.post(event)




if __name__ == '__main__':
	main()
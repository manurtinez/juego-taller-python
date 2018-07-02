import pygame, sys, os
from pygame.locals import *
from random import randint

DIRIMAGENES = r"./imagenes"

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

ANCHOVENTANA = 1600
ALTOVENTANA = 900
IMAGENES = [f for f in os.listdir(DIRIMAGENES) if os.path.splitext(f)[-1] == '.png']
IMAGENESVIS = [False]*len(IMAGENES)


def main():
	pygame.init()
	pantalla = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA))
	pygame.display.set_caption('Prueba')
	pantalla.fill(BRIGHTGREEN)
	pygame.display.update()
	mostrarImagenes(pantalla)
	while True:
		chequearQuit()

def mostrarImagenes(pantalla):
	x = 100
	y = 100
	for i in range(1,6):
		im = randint(1, len(IMAGENES)-1)
		while(IMAGENESVIS[im]):
			im = randint(1, len(IMAGENES)-1)
		imagen = pygame.image.load(DIRIMAGENES+os.sep+IMAGENES[im])
		imagen = pygame.transform.rotozoom(imagen, 0, .8)
		IMAGENESVIS[im] = True
		pantalla.blit(imagen, (x, y))
		pygame.display.update()
		x = x+300

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
import pygame, sys, os
from pygame.locals import *
from random import randint
import Boton

pygame.init()

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
ANCHOBOTON=150
ALTOBOTON=50
ANCHOCENTROVENTANA= ANCHOVENTANA / 2
ALTOCENTROVENTANA= ALTOVENTANA / 2
FUENTEBOTON=pygame.font.SysFont("comicsansms", 25)
clock = pygame.time.Clock()

#musica

pygame.mixer.music.set_volume(0.9)
sonidoBien = pygame.mixer.Sound('./sonidos/109662__grunz__success.wav')
sonidoMal = pygame.mixer.Sound('./sonidos/366107__original-sound__error_sound.wav')
pygame.mixer.music.load('./sonidos/432367__a-c-acid__fast-ukulele.mp3')



pantalla = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA))

botonInicio = Boton.boton(RED, BLUE, pantalla, "INICIAR", ANCHOCENTROVENTANA - (ANCHOBOTON / 2),
                            ALTOCENTROVENTANA - 30, ANCHOBOTON, ALTOBOTON, WHITE, -30, ANCHOCENTROVENTANA,
                            ALTOCENTROVENTANA, FUENTEBOTON)

botonSalir = Boton.boton(RED, BLUE, pantalla, "SALIR", ANCHOCENTROVENTANA - (ANCHOBOTON / 2),
                           ALTOCENTROVENTANA + 50, ANCHOBOTON, ALTOBOTON, WHITE, 50, ANCHOCENTROVENTANA,
                           ALTOCENTROVENTANA, FUENTEBOTON)
def main():
	pygame.display.set_caption('Prueba')
	pantalla.fill(BRIGHTGREEN)
	pygame.display.update()
	mostrarImagenes(pantalla)
	pygame.mixer.music.play(-1, 0.0)
	reproduccionMusica= True
	while True:
		#x, y= pygame.mouse.get_pos()
		for event in pygame.event.get():
			if (event.type == KEYUP):
				if event.key == K_ESCAPE:
					terminate()
				if event.key == K_m:
					if (reproduccionMusica):
						pygame.mixer.music.pause()
						reproduccionMusica= False
					else:
						pygame.mixer.music.unpause()
						reproduccionMusica= True

		
		#print (x, y)
		pygame.display.update()
		clock.tick(30)
		
		
		
		

def agregarMatriz(imagen, matriz, i, x, y, lista):
		matriz.append([])
		r = pygame.Rect(0+x, 0+y+imagen.get_rect()[3], imagen.get_rect()[2], imagen.get_rect()[3])
		matriz[i].append(r)
		lista.append(r)

def mostrarImagenes(pantalla):
	matriz = []
	lista=[]
	x = 0
	y = 100
	for i in range(0,5):
		im = randint(1, len(IMAGENES)-1)
		while(IMAGENESVIS[im]):
			im = randint(1, len(IMAGENES)-1)
		imagen = pygame.image.load(DIRIMAGENES+os.sep+IMAGENES[im])
		imagen = pygame.transform.rotozoom(imagen, 0, .8)
		agregarMatriz(imagen, matriz, i, x, y, lista)
		IMAGENESVIS[im] = True
		pantalla.blit(imagen, (x, y))
		pygame.display.update()
		x = x+300
	print(matriz)
	print (lista[1])
		
def pantallaInicio():
    """
    Carga la pantalla inicial del juego
    """
    
    while True:

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                terminate()

        botonInicio.mostrarBoton()
        botonSalir.mostrarBoton()

        if botonInicio.toca(getCursorPos()) and botonIzquierdoMouseClickeado():
            return
        elif botonSalir.toca(getCursorPos()) and botonIzquierdoMouseClickeado():
            terminate()

        pygame.display.update()
        
def botonIzquierdoMouseClickeado():
    return pygame.mouse.get_pressed()[0]

def getCursorPos():
    return pygame.mouse.get_pos()
    
def terminate():
	pygame.quit()
	sys.exit()



if __name__ == '__main__':
	pygame.display.set_caption('Prueba')
	pantalla.fill(BRIGHTGREEN)
	pygame.display.update()
	pantallaInicio()
	main()

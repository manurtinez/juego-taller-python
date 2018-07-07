# -*- coding: utf-8 -*-
import time, Boton
import sys
import pygame
from pygame.locals import *
from spriteImagen import *
 
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
 


pygame.init()
ancho_ventana = 900
alto_ventana = 900
pygame.display.set_caption("Tutorial sprites Piensa 3D")
clock = pygame.time.Clock()
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
WHITE     = (255, 255, 255)
ANCHOBOTON=150
ALTOBOTON=50
ANCHOCENTROVENTANA= ancho_ventana / 2
ALTOCENTROVENTANA= alto_ventana / 2
FUENTEBOTON=pygame.font.SysFont("comicsansms", 25)
screen = pygame.display.set_mode((ancho_ventana, alto_ventana))

DIRIMAGENES= "./imagenes/"


diccionario_imagenes= {}

botonInicio = Boton.boton(RED, BLUE, screen, "INICIAR", ANCHOCENTROVENTANA - (ANCHOBOTON / 2),
                            ALTOCENTROVENTANA - 30, ANCHOBOTON, ALTOBOTON, WHITE, -30, ANCHOCENTROVENTANA,
                            ALTOCENTROVENTANA, FUENTEBOTON)

botonSalir = Boton.boton(RED, BLUE, screen, "SALIR", ANCHOCENTROVENTANA - (ANCHOBOTON / 2),
                           ALTOCENTROVENTANA + 50, ANCHOBOTON, ALTOBOTON, WHITE, 50, ANCHOCENTROVENTANA,
                           ALTOCENTROVENTANA, FUENTEBOTON)

pygame.mixer.music.set_volume(0.5)
sonidoBien = pygame.mixer.Sound('./sonidos/109662__grunz__success.wav')
sonidoMal = pygame.mixer.Sound('./sonidos/366107__original-sound__error_sound.wav')
pygame.mixer.music.load('./sonidos/432367__a-c-acid__fast-ukulele.mp3')
 

 
def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (ancho_ventana - 120, 10)
    screen.blit(scoreSurf, scoreRect)
 
 
# Definimos algunas variables que usaremos en nuestro código
 
 
 
def main():
    letra_A= Imagen((ancho_ventana-900, alto_ventana-700), "kate.png")
    player = Imagen((ancho_ventana/2, alto_ventana/2),"kate.png")
    player2 = Imagen((ancho_ventana/1.5, alto_ventana/1.5), "kate.png")
    player2.image=pygame.transform.rotozoom(player.image,0,.8)
    player.image=pygame.transform.rotozoom(player.image,0,.8)
    pygame.mixer.music.play(-1, 0.0)
    persona=True
    while True:
        correrJuego(player, player2, letra_A)
       
   
def correrJuego(player, player2, letra_A):
	puntos= 0
	reproduccionMusica= True
	drawScore(puntos)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				terminate()
			if (event.type == KEYUP):
				if event.key == K_ESCAPE:
					terminate()
				if event.key == K_m:
					if reproduccionMusica:
						pygame.mixer.music.pause()
						reproduccionMusica= False
					else:
						pygame.mixer.music.unpause()
						reproduccionMusica= True
			x,y=pygame.mouse.get_pos()
			if pygame.mouse.get_pressed()[0]:
				if letra_A.toca (x,y):
					print("letra_A")
					if letra_A.rect.colliderect(player.rect):
						if player.arrastra:
							player.arrastra=False
							puntos+=3
					if letra_A.rect.colliderect(player2.rect):
						if player2.arrastra:
							player2.arrastra = False
							puntos+=3
				else:
					if player2.toca(x,y):
						player2.handle_event(event)
					elif player.toca(x,y):
						player.handle_event(event)

		screen.fill(pygame.Color('gray'))
		if player.arrastra:
			screen.blit(player.image, player.rect)
		if player2.arrastra:
			screen.blit(player2.image, player2.rect)
		drawScore(puntos)
		screen.blit(letra_A.image, letra_A.rect)
		pygame.display.flip()
		clock.tick(60)
		
def pantallaInicio():
    """
    Carga la pantalla inicial del juego
    """
    screen.fill(pygame.Color('dark green'))
    while True:

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                terminate()
            if (event.type == KEYUP):
                if event.key == K_ESCAPE:
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
    
    
def cargarDiccionario(dicc, ruta= DIRIMAGENES):
	"""carga diccionario con todas las imagenes de la ruta"""
	lista=[]
	for letra in os.listdir(ruta):
		if os.path.isdir(ruta+letra):
			for img in os.listdir(ruta+letra):
				lista.append(img)
			dicc[letra]= lista
	#print (dicc)
	return dicc)
 
if __name__ == "__main__":
    cargarDiccionario(diccionario_imagenes)
    pantallaInicio()
    main()
    
    
    
    
		
		

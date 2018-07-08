# -*- coding: utf-8 -*-
import time, Boton
import sys
import pygame
from pygame.locals import *
from spriteImagen import *
import random
 
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
ancho_ventana = 1280
alto_ventana = 720
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

LISTA_DIR_IMAGENES= ["./imagenes/A/", "./imagenes/E/", "./imagenes/I/", "./imagenes/O/", "./imagenes/U/"] 


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
    scoreSurf = BASICFONT.render('puntos: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (ancho_ventana - 120, 10)
    screen.blit(scoreSurf, scoreRect)
 
 
# Definimos algunas variables que usaremos en nuestro código
 
 
 
def main():
	aux=0           # indice que hace referencia a la letra a usar del diccionario
	dicc_actual= seleccionDeImagenes(diccionario_imagenes, aux)
	
	#print(diccionario_imagenes['Letras'][0])
	#char= imagen[0].upper()              
	#ruta= DIRIMAGENES+char+"/"+imagen    
	#imagen= Imagen((ancho_ventana_aux, alto_ventana_aux), ruta)
	lista_sprites= inicializarImagenes(dicc_actual, LISTA_DIR_IMAGENES[aux])
	pygame.mixer.music.play(-1, 0.0)
	while True:
		copy = lista_sprites[1:]
		random.shuffle(copy)
		lista_sprites[1:] = copy
		tupla=tuple(lista_sprites[1:])
		correrJuego(RED,lista_sprites[0], tupla)
		dicc_actual= seleccionDeImagenes(diccionario_imagenes, aux)     #hay q hacer que cuando se complete el nivel de la letra A, 
																		#se pase al siguiente nivel con esta funcion e incrementando la variable aux
																		#para que se seleccione la siguiente vocal


def correrJuego(color,letra,args):
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
				for objeto in args:
					if objeto.toca(x,y):
						puntos=evaluar(objeto,letra,event,color,puntos,args)		
		screen.fill(color)
		for objeto in args:
			if objeto.arrastra:
				screen.blit(objeto.image, objeto.rect)
		drawScore(puntos)
		screen.blit(letra.image, letra.rect)
		pygame.display.flip()
		clock.tick(60)


def evaluar(objeto,objeto_destino,event,color,puntos,args):
	while not objeto_destino.rect.colliderect(objeto.rect) and pygame.mouse.get_pressed()[0]:
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
		screen.fill(color)
		for obj in args:
			if obj.arrastra:
				screen.blit(obj.image,obj.rect)
		drawScore(puntos)
		screen.blit(objeto_destino.image, objeto_destino.rect)
		objeto.handle_event(event,screen)
		screen.blit(objeto.image,objeto.rect)
		pygame.display.flip()
		clock.tick(60)
	if objeto_destino.rect.colliderect(objeto.rect):
		if objeto.arrastra:
			objeto.arrastra=False
			if objeto.nombre[0].upper() == objeto_destino.nombre:
				puntos+= 3
			else:
				puntos-= 3
	return puntos
	
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

def seleccionDeImagenes(dicc, aux):
	"""retorna diccionario cargado con 5 imagenes aleatorias"""
	dicc_aux={}
	if aux == 0:
		lis= random.sample(dicc["A"], 3)
		lis.append(random.sample(dicc["E"],1)[0])
		lis.append(random.sample(dicc["I"],1)[0])
		dicc_aux["A"]= lis
	elif aux == 1:
		lis= random.sample(dicc["E"], 3)
		lis.append(random.sample(dicc["A"],1)[0])
		lis.append(random.sample(dicc["O"],1)[0])
		dicc_aux["E"]= lis
	elif aux == 2:
		lis= random.sample(dicc["I"], 3)
		lis.append(random.sample(dicc["U"],1)[0])
		lis.append(random.sample(dicc["O"],1)[0])
		dicc_aux["I"]= lis
	elif aux == 3:
		lis= random.sample(dicc["O"], 3)
		lis.append(random.sample(dicc["A"],1)[0])
		lis.append(random.sample(dicc["E"],1)[0])
		dicc_aux["O"]= lis
	elif aux == 4:
		lis= random.sample(dicc["U"], 3)
		lis.append(random.sample(dicc["O"],1)[0])
		lis.append(random.sample(dicc["I"],1)[0])
		dicc_aux["U"]= lis
	return dicc_aux
		
def cargarDiccionario(dicc, ruta= DIRIMAGENES):
	"""carga diccionario con todas las imagenes de la ruta"""
	lista=[]
	for letra in os.listdir(ruta):
		if os.path.isdir(ruta+letra):
			for img in os.listdir(ruta+letra):
				lista.append(img)
			dicc[letra]= lista
			lista=[]
	print (dicc)
	return (dicc)

def inicializarImagenes(dicc, ruta):
	ancho_aux= 0
	alto_aux= 50
	resta_ancho= ancho_ventana
	lista_sprites=[]				#lista de los sprites para poder controlar los eventos
	letra= list(dicc.keys())[0]       # almacena en letra la letra del direc.
	lis= dicc[letra]				
	copy = lis[1:]						# mezclo la lista para que las imagenes incorrctas no vayan siempre al final de la pantalla
	random.shuffle(copy)		
	lis[1:] = copy		                  	#lista con el nombre de cada imagen
	imagen= Imagen((ancho_aux+ancho_ventana/2.4, alto_aux+alto_ventana/1.6), DIRIMAGENES+"Letras"+"/"+letra.lower()+"_letra_"+letra+".png", letra)
	lista_sprites.append(imagen)
	imagen.set_rect(50, 50)        # mod. rectangulo de letra
	for imagen in lis:
		char= imagen[0].upper()                #agarro la primera letra de la imagen, para saber en q directorio buscar
		ruta= DIRIMAGENES+char+"/"+imagen        #modifico directorio pq sino no encuentra la imagen, 
		imagen= Imagen((ancho_aux+ancho_ventana-resta_ancho, alto_aux), ruta, imagen)
		resta_ancho-= 280 
		lista_sprites.append(imagen)
	
	print (lista_sprites)
	return lista_sprites                                         
											
	
	
if __name__ == "__main__":
    cargarDiccionario(diccionario_imagenes)
	
    pantallaInicio()
    main()		

#!/usr/bin/env python
import time, Boton
import sys
import pygame
from pygame.locals import *
from spriteImagen import *
from itertools import cycle
import random
import json
import come_vocales
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
 
colores=[BRIGHTRED,BRIGHTGREEN,BRIGHTBLUE,GREEN]

pygame.init()
pygame.display.set_icon(pygame.image.load("./imagenes/Letras/a_letra_A.png"))
ancho_ventana = 1320
alto_ventana = 720
pygame.display.set_caption("El entrometido")
clock = pygame.time.Clock()
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
BASICFONT_NOMBRE = pygame.font.Font('freesansbold.ttf', 30)
WHITE     = (255, 255, 255)
ANCHOBOTON=150
ALTOBOTON=50
ANCHOCENTROVENTANA= ancho_ventana / 2
ALTOCENTROVENTANA= alto_ventana / 2
FUENTEBOTON=pygame.font.SysFont("comicsansms", 25)
FUENTECONSIGNA = pygame.font.Font("./fuentes/A.C.M.E. Explosive.ttf", 30)
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
botonJuegoNuevo = Boton.boton(RED, BLUE, screen, "JUGAR DE NUEVO", ANCHOCENTROVENTANA - (ANCHOBOTON / 2) - 55,
                            ALTOCENTROVENTANA - 30, ANCHOBOTON + 110 , ALTOBOTON, WHITE, -30, ANCHOCENTROVENTANA,
                            ALTOCENTROVENTANA, FUENTEBOTON)
pygame.mixer.music.set_volume(0.5)
sonidoBien = pygame.mixer.Sound('./sonidos/109662__grunz__success.wav')
sonidoMal = pygame.mixer.Sound('./sonidos/366107__original-sound__error_sound.wav')
pygame.mixer.music.load('./sonidos/432367__a-c-acid__fast-ukulele.mp3')


def main(nombre_usuario):	
	"""loop principal"""
	tacho= Imagen((ANCHOCENTROVENTANA,50),DIRIMAGENES+"tacho.png","tacho")
	tacho.set_rect(200, 1)  
	puntos= 0
	pygame.mixer.music.play(-1, 0.0)
	aux=0 # indice que hace referencia a la letra a usar del diccionario
	screen.fill(random.choice(colores))
	come_vocales.drawMensaje("HOLA "+nombre_usuario+ " !",ANCHOCENTROVENTANA-ANCHOBOTON,ALTOCENTROVENTANA-ALTOBOTON)
	pygame.display.flip()
	time.sleep(1)
	while True and aux!=5:           
		dicc_actual= seleccionDeImagenes(diccionario_imagenes, aux)
		lista_sprites= come_vocales.inicializarImagenes(dicc_actual)
		copy = lista_sprites[1:]
		random.shuffle(copy)
		lista_sprites[1:] = copy
		tupla=tuple(lista_sprites[1:])
		puntos=correrJuego(tacho,random.choice(colores),lista_sprites[0], tupla , puntos)
		time.sleep(0.5)
		screen.fill(random.choice(colores))
		pygame.display.flip()
		if aux!=4:
			come_vocales.drawMensaje("SIGUIENTE NIVEL", ancho_ventana/2.4, alto_ventana/3)
			pygame.display.flip()
		time.sleep(1)
																						
		aux+=1		
	screen.fill(random.choice(colores))	
	come_vocales.drawMensaje("FIN DEL JUEGO",((ancho_ventana/2)-ANCHOBOTON)+20,alto_ventana/3.5)	
	come_vocales.drawMensaje("Tu puntaje fue: "+ str(puntos),(ancho_ventana/2)-ANCHOBOTON,alto_ventana/3)
	datosJson =[
					{
						"nombre": nombre_usuario,
						"puntaje_maximo": puntos
					}
				]	
	come_vocales.modificoArchivoLog(datosJson,"logs_el_entrometido.json")	
	come_vocales.pantallaLeaderboard("logs_el_entrometido.json")
	come_vocales.pantallaInicio(botonJuegoNuevo)													
	pygame.display.flip()																	


def correrJuego(tacho,color,letra,args,puntos):
	"""loop del juego al clickear en iniciar"""
	puntosAnt=0
	correcto=0
	consigna = 'cuales no empiezan con {}?'.format(os.path.splitext(letra.nombre)[0])
	msj = ""
	reproduccionMusica= True
	come_vocales.drawScore(puntos)
	while True and correcto!=3:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				come_vocales.terminate()
			if (event.type == KEYUP):
				if event.key == K_ESCAPE:
					come_vocales.terminate()
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
						puntosAnt = puntos
						tupla=evaluar(tacho,objeto,letra,event,color,puntos,consigna,msj,correcto,True,args)
						puntos=tupla[0]
						correcto=tupla[1]
						if(puntosAnt>puntos):
							msj = 'incorrecto, {} empieza con {}!'.format(os.path.splitext(objeto.nombre)[0],letra.nombre)
						elif(puntosAnt<puntos):
							msj = 'correcto, {} no empieza con {}!'.format(os.path.splitext(objeto.nombre)[0],letra.nombre)		
		screen.fill(color)
		for objeto in args:
			if objeto.arrastra:
				screen.blit(objeto.image, objeto.rect)
		come_vocales.drawScore(puntos)
		come_vocales.drawMensaje(consigna, ancho_ventana-1250, alto_ventana-650)
		come_vocales.drawMensaje(msj, 10, 200)
		screen.blit(tacho.image,tacho.rect)
		screen.blit(letra.image, (1000,100))
		pygame.display.flip()
		clock.tick(60)
	return puntos



def evaluar(tacho,objeto,objeto_destino,event,color,puntos,consigna,msj,correcto,reproduccionMusica, args):
	"""para evaluar si la imagen colisionada corresponde con la letra o no"""
	while not tacho.rect.colliderect(objeto.rect) and pygame.mouse.get_pressed()[0]:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				come_vocales.terminate()
			if (event.type == KEYUP):
				if event.key == K_ESCAPE:
					come_vocales.terminate()
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
		come_vocales.drawScore(puntos)
		come_vocales.drawMensaje(consigna, ancho_ventana-1250, alto_ventana-650)
		screen.blit(tacho.image,tacho.rect)
		screen.blit(objeto_destino.image, (1000,100))
		objeto.handle_event(event,screen)
		screen.blit(objeto.image,objeto.rect)
		pygame.display.flip()
		clock.tick(60)
	if tacho.rect.colliderect(objeto.rect):
		if objeto.arrastra:
			if objeto.nombre[0].upper() != objeto_destino.nombre:
				objeto.arrastra=False
				puntos+= 3
				correcto=correcto+1
			else:
				puntos-= 1
				objeto.rect.topleft=objeto.rect_aux
	return puntos,correcto

def seleccionDeImagenes(dicc, aux):
	"""retorna diccionario cargado con 5 imagenes aleatorias"""
	dicc_aux={}
	if aux == 0:
		lis= random.sample(dicc["A"], 2)
		lis.append(random.sample(dicc["E"],1)[0])
		lis.append(random.sample(dicc["I"],1)[0])
		lis.append(random.sample(dicc["O"],1)[0])
		dicc_aux["A"]= lis
	elif aux == 1:
		lis= random.sample(dicc["E"], 2)
		lis.append(random.sample(dicc["A"],1)[0])
		lis.append(random.sample(dicc["O"],1)[0])
		lis.append(random.sample(dicc["I"],1)[0])
		dicc_aux["E"]= lis
	elif aux == 2:
		lis= random.sample(dicc["I"], 2)
		lis.append(random.sample(dicc["U"],1)[0])
		lis.append(random.sample(dicc["O"],1)[0])
		lis.append(random.sample(dicc["E"],1)[0])
		dicc_aux["I"]= lis
	elif aux == 3:
		lis= random.sample(dicc["O"], 2)
		lis.append(random.sample(dicc["A"],1)[0])
		lis.append(random.sample(dicc["E"],1)[0])
		lis.append(random.sample(dicc["I"],1)[0])
		dicc_aux["O"]= lis
	elif aux == 4:
		lis= random.sample(dicc["U"], 2)
		lis.append(random.sample(dicc["O"],1)[0])
		lis.append(random.sample(dicc["I"],1)[0])
		lis.append(random.sample(dicc["E"],1)[0])
		dicc_aux["U"]= lis
	return dicc_aux


if __name__ == "__main__":
	come_vocales.cargarDiccionario(diccionario_imagenes)
	pygame.mixer.music.play(-1, 0.0)
	pygame.mixer.music.pause()
	screen.fill(random.choice(colores))		
	while True:	
		come_vocales.pantallaInicio(botonInicio)
		nombre_usuario= come_vocales.ingreso_usuario(13)
		main(nombre_usuario)

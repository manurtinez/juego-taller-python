# -*- coding: utf-8 -*-
import time, Boton
import sys
import pygame
from pygame.locals import *
from spriteImagen import *
from itertools import cycle
import random
import json
 
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
pygame.display.set_caption("Conectar")
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
 
def pantallaLeaderboard():
	puntaje_maximo= -1
	nom_punt_max= ""
	archivo= open("logs.json", "r")
	datos= json.load(archivo)
	for partida in datos:
		if partida["puntaje_maximo"] > puntaje_maximo:
			puntaje_maximo= partida["puntaje_maximo"]
			nom_punt_max= partida["nombre"]
	drawMensaje("puntaje mas alto "+str(puntaje_maximo)+", lo hizo "+'"'+nom_punt_max+'"', 290, 50)
 
def drawScore(score):
    scoreSurf = BASICFONT.render('puntos: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (ancho_ventana - 120, 10)
    screen.blit(scoreSurf, scoreRect)
 
 
def modificoArchivoLog(datosJson):
	ok= False
	aux= False             #para saber si el puntaje actual es menor
	archivo= open("logs.json", "r")			#el archivo json debe tener por lo menos 1 dato
	datos_iguales= json.load(archivo)
	datos_viejos= datos_iguales.copy()
	for partida in datos_viejos:
		if partida["nombre"] == datosJson[0]["nombre"]:
			if partida["puntaje_maximo"] < datosJson[0]["puntaje_maximo"]:
				partida["puntaje_maximo"]= datosJson[0]["puntaje_maximo"]
				ok= True
			else: 
				aux= True                #significa que no supero su record
	archivo= open("logs.json", "w")
	if ok:
		json.dump(datos_viejos, archivo)
	elif not(aux):
		datos_viejos.append(datosJson[0])
		json.dump(datos_viejos, archivo)
	else:
		json.dump(datos_iguales, archivo)
	archivo.close()
 
 
 
def main(nombre_usuario):	
	"""loop principal"""
	puntos= 0
	pygame.mixer.music.play(-1, 0.0)
	aux=0 # indice que hace referencia a la letra a usar del diccionario
	screen.fill(random.choice(colores))
	drawMensaje("HOLA "+nombre_usuario+ " !",ANCHOCENTROVENTANA-ANCHOBOTON,ALTOCENTROVENTANA-ALTOBOTON)
	pygame.display.flip()
	time.sleep(1)
	while True and aux!=5:           
		dicc_actual= seleccionDeImagenes(diccionario_imagenes, aux)
		lista_sprites= inicializarImagenes(dicc_actual)
		copy = lista_sprites[1:]
		random.shuffle(copy)
		lista_sprites[1:] = copy
		tupla=tuple(lista_sprites[1:])
		puntos=correrJuego(random.choice(colores),lista_sprites[0], tupla , puntos)
		time.sleep(0.5)
		screen.fill(random.choice(colores))
		pygame.display.flip()
		if aux!=4:
			drawMensaje("SIGUIENTE NIVEL", ancho_ventana/2.4, alto_ventana/3)
			pygame.display.flip()
		time.sleep(1)
																						
		aux+=1		
	screen.fill(random.choice(colores))	
	drawMensaje("FIN DEL JUEGO",((ancho_ventana/2)-ANCHOBOTON)+20,alto_ventana/3.5)	
	drawMensaje("Tu puntaje fue: "+ str(puntos),(ancho_ventana/2)-ANCHOBOTON,alto_ventana/3)
	pantallaLeaderboard()
	datosJson =[
					{
						"nombre": nombre_usuario,
						"puntaje_maximo": puntos
					}
				]	
	modificoArchivoLog(datosJson)	
	pantallaInicio(botonJuegoNuevo)													
	pygame.display.flip()																	


def correrJuego(color,letra,args,puntos):
	"""loop del juego al clickear en iniciar"""
	puntosAnt=0
	correcto=0
	consigna = 'cuales empiezan con {}?'.format(os.path.splitext(letra.nombre)[0])
	msj = ""
	reproduccionMusica= True
	drawScore(puntos)
	while True and correcto!=3:
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
						puntosAnt = puntos
						tupla=evaluar(objeto,letra,event,color,puntos,consigna,msj,correcto,True,args)
						puntos=tupla[0]
						correcto=tupla[1]
						if(puntosAnt>puntos):
							msj = 'incorrecto!! era {}'.format(os.path.splitext(objeto.nombre)[0])
						elif(puntosAnt<puntos):
							msj = 'correcto!! era {}'.format(os.path.splitext(objeto.nombre)[0])		
		screen.fill(color)
		for objeto in args:
			if objeto.arrastra:
				screen.blit(objeto.image, objeto.rect)
		drawScore(puntos)
		drawMensaje(consigna, ancho_ventana-1250, alto_ventana-650)
		drawMensaje(msj, ancho_ventana-500, alto_ventana-650)
		screen.blit(letra.image, letra.rect)
		pygame.display.flip()
		clock.tick(60)
	return puntos


def drawMensaje(msj, x, y):
	"""dibuja el puntaje correspondiente"""
	msjSurf = FUENTECONSIGNA.render(msj, True, BLACK)
	screen.blit(msjSurf, (x, y))

def evaluar(objeto,objeto_destino,event,color,puntos,consigna,msj,correcto,reproduccionMusica, args):
	"""para evaluar si la imagen colisionada corresponde con la letra o no"""
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
		drawMensaje(consigna, ancho_ventana-1250, alto_ventana-650)
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
				correcto=correcto+1
			else:
				puntos-= 1
	return puntos,correcto
	
def pantallaInicio(boton):
    """
    Carga la pantalla inicial del juego
    """
    while True:

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                terminate()
            if (event.type == KEYUP):
                if event.key == K_ESCAPE:
                    terminate()

        boton.mostrarBoton()
        botonSalir.mostrarBoton()

        if boton.toca(getCursorPos()) and botonIzquierdoMouseClickeado():
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
	return (dicc)

def inicializarImagenes(dicc):
	"""retorna una lista con las imagenes del directorio"""
	ancho_aux= 0
	alto_aux= 50
	resta_ancho= ancho_ventana
	lista_sprites=[]	#lista de los sprites para poder controlar los eventos
	letra= list(dicc.keys())[0]     # almacena en letra la letra del direc.
	lis= dicc[letra]				
	copy = lis[:]					# mezclo la lista para que las imagenes incorrctas no vayan siempre al final de la pantalla
	random.shuffle(copy)		
	lis = copy[:]	
	imagen= Imagen((ancho_aux+ancho_ventana/2.4, alto_aux+30), DIRIMAGENES+"Letras"+"/"+letra.lower()+"_letra_"+letra+".png", letra)
	lista_sprites.append(imagen)
	imagen.set_rect(1, 1)        # mod. rectangulo de letra
	alto_aux=500
	for imagen in lis:
		char= imagen[0].upper()                #agarro la primera letra de la imagen, para saber en q directorio buscar
		ruta= DIRIMAGENES+char+"/"+imagen        #modifico directorio pq sino no encuentra la imagen, 
		imagen= Imagen((ancho_aux+ancho_ventana-resta_ancho, alto_aux), ruta, imagen)
		resta_ancho-= 280 
		lista_sprites.append(imagen)
	
	return lista_sprites                                         
											
def ingreso_usuario(largo_max, lower = False, upper = False, title = False):
	"""metodo para ingresar un nombre de usuario al iniciar la partida"""
	FUENTE_NOMBRE_2 = pygame.font.Font("./fuentes/A.C.M.E. Explosive.ttf", 30)
	cadena = ""
	fin = False
	valores_permitidos= [i for i in range(97, 123)] + [i for i in range(48,58)]
	EVENT_PARPADEO = pygame.USEREVENT + 0
	pygame.time.set_timer(EVENT_PARPADEO, 800)
	ciclo_parpadeo = cycle(["_", " "])
	siguiente_parpadeo = next(ciclo_parpadeo)
	while not fin:
		screen.fill(pygame.Color('dark green'))
		pygame.draw.rect(screen, BLUE, (ancho_ventana/2-150, alto_ventana/2-50, 300, 80)) #coordenadas de rectangulo azul
		imprimo_texto(BASICFONT_NOMBRE, ancho_ventana/2-150, alto_ventana/2-100, "TU NOMBRE: ")

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == EVENT_PARPADEO:					#controla parpadeos
				siguiente_parpadeo = next(ciclo_parpadeo)
			
			elif event.type == KEYUP and event.key in valores_permitidos and len(cadena) < largo_max:     #si el caracter cumple
				# caps entry?
				if pygame.key.get_mods() & KMOD_SHIFT or pygame.key.get_mods() & KMOD_CAPS:        #si se ingresa en mayusculas
					cadena += chr(event.key).upper()
				# lowercase entry
				else:														#si es minuscula
					cadena += chr(event.key)
			elif event.type == KEYUP:											
				if event.key == K_BACKSPACE:						
					cadena = cadena[:-1]
				elif event.key == K_SPACE:
					cadena += " "
				elif event.key == K_RETURN:
					fin = True
		if len(cadena) < largo_max:
			imprimo_texto(FUENTE_NOMBRE_2, ancho_ventana/2-145, alto_ventana/2-25, cadena + siguiente_parpadeo)
		else:
			imprimo_texto(FUENTE_NOMBRE_2, ancho_ventana/2-145, alto_ventana/2-25, cadena + siguiente_parpadeo)
		pygame.display.update()
	return cadena


def imprimo_texto(fuente, x, y, texto, color = (255,255,255)):
    texto_imagen = fuente.render(texto, True, color)
    screen.blit(texto_imagen, (x,y))



	
if __name__ == "__main__":
	cargarDiccionario(diccionario_imagenes)
	pygame.mixer.music.play(-1, 0.0)
	pygame.mixer.music.pause()
	screen.fill(random.choice(colores))		
	while True:	
		pantallaInicio(botonInicio)
		nombre_usuario= ingreso_usuario(13)
		main(nombre_usuario)

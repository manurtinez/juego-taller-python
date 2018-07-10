import come_vocales, pygame, el_entrometido, Boton, random, sys, cada_una_en_su_lugar, os
import time, Boton, suite
import sys
import pygame
from pygame.locals import *
from spriteImagen import *
from itertools import cycle
import random
import json

ROJOCLARO = (255,   0,   0)
ROJO = (155,   0,   0)
VERDECLARO = (  0, 255,   0)
VERDE = (  0, 155,   0)
AZULCLARO = (  0,   0, 255)
AZUL = (  0,   0, 155)
BLANCO = (255, 255, 255)
NEGRO= (0, 0, 0)


colores=[ROJOCLARO,VERDECLARO,AZULCLARO,VERDE]
pygame.init()
pygame.display.set_icon(pygame.image.load("./imagenes/Letras/a_letra_A.png"))

ancho_ventana = 1320
alto_ventana = 720

pygame.display.set_caption("Conectar")

clock = pygame.time.Clock()

FUENTE_BASICA = pygame.font.Font('freesansbold.ttf', 18)
FUENTE_BASICA_NOMBRE = pygame.font.Font('freesansbold.ttf', 30)

ANCHOBOTON=150
ALTOBOTON=50
ANCHOCENTROVENTANA= ancho_ventana / 2
ALTOCENTROVENTANA= alto_ventana / 2


FUENTEBOTON=pygame.font.SysFont("comicsansms", 25)
FUENTECONSIGNA = pygame.font.Font("./fuentes/A.C.M.E. Explosive.ttf", 30)
screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
DIRIMAGENES= "./imagenes/"

botonComeVocales = Boton.boton(ROJO, AZUL, screen, "Come Vocales", ANCHOCENTROVENTANA - (ANCHOBOTON / 2) - 20,
                            ALTOCENTROVENTANA - 30, ANCHOBOTON + 50, ALTOBOTON, BLANCO, -30, ANCHOCENTROVENTANA,
                            ALTOCENTROVENTANA, FUENTEBOTON)

botonEntrometido = Boton.boton(ROJO, AZUL, screen, "El Entrometido", ANCHOCENTROVENTANA - (ANCHOBOTON / 2) - 20,
                            ALTOCENTROVENTANA - 100, ANCHOBOTON + 50, ALTOBOTON, BLANCO, -100, ANCHOCENTROVENTANA,
                            ALTOCENTROVENTANA, FUENTEBOTON)

botonSalir = Boton.boton(ROJO, AZUL, screen, "SALIR", ANCHOCENTROVENTANA - (ANCHOBOTON / 2),
                           ALTOCENTROVENTANA + 50, ANCHOBOTON, ALTOBOTON, BLANCO, 50, ANCHOCENTROVENTANA,
                           ALTOCENTROVENTANA, FUENTEBOTON)
botonJuegoNuevo = Boton.boton(ROJO, AZUL, screen, "JUGAR DE NUEVO", ANCHOCENTROVENTANA - (ANCHOBOTON / 2) - 55,
                            ALTOCENTROVENTANA - 30, ANCHOBOTON + 110 , ALTOBOTON, BLANCO, -30, ANCHOCENTROVENTANA,
                            ALTOCENTROVENTANA, FUENTEBOTON)

botonCadaUnaEnSuLugar = Boton.boton(ROJO, AZUL, screen, "Cada uno en su lugar", ANCHOCENTROVENTANA - (ANCHOBOTON / 2) - 55,
                            ALTOCENTROVENTANA - 170, ANCHOBOTON + 110 , ALTOBOTON, BLANCO, -170, ANCHOCENTROVENTANA,
                            ALTOCENTROVENTANA, FUENTEBOTON)


def pantallaLeaderboard(nombre):
	"""muestra el puntaje maximo y quien lo realizo en pantalla""" 
	puntaje_maximo= -1
	nom_punt_max= ""
	archivo= open(nombre, "r")
	datos= json.load(archivo)
	for partida in datos:
		if partida["puntaje_maximo"] > puntaje_maximo:
			puntaje_maximo= partida["puntaje_maximo"]
			nom_punt_max= partida["nombre"]
	drawMensaje("puntaje mas alto "+str(puntaje_maximo)+", lo hizo "+'"'+nom_punt_max+'"', 290, 50)


def modificoArchivoLog(datosJson,nombre):
	"""actualiza o crea el archivo log del juego correspondiente"""
	try:
		ok= False
		aux= False    			         #para saber si el puntaje actual es menor
		archivo= open(nombre,"r")			#el archivo json debe tener por lo menos 1 dato
		datos_iguales= json.load(archivo)
		datos_viejos= datos_iguales.copy()
		for partida in datos_viejos:
			if partida["nombre"] == datosJson[0]["nombre"]:
				if partida["puntaje_maximo"] < datosJson[0]["puntaje_maximo"]:
					partida["puntaje_maximo"]= datosJson[0]["puntaje_maximo"]
					ok= True
				else: 
					aux= True                #significa que no supero su record
		archivo= open(nombre, "w")
		if ok:
			json.dump(datos_viejos, archivo)
		elif not(aux):
			datos_viejos.append(datosJson[0])
			json.dump(datos_viejos, archivo)
		else:
			json.dump(datos_iguales, archivo)
		archivo.close()
	except:
		archivo= open(nombre, "w")
		json.dump(datosJson,archivo)
		archivo.close()

def pantallaInicio():
    """Carga la pantalla inicial del juego"""
    screen.fill(random.choice(colores))
    drawMensaje("elegi un juego!", 500, 50)
    pygame.mixer.music.pause()	
    while True:

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                terminate()
            if (event.type == KEYUP):
                if event.key == K_ESCAPE:
                    terminate()

        botonComeVocales.mostrarBoton()
        botonEntrometido.mostrarBoton()
        botonCadaUnaEnSuLugar.mostrarBoton()
        botonSalir.mostrarBoton()

        if botonComeVocales.toca(getCursorPos()) and botonIzquierdoMouseClickeado():
            come_vocales.main()
        if botonEntrometido.toca(getCursorPos()) and botonIzquierdoMouseClickeado():
        	el_entrometido.main()
        if botonCadaUnaEnSuLugar.toca(getCursorPos()) and botonIzquierdoMouseClickeado():
        	cada_una_en_su_lugar.main()
        elif botonSalir.toca(getCursorPos()) and botonIzquierdoMouseClickeado():
            terminate()

        pygame.display.update()

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

def botonIzquierdoMouseClickeado():
	"""retorna si el boton izquierdo del mouse esta presionado"""
	return pygame.mouse.get_pressed()[0]
		
def getCursorPos():
	"""retorna la posicion del mouse"""
	return pygame.mouse.get_pos()

def evaluarTacho(tacho,objeto,objeto_destino,event,color,puntos,consigna,msj,correcto,reproduccionMusica, args):
	"""	evalua la condicion del tacho despues de arastrar el objeto"""
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
		drawScore(puntos)
		drawMensaje(consigna, ancho_ventana-1250, alto_ventana-600)
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

def evaluar(objeto,objeto_destino,event,color,puntos,consigna,msj,correcto,reproduccionMusica, args):
	"""evalua si la imagen colisionada corresponde con la letra o no"""
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
		drawMensaje("esc: volver al menu, m: pausar musica", ancho_ventana-1280, alto_ventana-700)
		drawMensaje(consigna, ancho_ventana-1250, alto_ventana-600)
		screen.blit(objeto_destino.image, objeto_destino.rect)
		objeto.handle_event(event,screen)
		screen.blit(objeto.image,objeto.rect)
		pygame.display.flip()
		clock.tick(60)
	if objeto_destino.rect.colliderect(objeto.rect):
		if objeto.arrastra:
			if objeto.nombre[0].upper() == objeto_destino.nombre:
				objeto.arrastra=False
				puntos+= 3
				correcto=correcto+1
			else:
				puntos-= 1
				objeto.rect.topleft=objeto.rect_aux
	return puntos,correcto

def drawMensaje(msj, x, y):
	"""dibuja el puntaje correspondiente"""
	msjSurf = FUENTECONSIGNA.render(msj, True, NEGRO)
	screen.blit(msjSurf, (x, y))

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
		screen.fill(VERDE)
		pygame.draw.rect(screen, AZUL, (ancho_ventana/2-150, alto_ventana/2-50, 300, 80)) #coordenadas de rectangulo azul
		imprimo_texto(FUENTE_BASICA_NOMBRE, ancho_ventana/2-150, alto_ventana/2-100, "TU NOMBRE: ")

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
	"""imprime texto en pantalla dada ua poicion determinada"""
	texto_imagen = fuente.render(texto, True, color)
	screen.blit(texto_imagen, (x,y))

def drawScore(score):
    """muestra y actualiza la puntuacion del juego"""
    scoreSurf = FUENTE_BASICA.render('puntos: {}'.format(score), True, BLANCO)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (ancho_ventana - 120, 10)
    screen.blit(scoreSurf, scoreRect)

def inicializarImagenes(dicc):
	"""iniciaiza todos los sprites en pantalla y retorna una lista de sprites"""
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
	imagen.set_rect(200, 1)        # mod. rectangulo de letra
	alto_aux=500
	for imagen in lis:
		char= imagen[0].upper()                #agarro la primera letra de la imagen, para saber en q directorio buscar
		ruta= DIRIMAGENES+char+"/"+imagen        #modifico directorio pq sino no encuentra la imagen, 
		imagen= Imagen((ancho_aux+ancho_ventana-resta_ancho, alto_aux), ruta, imagen)
		resta_ancho-= 280 
		lista_sprites.append(imagen)
	
	return lista_sprites

def inicializarImagenesCadaUno(dicc):
	"""retorna una lista con las imagenes del directorio"""
	ancho_aux= 300
	alto_aux= 50
	resta_ancho= ancho_ventana
	lista_sprites=[]	#lista de los sprites para poder controlar los eventos
	letra= list(dicc.keys())[0]     # almacena en letra la letra del direc.
	lis= dicc[letra]				
	alto_aux=300
	for imagen in lis:
		char= imagen[0].upper()                #agarro la primera letra de la imagen, para saber en q directorio buscar
		ruta= DIRIMAGENES+char+"/"+imagen        #modifico directorio pq sino no encuentra la imagen, 
		imagen= Imagen((ancho_aux+ancho_ventana-resta_ancho, alto_aux), ruta, imagen)
		resta_ancho-= 280 
		lista_sprites.append(imagen)
	return lista_sprites

def terminate():
	"""finaliza ejecucion y cierra el programa"""
	pygame.quit()
	sys.exit()

if __name__ == "__main__":
	screen.fill(random.choice(colores))
	pygame.mixer.music.play(-1, 0.0)
	pantallaInicio()

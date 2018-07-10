import come_vocales, pygame, el_entrometido, Boton, random, sys, cada_una_en_su_lugar
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

botonComeVocales = Boton.boton(RED, BLUE, screen, "Come Vocales", ANCHOCENTROVENTANA - (ANCHOBOTON / 2) - 20,
                            ALTOCENTROVENTANA - 30, ANCHOBOTON + 50, ALTOBOTON, WHITE, -30, ANCHOCENTROVENTANA,
                            ALTOCENTROVENTANA, FUENTEBOTON)

botonEntrometido = Boton.boton(RED, BLUE, screen, "El Entrometido", ANCHOCENTROVENTANA - (ANCHOBOTON / 2) - 20,
                            ALTOCENTROVENTANA - 100, ANCHOBOTON + 50, ALTOBOTON, WHITE, -100, ANCHOCENTROVENTANA,
                            ALTOCENTROVENTANA, FUENTEBOTON)

botonSalir = Boton.boton(RED, BLUE, screen, "SALIR", ANCHOCENTROVENTANA - (ANCHOBOTON / 2),
                           ALTOCENTROVENTANA + 50, ANCHOBOTON, ALTOBOTON, WHITE, 50, ANCHOCENTROVENTANA,
                           ALTOCENTROVENTANA, FUENTEBOTON)
botonJuegoNuevo = Boton.boton(RED, BLUE, screen, "JUGAR DE NUEVO", ANCHOCENTROVENTANA - (ANCHOBOTON / 2) - 55,
                            ALTOCENTROVENTANA - 30, ANCHOBOTON + 110 , ALTOBOTON, WHITE, -30, ANCHOCENTROVENTANA,
                            ALTOCENTROVENTANA, FUENTEBOTON)

botonCadaUnaEnSuLugar = Boton.boton(RED, BLUE, screen, "Cada uno en su lugar", ANCHOCENTROVENTANA - (ANCHOBOTON / 2) - 55,
                            ALTOCENTROVENTANA - 170, ANCHOBOTON + 110 , ALTOBOTON, WHITE, -170, ANCHOCENTROVENTANA,
                            ALTOCENTROVENTANA, FUENTEBOTON)


def pantallaInicio():
    """
    Carga la pantalla inicial del juego
    """
    screen.fill(random.choice(colores))
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

        if botonComeVocales.toca(come_vocales.getCursorPos()) and come_vocales.botonIzquierdoMouseClickeado():
            come_vocales.main()
        if botonEntrometido.toca(come_vocales.getCursorPos()) and come_vocales.botonIzquierdoMouseClickeado():
        	el_entrometido.main()
        if botonCadaUnaEnSuLugar.toca(come_vocales.getCursorPos()) and come_vocales.botonIzquierdoMouseClickeado():
        	cada_una_en_su_lugar.main()
        elif botonSalir.toca(come_vocales.getCursorPos()) and come_vocales.botonIzquierdoMouseClickeado():
            terminate()

        pygame.display.update()

def main():
	pantallaInicio()

def terminate():
	pygame.quit()
	sys.exit()

if __name__ == "__main__":
	screen.fill(random.choice(colores))
	pygame.mixer.music.play(-1, 0.0)
	main()
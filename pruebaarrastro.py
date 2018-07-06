# -*- coding: utf-8 -*-
import time
import sys
import pygame
from pygame.locals import *
from spriteImagen import *
 
 
 
pygame.init()
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
WHITE     = (255, 255, 255)
 
 
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
 
ancho_ventana = 900
alto_ventana = 900
screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Tutorial sprites Piensa 3D")
clock = pygame.time.Clock()
 
 
 
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
                pygame.quit()
                sys.exit()
            if (event.type == KEYUP):
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
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
                print("player2")
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
                else:
                    if player.toca(x,y):
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
       
 
 
if __name__ == "__main__":
    main()
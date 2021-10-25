#importar librería
import pygame, sys

from pygame import color
#inicializar la librería
pygame.init()

#Colores
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

#VENTANA
#tamaño
size = (800, 500)
#crear ventana
screen = pygame.display.set_mode(size)
#el reloj controla los FPS
clock = pygame.time.Clock()

#coordenadas del cuadrado
cord_x = 400
cord_y = 200

#velocidad del cuadrado
speed_x = 3
speed_y = 3

#un juego es un bucle infinito
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #para que el cuadrado no se salga de la pantalla
    if (cord_x>720 or cord_x<0):
        speed_x*=-1
    if (cord_y>420 or cord_y<0):
        speed_y*=-1
    
    #animacion del cuadrado
    cord_x += speed_x
    cord_y += speed_y
    
    #pintar el fondo  
    screen.fill(WHITE)

    ##INICIO ZONA DE DIBUJO
    
    #pygame.draw.line(screen,GREEN,[0,100],[100,100],5)
    #pygame.draw.rect(screen,BLACK, (100,100,80,80))
    #pygame.draw.circle(screen,RED,(115,200),30)
    #for x in range(100,700,100):
        #pygame.draw.rect(screen,BLACK,(x,230,50,50))
        #pygame.draw.line(screen,GREEN,[x,0],[x,100],2)

    #Una casa bien fea pero hecha por mi XD
    # pygame.draw.line(screen,RED,(100,100),(200,100),3)
    # pygame.draw.line(screen,RED,(100,100),(100,200),3)
    # pygame.draw.line(screen,RED,(200,100),(200,200),3)
    # pygame.draw.line(screen,RED,(100,200),(200,200),3)
    # pygame.draw.rect(screen,BLACK,(100,100,100,100))
    # pygame.draw.rect(screen,GREEN,(135,170,30,30))
    # pygame.draw.rect(screen,WHITE,(110,120,30,30))
    # pygame.draw.rect(screen,WHITE,(160,120,30,30))
    # pygame.draw.line(screen,RED,(100,100),(150,50),3)
    # pygame.draw.line(screen,RED,(200,100),(150,50),3)

    #el rectangulo que se mueve
    pygame.draw.rect(screen,RED,(cord_x,cord_y,80,80))


    ##FIN ZONA DE DIBUJO

    #método para actualizar pantalla
    pygame.display.flip()
    #para controlar los fps
    clock.tick(60)
 
    #En resumen
    #1 lógica del juego 
    #2 pintar la pantalla de blanco
    #3 zona de dibujo
import pygame
pygame.init()

#colores
black = (0,0,0)
white = (255,255,255)

#tamaño de pantalla
screen_size = (800,600)

#tamaño de las paletas
player_width = 15
player_height = 90

#coordenadas y velocidad p1
player1_x_coord = 50
player1_y_coord = 300 - 45
player1_y_speed = 0

#coordenadas y velocidad p2
player2_x_coord = 750 - player_width
player2_y_coord = 300 - 45
player2_y_speed = 0

#coordenadas y velocidad de la pelota
pelota_x = 400
pelota_y = 300
pelota_speed_x = 3
pelota_speed_y = 3

#puntajes
player1_puntaje = 0
player2_puntaje = 0


#texto
#título
fuente = pygame.font.SysFont("consolas", 30)
texto = fuente.render("PONG", True, white) #texto, bordes suavizados, color
#jugadores
fuente2 = pygame.font.SysFont("consolas", 15)


#desplegar pantalla e iniciar reloj
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        #eventos de teclado
        if event.type == pygame.KEYDOWN:
            #jugador 1
            if event.key == pygame.K_w:
                player1_y_speed = -3
            if event.key == pygame.K_s:
                player1_y_speed = 3
            #jugador 2
            if event.key == pygame.K_UP:
                player2_y_speed = -3
            if event.key == pygame.K_DOWN:
                player2_y_speed = 3
        
        if event.type == pygame.KEYUP:
            #jugador 1
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0
            #jugador 2
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0
            
    #rebote de la pelota con las paredes de arriba y abajo
    if pelota_y > 590 or pelota_y < 10:
        pelota_speed_y *= -1
    
    #revisar si la pelota se sale por los lados
    #izquierda
    if pelota_x < 0:
        #centrar de nuevo
        pelota_x = 400
        pelota_y = 300
        #invertir dirección
        pelota_speed_x *= -1
        pelota_speed_y *= -1
        #puntaje
        player2_puntaje +=1

    #derecha
    if pelota_x > 800:
        #centrar de nuevo
        pelota_x = 400
        pelota_y = 300
        #invertir dirección
        pelota_speed_x *= -1
        pelota_speed_y *= -1
        #puntaje
        player1_puntaje +=1


    #modifica las coordenadas para mover jugadores y pelota
    player1_y_coord += player1_y_speed
    player2_y_coord += player2_y_speed

    #movimiento de la pelota 
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y

    #fondo negro
    screen.fill(black)

    ######ZONA DE DIBUJO######
    #score a texto
    pat1 = "P1: " + repr(player1_puntaje)
    pat2 = "P2: " + repr(player2_puntaje)
    #renderizar texto
    texto_score1 = fuente.render(pat1, False, white) #texto, bordes suavizados, color
    texto_score2 = fuente.render(pat2, False, white) #texto, bordes suavizados, color
    #desplegar texto
    screen.blit(texto, (350,10))
    screen.blit(texto_score1 , (10,10))
    screen.blit(texto_score2, (700,10))

    #dibujar paletas y pelota
    jugador1 = pygame.draw.rect(screen, white, (player1_x_coord,player1_y_coord,player_width,player_height))
    jugador2 = pygame.draw.rect(screen, white, (player2_x_coord,player2_y_coord,player_width,player_height))
    pelota = pygame.draw.circle(screen, white, (pelota_x, pelota_y),10)


    ######FIN ZONA DE DIBUJO######

    #colisiones
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_speed_x *= -1

    pygame.display.flip()
    clock.tick(60) #60FPS

pygame.quit()          
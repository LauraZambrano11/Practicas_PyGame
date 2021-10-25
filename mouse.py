import pygame, sys
pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

size = (800,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#visibilidad del mouse: 
#0 para no ver el puntero 
#1 para ver el puntero
pygame.mouse.set_visible(0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #posición del mouse
    mouse_pos = pygame.mouse.get_pos()
    #print(mouse_pos)
    x = mouse_pos[0]
    y = mouse_pos[1]

    screen.fill(white)

    pygame.draw.rect(screen,red,(x,y,100,100))

    pygame.display.flip()
    clock.tick(60)
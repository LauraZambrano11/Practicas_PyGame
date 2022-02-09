import pygame
pygame.init()

size = (620,465)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

done = False

#carga de imágenes
backgorund = pygame.image.load("lobos.jpg").convert()
ship = pygame.image.load("nave.png").convert()
ship.set_colorkey([0,0,0]) #remover el fondo negro

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #obtener posicion del mouse
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]

    #usar la imágen como fondo
    screen.blit(backgorund, [0,0])
    screen.blit(ship, [x,y])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


import pygame
pygame.init()

size = (620,465)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

done = False

#carga de la imágen
backgorund = pygame.image.load("lobos.jpg").convert()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #usar la imágen como fondo
    screen.blit(backgorund, [0,0])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


#Un comentario posiblemente útil
#Gente, un consejo, al cargar las imagenes importen os y escriban:

#player = pygame.image.load(os.path.join('carpeta_de_los_archivos", "imagen"))

#asi tendran un codigo limpio y menos posibles problemas al cargar la imagen, además no hay necesidad de remover el fondo
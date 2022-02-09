import pygame, random
pygame.init()

white = (255,255,255)
black = (0,0,0)

#métodos para los meteoros
class Meteor (pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("stone.jpg").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y +=1
        if self.rect.y > 700:
            self.rect.y = -10
            self.rect.x = random.randrange(900)

#métodos para el jugador
class Player (pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("nave.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()

    def update(self):
        #obtener posicion del mouse
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0]
        player.rect.y = mouse_pos[1]

size = (900,700)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
done = False
score = 0

#listas para almacenar todas las instancias de meteoro
meteor_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

#instancias de los mteoros
for i in range(50):
    meteor = Meteor()
    meteor.rect.x = random.randrange(900)
    meteor.rect.y = random.randrange(700)
    #agregar elementos a las listas
    meteor_list.add(meteor)
    all_sprite_list.add(meteor)

#instancia de jugador
player = Player()
all_sprite_list.add(player)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    all_sprite_list.update()
    #colisiones y eliminación de objetos
    meteor_hit_list = pygame.sprite.spritecollide(player, meteor_list, True)

    #puntaje
    for meteor in meteor_hit_list:
        score +=1
        print(score)

    screen.fill(white)
    all_sprite_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


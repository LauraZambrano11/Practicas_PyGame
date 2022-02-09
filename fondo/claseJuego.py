import pygame, random

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
BLACK = (0,0,0)
WHITE = (255,255,255)

#métodos para los meteoros
class Meteor (pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("stone.jpg").convert()
        self.image.set_colorkey(WHITE)
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
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

    def update(self):
        #obtener posicion del mouse
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = mouse_pos[0]
        self.rect.y = mouse_pos[1]

#clase Juego 
class Game(object): 
    def __init__(self): 
        self.game_over = False
        self.score = 0
        self.meteor_list = pygame.sprite.Group()
        self.all_sprite_list = pygame.sprite.Group()

        #instancias de los mteoros
        for i in range(50):
            meteor = Meteor()
            meteor.rect.x = random.randrange(SCREEN_WIDTH)
            meteor.rect.y = random.randrange(SCREEN_HEIGHT)
            #agregar elementos a las listas
            self.meteor_list.add(meteor)
            self.all_sprite_list.add(meteor)

        #instancia de jugador
        self.player = Player()
        self.all_sprite_list.add(self.player)

    def proccess_events(self): #eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            #cuando esté en game over se reinicia el juego con este evento
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
        
        return False

    def run_logic(self): #lógica del juego

        if not self.game_over:
            self.all_sprite_list.update()
            #colisiones y eliminación de objetos
            meteor_hit_list = pygame.sprite.spritecollide(self.player, self.meteor_list, True)

            for meteor in meteor_hit_list:
                self.score +=1
                print(self.score)

            #si ya no quedan meteoros se termina
            if len(self.meteor_list) == 0:
                self.game_over = True

    def display_frame(self, screen): #pantalla
        screen.fill(WHITE)

        if self.game_over:
            font = pygame.font.SysFont("console", 25) #fuente
            text = font.render("Game Over, Click To Continue", True, BLACK) #texto
            #ubicación
            center_x = (SCREEN_WIDTH // 2 ) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y]) #despliegue en pantalla
        if not self.game_over:
            self.all_sprite_list.draw(screen)
        pygame.display.flip() 

def main():
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH , SCREEN_HEIGHT])
    done = False
    clock = pygame.time.Clock()
    game = Game()

    while not done:
        done = game.proccess_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(60)
    
    pygame.quit

#estas dos líneas permiten ejecutar la función principal main
if __name__ == "__main__":
    main()  

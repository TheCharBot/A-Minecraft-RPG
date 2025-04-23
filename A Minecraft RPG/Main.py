import pygame
import time
import Maps
#import mapRendering

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("A Minecraft RPG")
running = True
clock = pygame.time.Clock()
x = 0

overworld = Maps.overworld1()
def map(x, y, map):
    for item in map:
        if item == 1:
            mapObject = pygame.image.load("textures\\blocks\\grass\\grassside.png")
            display_surface.blit(mapObject, (x, y))
            x += 50
        elif item == 2:
            mapObject = pygame.image.load("textures\\blocks\\grass\\grasstop.png")
            display_surface.blit(mapObject, (x, y))
            x += 50
        elif item == 3:
            mapObject = pygame.image.load("textures\\blocks\\cobblestone\\cobblestone.png")
            display_surface.blit(mapObject, (x, y))
            x += 50
        if x == 500 or x >= 500:
            y += 50
            x = 0
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 200
        self.x = 0
        self.y = 0
        self.direction = pygame.Vector2()
        self.image = pygame.image.load("textures\\player\\playerdown\\playerdown1.png").convert_alpha()
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        # Calculate vertical direction
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = (
            self.direction.normalize() if self.direction else self.direction
        )
        self.rect.x += self.direction.x * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt
        ###  REWORK  ###
        #self.direction.x = int(keys[pygame.K_a]) - int(keys[pygame.K_d])
        #self.direction.y = int(keys[pygame.K_w]) - int(keys[pygame.K_s])
       

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

while running:
    dt = clock.tick(20) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update(dt)
    
    display_surface.fill("black")
    
    map(0,0,overworld)
    all_sprites.draw(display_surface)
    
    pygame.display.update()
pygame.quit()

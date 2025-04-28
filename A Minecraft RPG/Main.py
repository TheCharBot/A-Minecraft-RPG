import pygame
import Maps


# Setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 500, 567
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("A Minecraft RPG")

# Object creation
running = True
clock = pygame.time.Clock()
x = 0
animationState = 1
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
        self.facing = "idle"
        self.speed = 200
        self.x = 0
        self.y = 0
        self.direction = pygame.Vector2()
        self.image = pygame.image.load("textures\\player\\playerdown\\playerdown1.png").convert_alpha()
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
    def update(self, dt):
        # Key sensing
        keys = pygame.key.get_pressed()
        
        # Key and movement calculation
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

        # Animation and rotational calculations
        if self.direction.magnitude() > 0: 
            if self.direction.x > 0:
                self.facing = "right"
            elif self.direction.x < 0:
                self.facing = "left"
            elif self.direction.y < 0:
                self.facing = "up"
            elif self.direction.y > 0:
                self.facing = "down"
            
        else: 
            self.facing = "idle"
        # Normalizing diagonal movemnts with the vector
        self.direction = (
            self.direction.normalize() if self.direction else self.direction
        )
        
        # Recalculating psition and movement
        self.rect.x += self.direction.x * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt

        global wall_touched
        wall_touched = "none"
        if self.rect.x < 0:
            self.rect.x = 0
            wall_touched = "left"
        elif self.rect.x > 450:
            self.rect.x = 450
            wall_touched = "right"
        if self.rect.y < 0:
            self.rect.y = 0
            wall_touched = "top"
        elif self.rect.y > 450:
            self.rect.y = 450
            wall_touched = "bottom"
        
        
    def animate(self):
        
        if is_even(animationState):
            if self.facing == "right":
                self.image = pygame.image.load("textures\\player\\playerright\\playerright1.png").convert_alpha()
            elif self.facing == "left":
                self.image = pygame.image.load("textures\\player\\playerleft\\playerleft1.png").convert_alpha()
            elif self.facing == "up":
                self.image = pygame.image.load("textures\\player\\playerup\\playerup1.png").convert_alpha()
            elif self.facing == "down":
                self.image = pygame.image.load("textures\\player\\playerdown\\playerdown1.png").convert_alpha()
            else:
                self.image = pygame.image.load("textures\\player\\idle\\idle.png").convert_alpha()
        else:
            if self.facing == "right":
                self.image = pygame.image.load("textures\\player\\playerright\\playerright2.png").convert_alpha()
            elif self.facing == "left":
                self.image = pygame.image.load("textures\\player\\playerleft\\playerleft2.png").convert_alpha()
            elif self.facing == "up":
                self.image = pygame.image.load("textures\\player\\playerup\\playerup2.png").convert_alpha()
            elif self.facing == "down":
                self.image = pygame.image.load("textures\\player\\playerdown\\playerdown2.png").convert_alpha()
            else:
                self.image = pygame.image.load("textures\\player\\idle\\idle.png").convert_alpha()
        
class Hotbar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        
        self.x = 0
        self.y = 480
        self.direction = pygame.Vector2()
        self.image = pygame.image.load("textures\\inventory\\hotbar.png")
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT-33))


####### FIGURE OUT DICTIONARIES ######

my_info = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer"
}

def is_even(number):
  return number % 2 == 0
def check_for_input():
    keys = pygame.key.get_pressed()
    if keys == int(keys[pygame.K_RIGHT]):
        player.attack()



    

        
TASK_ONE_TRIGGER = pygame.USEREVENT + 1
pygame.time.set_timer(TASK_ONE_TRIGGER, 200)

all_sprites = pygame.sprite.Group()
player = Player()
hotbar = Hotbar()
all_sprites.add(hotbar)
all_sprites.add(player)

while running:
    dt = clock.tick(20) / 1000
    keys = pygame.key.get_pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == TASK_ONE_TRIGGER:
            animationState +=1
    
    
    all_sprites.update(dt)
    
    display_surface.fill("black")
    
    map(0,0,overworld)
    player.animate()
    all_sprites.draw(display_surface)
    
    pygame.display.update()
pygame.quit()

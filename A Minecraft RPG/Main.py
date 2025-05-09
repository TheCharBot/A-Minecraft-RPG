import pygame
import Maps
import Items
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
current_map = Maps.a1()
collision_rects = []
def map(map):
    x = 0
    y = 0
    for item in map:
        if item == 1:
            mapObject = pygame.image.load("textures\\blocks\\grass\\grassside.png")
            collision_rects.append(pygame.Rect(x, y, 50, 50))
        elif item == 2:
            mapObject = pygame.image.load("textures\\blocks\\grass\\grasstop.png")
        elif item == 3:
            mapObject = pygame.image.load("textures\\blocks\\cobblestone\\cobblestone.png")
        elif item == 4:
            mapObject = pygame.image.load("textures\\blocks\\water\\water.png")
            collision_rects.append(pygame.Rect(x, y, 50, 50))
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
        # Variable creation and assignment
        keys = pygame.key.get_pressed()
        self.colliding = False
        
        # Saving current location for collisions
        if self.colliding == False:
            playerrectxSAVE = self.rect.x
            playerrectySAVE = self.rect.y  
        
        # Key and movement calculation
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

        # Normalizing diagonal movements with the vector
        self.direction = (self.direction.normalize() if self.direction else self.direction)

        # Recalculating position and movement
        self.rect.x += self.direction.x * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt

        ### Direction Calculation ###

        # Checking which way the magnitude reports the player is going
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

        ### Collisions ###
        # Checking for collisions, if true, revert player to a previous position
        for rect in collision_rects:
            if self.rect.colliderect(rect):
                self.rect.x = playerrectxSAVE
                self.rect.y = playerrectySAVE
                self.colliding = True
                break
        
        ### Checking which wall was touched ###
        global wall_touched
        wall_touched = "none"

        # Checking for left wall
        if self.rect.x < 0:
            self.rect.x = 0
            wall_touched = "left"
        
        # Checking for right wall
        elif self.rect.x > 450:
            self.rect.x = 450
            wall_touched = "right"
        
        # Checking for top wall
        if self.rect.y < 0:
            self.rect.y = 0
            wall_touched = "top"
        
        # Checking for bottom wall
        elif self.rect.y > 450:
            self.rect.y = 450
            wall_touched = "bottom"

        ### Attacking and Placing ###

        # Checking for X key getting pressed
        if pygame.key.get_just_pressed()[pygame.K_x]:
            print("X key just pressed")
        
        # Checking for Z key getting pressed
        if pygame.key.get_just_pressed()[pygame.K_z]:
            print("Z key just pressed")
        
        # Checking for F key getting pressed (to switch the off hand item with the X or Z key items)
        if pygame.key.get_just_pressed()[pygame.K_f]:
            print("F key just pressed")  

    # Animation function
    def animate(self):
        # Animation State Check
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
        # If the animation state is odd, do a different animation
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
class XItem(pygame.sprite.Sprite):
    # Class for the item in the X slot (assigned for the X key)
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
class Hotbar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 480
        self.direction = pygame.Vector2()
        self.image = pygame.image.load("textures\\inventory\\hotbar.png")
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT-33))

# Even Number Finder
def is_even(number):
  return number % 2 == 0

# Animation Stage Event
ANIMATION_STATE_TRIGGER = pygame.USEREVENT + 1
pygame.time.set_timer(ANIMATION_STATE_TRIGGER, 200)

# Assignment of Sprite Classes to Sprite Group
all_sprites = pygame.sprite.Group()
player = Player()
hotbar = Hotbar()
all_sprites.add(hotbar)
all_sprites.add(player)

# Game Loop
while running:
    dt = clock.tick(20) / 1000
    
    # Checking for Quit Event and Animation Stage Shift Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == ANIMATION_STATE_TRIGGER:
            animationState +=1
    
    # Update sprites
    all_sprites.update(dt)

    # Animate Player
    player.animate()

    # Refresh On-Screen Colors
    display_surface.fill("black")

    # Draw the map
    map(current_map)

    # Drawing Player and Hotbar
    all_sprites.draw(display_surface)

    # Updating Display
    pygame.display.update()
pygame.quit()

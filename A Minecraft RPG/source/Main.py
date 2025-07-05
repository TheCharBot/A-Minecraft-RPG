import pygame
#import os
import source.maps as maps
import source.images as images

# Setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 867
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display_icon = pygame.image.load(images.icon)
pygame.display.set_icon(display_icon)
pygame.display.set_caption("A Minecraft RPG")

# Object creation
running = True
clock = pygame.time.Clock()
animationState = 1
collision_rects = []
warp_rects = []
warp_rect_names = []
entity_list = []
interact_rects = []

class XItem(pygame.sprite.Sprite):
    # Class for the item in the X slot (assigned for the X key)
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Hotbar(pygame.sprite.Sprite):
    # Class for the Hotbar Sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 480
        self.direction = pygame.Vector2()
        self.image = pygame.image.load(images.hotbar_image)
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT-33))
    
# Even Number Finder
def is_even(number):
  return number % 2 == 0

# Animation Stage Event
ANIMATION_STATE_TRIGGER = pygame.USEREVENT + 1
pygame.time.set_timer(ANIMATION_STATE_TRIGGER, 200)

# import of sprite classes
import source.entities as entities
npc = entities.Villager()
import source.playerClass as playerClass
player = playerClass.Player()
import source.mapClass as mapClass
map = mapClass.Map()
# Assignment of Sprite Classes to Sprite Group
all_sprites = pygame.sprite.Group()

hotbar = Hotbar()



all_sprites.add(hotbar)
all_sprites.add(player)


# Game Loop
#current_map = map_check()
while running:
    dt = clock.tick(30) / 1000
    
    # Checking for Quit Event and Animation Stage Shift Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == ANIMATION_STATE_TRIGGER:
            animationState +=1
            
    mapCoords = player.map_movement()
    # Update sprites
    
    all_sprites.update(dt)
    
    # Animate Player
    player.animate(animationState)
    
    # Refresh On-Screen Colors
    display_surface.fill("black")
    
    # Draw the map
    map.update(mapCoords[0], mapCoords[1])
    # Drawing Player and Hotbar
    all_sprites.draw(display_surface)
    npc.update(entity_list)
    # Updating Display
    pygame.display.update()
    
pygame.quit()
import source.images as images
import json
import os

import source.config as config
import source.playerClass as playerClass
import pytmx
import pyscroll

# Load TMX data
tmx_data = pytmx.load_pygame(os.path.join("maps", "north_overworld", "north_overworld.tmx"))



# Create map data for pyscroll
map_data = pyscroll.data.TiledMapData(tmx_data)

# Create the scrolling map layer
map_layer = pyscroll.BufferedRenderer(map_data, (800, 800))



# print(map_data["Data"])
class Map(config.pygame.sprite.Sprite):
    def __init__(self):
        config.pygame.sprite.Sprite.__init__(self)
        self.direction = config.pygame.Vector2()
        self.speed = 15
        self.x = 400
        self.y = 400
        
        self.movement_mode = 1
        self.map_surface = config.pygame.Surface
        
        self.collision_tiles = [11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28]
        self.warp_tiles = [27, 29]
        playerClass.player.set_movement_mode(1)
    def update(self):
        if playerClass.player.inventory_switch == 1:
            self.movement_mode = 0
        else: 
            self.movement_mode = 1
        if self.movement_mode == 0:
            None
        if self.movement_mode == 1:
            keys = config.pygame.key.get_pressed()
            if keys[config.pygame.K_UP]:
                self.y -= self.speed
            if keys[config.pygame.K_DOWN]:
                self.y += self.speed
            if keys[config.pygame.K_RIGHT]:
                self.x += self.speed
            if keys[config.pygame.K_LEFT]:
                self.x -= self.speed
            
            
            if self.x < 320:
                self.x = 320
            if self.x > 3916:
                self.x = 3916
            if self.y < 320:
                self.y = 320
            if self.y> 3884:
                self.y = 3884
            map_layer.center((self.x, self.y))
        
        print(self.x, self.y, config.pygame.mouse.get_pos())
    def draw(self):
        
        map_layer.draw(config.display_surface, config.display_surface.get_rect())
        
    
map = Map()
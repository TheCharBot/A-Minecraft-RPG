import source.images as images
import os
import source.maps as maps
import source.config as config

class Map(config.pygame.sprite.Sprite):
    def __init__(self):
        config.pygame.sprite.Sprite.__init__(self)
        self.current_map = maps.a1
        self.cache = None
        self.collision_tiles = [11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28]
        self.warp_tiles = [27, 29]
    def update(self, map_x, map_y):

        # add main world maps here:
        if map_x == 1 and map_y == 1:
            if not self.current_map == maps.a1:
                self.current_map = maps.a1
                config.collision_rects.clear()
                config.warp_rects.clear()
                config.warp_rect_names.clear()
                config.entity_list.clear()
            config.warp_rect_names.append("house1")
                
        elif map_x==1 and map_y == 2:
            if not self.current_map == maps.b1:
                self.current_map = maps.b1
                config.collision_rects.clear()
                config.warp_rects.clear()

        elif map_x==2 and map_y==1:
            if not self.current_map == maps.a2:

                self.current_map = maps.a2
                config.collision_rects.clear()
                config.warp_rects.clear()

        elif map_x==2 and map_y == 2:
            if not self.current_map == maps.b2:
                self.current_map = maps.b2
                config.collision_rects.clear()
                config.warp_rects.clear()

        # add more building, cave, etc maps here:
        elif map_x == 100 and map_y == 100:
            if not self.current_map == maps.i1:
                self.current_map = maps.i1
                config.collision_rects.clear()
                config.warp_rects.clear()
                config.warp_rect_names.clear()
            
                config.entity_list.clear()
                config.entity_list.append("sword_villager")
            config.warp_rect_names.append("exit1")
        x = 0
        y = 0
        for item in self.current_map:
            if item in self.collision_tiles:
                config.collision_rects.append(config.pygame.Rect(x, y, 50, 50))
            if item in self.warp_tiles:
                config.warp_rects.append(config.pygame.Rect(x, y, 50, 50))
            config.display_surface.blit(images.image_cache.get_image(item), (x, y))
            x += 50
            
            if x == 800 or x >= 800:
                y += 50
                x = 0
            
    
map = Map()
import source.images as images
import os
import source.maps as maps
import source.config as config

class Map(config.pygame.sprite.Sprite):
    def __init__(self):
        config.pygame.sprite.Sprite.__init__(self)
        self.current_map = maps.a1
        self.cache = None
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
            if item == 11:
                
                config.collision_rects.append(config.pygame.Rect(x, y, 50, 50))
            
            elif item == 14:
                
                config.collision_rects.append(config.pygame.Rect(x, y, 50, 50))
            elif item == 15:
                
                config.collision_rects.append(config.pygame.Rect(x, y, 50, 50))
            elif item == 16:
                
                config.collision_rects.append(config.pygame.Rect(x, y, 50, 50))
            elif item == 17:
                
                config.collision_rects.append(config.pygame.Rect(x, y, 50, 50))
            elif item == 18:
                
                config.collision_rects.append(config.pygame.Rect(x, y, 50, 50))
            elif item == 19:
                
                config.collision_rects.append(config.pygame.Rect(x, y, 50, 50))
            elif item == 20:
                
                config.collision_rects.append(config.pygame.Rect(x, y, 50, 50))
            elif item == 21:
                
                config.collision_rects.append(config.pygame.Rect(x, y, 50, 50))
            elif item == 22:
                
                config.collision_rects.append(config.pygame.Rect(x, y, 50, 50))
            elif item == 23:
                
                config.collision_rects.append(config.pygame.Rect(x, y, 50, 50))
            elif item == 24:
                
                config.collision_rects.append(config.pygame.Rect(x, y, 50, 50))
            elif item == 25:
            
                config.collision_rects.append(config.pygame.Rect(x, y, 50, 50))
            elif item == 26:
                
                config.collision_rects.append(config.pygame.Rect(x, y, 50, 50))
            elif item == 27:
                
                config.warp_rects.append(config.pygame.Rect(x, y, 50, 50))
            elif item == 28:
                
                config.collision_rects.append(config.pygame.Rect(x, y, 50, 50))
            elif item == 29:
                
                config.warp_rects.append(config.pygame.Rect(x, y, 50, 50))
            self.mapObject = images.image_cache.get_image(item)
            config.display_surface.blit(self.mapObject, (x, y))
            x += 50
            
            if x == 800 or x >= 800:
                y += 50
                x = 0
            
    
map = Map()
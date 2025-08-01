import source.images as images
import os
import source.maps as maps
import source.config as config

class Map(config.pygame.sprite.Sprite):
    def __init__(self):
        config.pygame.sprite.Sprite.__init__(self)
        self.current_map = maps.M_1a
        self.cache = None
        self.collision_tiles = [11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28]
        self.warp_tiles = [27, 29]
        self.map_data = {
            # Main world maps
            (1, 1): {
                'map': maps.M_1a,
                'warp_names': ["house1"],
                'entities': []
            },
            (1, 2): {
                'map': maps.M_1b,
                'warp_names': [],
                'entities': []
            },
            (2, 1): {
                'map': maps.M_2a,
                'warp_names': [],
                'entities': []
            },
            (2, 2): {
                'map': maps.M_2b,
                'warp_names': [],
                'entities': []
            },
            (1, 3): {
                'map': maps.M_1c,
                'warp_names': [],
                'entities': [],
            
            },
            # Building/cave maps
            (100, 100): {
                'map': maps.M_1i,
                'warp_names': ["exit1"],
                'entities': ["sword_villager"]
            
            }
            # To add new maps, just add more entries like:
            # (3, 1): {'map': maps.c1, 'warp_names': [], 'entities': []},
        }
    def update(self, map_x, map_y):

        # add main world maps here:
        map_key = (map_x, map_y)
        
        if map_key in self.map_data:
            map_info = self.map_data[map_key]
            
            # Only change map if it's different (same logic as before)
            if not self.current_map == map_info['map']:
                self.current_map = map_info['map']
                config.collision_rects.clear()
                config.warp_rects.clear()
                config.warp_rect_names.clear()
                config.entity_list.clear()
                
                # Add the entities and warp names for this map
                config.entity_list.extend(map_info['entities'])
            config.warp_rect_names.extend(map_info['warp_names'])
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
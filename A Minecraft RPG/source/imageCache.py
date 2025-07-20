import source.config as config
import source.images as images

class ImageCache:
    def __init__(self):
        self.cache = {}
        self.load_all_images()
    
    def load_all_images(self):
        
        image_paths = {
            
            "player_up_1": images.player_up_1,
            "player_up_2": images.player_up_2,
            "player_down_1": images.player_down_1,
            "player_down_2": images.player_down_2,
            "player_right_1": images.player_right_1,
            "player_right_2": images.player_right_2,
            "player_left_1": images.player_left_1,
            "player_left_2": images.player_left_2,
            11: images.grass_side,
            12: images.grass_top,
            13: images.cobblestone,
            14: images.water,
            15: images.dirt,
            16: images.stair_side_left,
            17: images.stair_top_left,
            18: images.log_top,
            19: images.log_side,
            20: images.leaves_side,
            21: images.leaves_top,
            22: images.planks_side,
            23: images.planks_top,
            24: images.stair_side_right,
            25: images.stair_top_right,
            26: images.door_top,
            27: images.door_bottom,
            28: images.empty,
            29: images.door_one_block,
        }
        
        for tile_id, path in image_paths.items():
            self.cache[tile_id] = config.pygame.image.load(path).convert_alpha()
    
    def get_image(self, tile_id):
        return self.cache.get(tile_id)


image_cache = ImageCache()
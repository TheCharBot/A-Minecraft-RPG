import source.config as config
import source.images as images

class Sword():
    def __init__(self, type):
        if type == "wood":
            self.damage = 1
            self.image = images.image_cache.get_image("sword_wood")
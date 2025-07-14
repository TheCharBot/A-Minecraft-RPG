import source.config as config
import source.images as images


config.pygame.font.init()

class Textbox():
    def __init__(self):
        config.pygame.sprite.Sprite.__init__(self)
        self.image = config.pygame.image.load(images.textbox)
textbox = Textbox()
class Hotbar(config.pygame.sprite.Sprite):
    # Class for the Hotbar Sprite
    def __init__(self):
        config.pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 480
        self.direction = config.pygame.Vector2()
        self.image = config.pygame.image.load(images.hotbar_image)
        self.rect = self.image.get_rect(center = (config.WINDOW_WIDTH/2, config.WINDOW_HEIGHT-33))
hotbar = Hotbar()
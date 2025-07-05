from source.Main import *

pygame.font.init()

class Textbox():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(images.textbox)
    
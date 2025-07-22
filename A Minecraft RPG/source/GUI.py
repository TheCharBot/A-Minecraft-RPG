import source.config as config
import source.images as images
import source.playerClass as playerClass
import os

config.pygame.font.init()

class Textbox():
    def __init__(self):
        config.pygame.sprite.Sprite.__init__(self)
        self.image = images.image_cache.get_image("textbox")
        self.rect = self.image.get_rect()
        self.dialogue = None
        self.font = config.pygame.font.Font(os.path.join("font", "Jersey10-Regular.ttf"), 40)
        self.textbox_input = ""
        self.show = False
    def set_text(self, input):
        
        
        self.textbox_input = input
        self.text_surface = self.font.render(str(self.textbox_input), False, (255, 255, 255), (0, 0, 0))
        self.text_rect = self.text_surface.get_rect(topleft = (60, config.WINDOW_HEIGHT - 207))
        
    def update(self):
        if playerClass.player.speaking == True:
            self.show = True
            config.display_surface.blit(self.text_surface, self.text_rect)
            config.display_surface.blit(self.image, (50, config.WINDOW_HEIGHT - 217))
            playerClass.player.set_movement_mode(0)
            
        if playerClass.player.z_pressed:
            self.show = False
            playerClass.player.speaking = False
            playerClass.player.set_movement_mode(1)
textbox = Textbox()
class Hotbar(config.pygame.sprite.Sprite):
    # Class for the Hotbar Sprite
    def __init__(self):
        config.pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 480
        self.direction = config.pygame.Vector2()
        self.image = images.image_cache.get_image("hotbar_image")
        self.rect = self.image.get_rect(center = (config.WINDOW_WIDTH/2, config.WINDOW_HEIGHT-33))

hotbar = Hotbar()
class Inventory(config.pygame.sprite.Sprite):
    # Class for the Inventory Sprite
    def __init__(self):
        config.pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.show = False
        self.direction = config.pygame.Vector2()
        self.image = images.image_cache.get_image("inventory_image")
        self.rect = self.image.get_rect(center = (config.WINDOW_WIDTH/2, config.WINDOW_HEIGHT/2))
    def update(self):
        if playerClass.player.inventory_switch == 1:
            if playerClass.player.speaking:
                None
            else:
                self.show = True
                config.display_surface.blit(self.image, self.rect)
                playerClass.player.set_movement_mode(0)
                self.when_open()
        else:
            if not playerClass.player.speaking:
                playerClass.player.set_movement_mode(1)
            else:
                None
    def when_open(self):
        key = config.pygame.key.get_pressed()
        if key[config.pygame.K_UP]:
            None #print("UP")
        if key[config.pygame.K_DOWN]:
            None #print("DOWN")
        if key[config.pygame.K_LEFT]:
            None #print("LEFT")
        if key[config.pygame.K_RIGHT]:
            None #print("RIGHT")

            
                    

            
        
            
inventory = Inventory()
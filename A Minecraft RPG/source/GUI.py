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



class InventoryCursor(config.pygame.sprite.Sprite):
    def __init__(self):
        config.pygame.sprite.Sprite.__init__(self)
        self.show = False
        self.x = 0
        self.y = 0
        self.speed = 36
        self.image = images.image_cache.get_image("inv_cursor")
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.slot = 1
        self.holding_item = "clear"
    def show_state(self, input):
        self.show = input
    def update(self):
        if self.show == True:
           
            if self.rect.x > 511:
                self.rect.x = 511
            elif self.rect.x < 236:
                self.rect.x = 236
            if self.rect.y < inventory.y_offset+5:
                self.rect.y = inventory.y_offset+5
            if self.rect.y > 499:
                self.rect.y = 499
            config.display_surface.blit(self.image, self.rect)
            
            if self.holding_item != "clear":
                # Add Item image show here
                None
                
        #elif self.rect.y 
    def up(self):
        self.slot -= 7
        if self.slot < 1:
            self.slot = 1
        self.rect.x = inventory.slot_layout[self.slot]["x"]-2
        self.rect.y = inventory.slot_layout[self.slot]["y"]-1
    def down(self):
        self.slot += 7
        if self.slot > 36:
            self.slot = 36
        self.rect.x = inventory.slot_layout[self.slot]["x"]-2
        self.rect.y = inventory.slot_layout[self.slot]["y"]-1
    def right(self):
        self.slot += 1
        if self.slot > 36:
            self.slot = 36
        self.rect.x = inventory.slot_layout[self.slot]["x"]-2
        self.rect.y = inventory.slot_layout[self.slot]["y"]-1
    def left(self):
        self.slot -= 1
        if self.slot < 1:
            self.slot = 1
        self.rect.x = inventory.slot_layout[self.slot]["x"]-2
        self.rect.y = inventory.slot_layout[self.slot]["y"]-1
inv_cursor = InventoryCursor()
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
        self.items = playerClass.player.inventory
        self.x_offset = 230
        self.y_offset = 318
        
        self.slot_layout = {
            # Helmet Slot:
            1: {"x": self.x_offset + 8,
                "y": self.y_offset + 6,
                "contents": "clear"},
            # Chestplate Slot:
            2: {"x": self.x_offset + 53,
                "y": self.y_offset + 6,
                "contents": "clear"},
            # Leggings Slot:
            3: {"x": self.x_offset + 106,
                "y": self.y_offset + 6,
                "contents": "clear"},
            # Boots Slot:
            4: {"x": self.x_offset + 147,
                "y": self.y_offset + 6,
                "contents": "clear"},
            # Orb Slot:
            5: {"x": self.x_offset + 293,
                "y": self.y_offset + 6,
                "contents": "clear"}, 
            # Normal Item Slots:
            6: {"x": self.x_offset + 8,
                "y": self.y_offset + 41,
                "contents": "sword_neth"}, 
            7: {"x": self.x_offset + 53,
                "y": self.y_offset + 41,
                "contents": "sword_diam"},
            8: {"x": self.x_offset + 99,
                "y": self.y_offset + 41,
                "contents": "clear"},
            9: {"x": self.x_offset + 145,
                "y": self.y_offset + 41,
                "contents": "clear"},
            10: {"x": self.x_offset + 191,
                "y": self.y_offset + 41,
                "contents": "clear"}, 
            11: {"x": self.x_offset + 237,
                "y": self.y_offset + 41,
                "contents": "clear"}, 
            12: {"x": self.x_offset + 283,
                "y": self.y_offset + 41,
                "contents": "clear"}, 
            13: {"x": self.x_offset + 8,
                "y": self.y_offset + 76,
                "contents": "clear"}, 
            14: {"x": self.x_offset + 53,
                "y": self.y_offset + 76,
                "contents": "clear"}, 
            15: {"x": self.x_offset +  99,
                "y": self.y_offset + 76,
                "contents": "clear"}, 
            16: {"x": self.x_offset + 145,
                "y": self.y_offset + 76,
                "contents": "clear"}, 
            17: {"x": self.x_offset + 191,
                "y": self.y_offset + 76,
                "contents": "clear"}, 
            18: {"x": self.x_offset + 237,
                "y": self.y_offset + 76,
                "contents": "clear"}, 
            19: {"x": self.x_offset + 283,
                "y": self.y_offset + 76,
                "contents": "clear"}, 
            20: {"x": self.x_offset + 8,
                "y": self.y_offset + 111,
                "contents": "clear"}, 
            21: {"x": self.x_offset + 53,
                "y": self.y_offset + 111,
                "contents": "clear"}, 
            22: {"x": self.x_offset + 99,
                "y": self.y_offset + 111,
                "contents": "clear"}, 
            23: {"x": self.x_offset + 145,
                "y": self.y_offset + 111,
                "contents": "clear"}, 
            24: {"x": self.x_offset + 191,
                "y": self.y_offset + 111,
                "contents": "clear"}, 
            25: {"x": self.x_offset + 237,
                "y": self.y_offset + 111,
                "contents": "clear"}, 
            26: {"x": self.x_offset + 283,
                "y": self.y_offset + 111,
                "contents": "clear"}, 
            27: {"x": self.x_offset + 8,
                "y": self.y_offset + 146,
                "contents": "clear"}, 
            28: {"x": self.x_offset + 53,
                "y": self.y_offset + 146,
                "contents": "clear"}, 
            29: {"x": self.x_offset + 99,
                "y": self.y_offset + 146,
                "contents": "clear"}, 
            30: {"x": self.x_offset + 145,
                "y": self.y_offset + 146,
                "contents": "clear"}, 
            31: {"x": self.x_offset + 191,
                "y": self.y_offset + 146,
                "contents": "clear"}, 
            32: {"x": self.x_offset + 237,
                "y": self.y_offset + 146,
                "contents": "clear"}, 
            33: {"x": self.x_offset + 283,
                "y": self.y_offset + 146,
                "contents": "clear"},
            # Held Item Slots:
            34: {"x": self.x_offset + 8,
                "y": self.y_offset + 181,
                "contents": "clear"}, 
            35: {"x": self.x_offset + 53,
                "y": self.y_offset + 181,
                "contents": "clear"}, 
            36: {"x": self.x_offset + 99,
                "y": self.y_offset + 181,
                "contents": "clear"},

            
        }
        
    def update(self):
        
        if playerClass.player.inventory_switch == 1:
            if playerClass.player.speaking:
                None
                inv_cursor.show_state(False)
            else:
                self.show = True
                inv_cursor.show_state(True)
                config.display_surface.blit(self.image, self.rect)
                playerClass.player.set_movement_mode(0)
                self.when_open()
        else:
            if not playerClass.player.speaking:
                inv_cursor.show_state(False)
                playerClass.player.set_movement_mode(1)
            else:
                None
    def when_open(self):
        
        key = config.pygame.key.get_just_pressed()
        if key[config.pygame.K_UP]:
            inv_cursor.up()
        if key[config.pygame.K_DOWN]:
            inv_cursor.down()
        if key[config.pygame.K_LEFT]:
            inv_cursor.left()
        if key[config.pygame.K_RIGHT]:
            inv_cursor.right()
        if key[config.pygame.K_x]:
            self.take_item(inv_cursor.slot)
        if key[config.pygame.K_z]:
            self.drop_item(inv_cursor.slot)
        for slot_data in self.slot_layout.values():
            config.display_surface.blit(
                images.image_cache.get_image(slot_data["contents"]), 
                (slot_data["x"], slot_data["y"])
            )
            
    def take_item(self, slot):
       
        if inv_cursor.holding_item == "clear" and not self.slot_layout[slot]["contents"] == "clear":
            inv_cursor.holding_item = self.slot_layout[slot]["contents"]
            self.slot_layout[slot]["contents"] = "clear"
            
        
        
    def drop_item(self, slot):
        if self.slot_layout[slot]["contents"] == "clear" and not inv_cursor.holding_item == "clear":
            self.slot_layout[slot]["contents"] = inv_cursor.holding_item
            inv_cursor.holding_item = "clear"
        

        
            
        
            
inventory = Inventory()



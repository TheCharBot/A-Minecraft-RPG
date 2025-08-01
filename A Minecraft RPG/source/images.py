import os
import platform
import source.config as config


empty = os.path.join("textures", "empty.png")
clear = os.path.join("textures", "clear.png")

if platform.system() == "Windows":
    
    icon = os.path.join("textures", "icon", "icon.ico")
else:
    
    icon = os.path.join("textures", "icon", "icon.png")

### PLAYER IMAGES ###

player_sheet = os.path.join("textures", "player", "player_sheet.png")
### BLOCK IMAGES ###

grass_side = os.path.join("textures", "blocks", "grass", "grassside.png")
grass_top = os.path.join("textures", "blocks", "grass", "grasstop.png")
cobblestone = os.path.join("textures", "blocks", "cobblestone", "cobblestone.png")
water = os.path.join("textures", "blocks", "water", "water.png")
dirt = os.path.join("textures", "blocks", "grass", "dirt.png")
stair_side_right = os.path.join("textures", "blocks", "stairs", "stairside_right.png")
stair_top_right = os.path.join("textures", "blocks", "stairs", "stairtop_right.png")
stair_side_left = os.path.join("textures", "blocks", "stairs", "stairside_left.png")
stair_top_left = os.path.join("textures", "blocks", "stairs", "stairtop_left.png")
log_top = os.path.join("textures", "blocks", "wood", "logtop.png")
log_side = os.path.join("textures", "blocks", "wood", "logside.png")
leaves_side = os.path.join("textures", "blocks", "leaves", "leavesside.png")
leaves_top = os.path.join("textures", "blocks", "leaves", "leavestop.png")
planks_side = os.path.join("textures", "blocks", "wood", "planksside.png")
planks_top = os.path.join("textures", "blocks", "wood", "plankstop.png")
door_bottom = os.path.join("textures", "blocks", "door", "door_bottom.png")
door_top = os.path.join("textures", "blocks", "door", "door_top.png")
door_one_block = os.path.join("textures", "blocks", "door", "door_one_block.png")

### INVENTORY IMAGES ###

hotbar_image = os.path.join("textures", "GUI", "inventory", "hotbar.png")
inventory_image = os.path.join("textures", "GUI", "inventory", "itempage.png")
inventory_cursor_image = os.path.join("textures", "GUI", "inventory", "inv_cursor.png")

### ITEMS ###

wood_sword_image = os.path.join("textures", "items", "swords", "wood_sword.png")
stone_sword_image = os.path.join("textures", "items", "swords", "stone_sword.png")
iron_sword_image = os.path.join("textures", "items", "swords", "iron_sword.png")
gold_sword_image = os.path.join("textures", "items", "swords", "gold_sword.png")
diamond_sword_image = os.path.join("textures", "items", "swords", "diamond_sword.png")
netherite_sword_image = os.path.join("textures", "items", "swords", "netherite_sword.png")

### ENTITIES ###

villager_down = os.path.join("textures", "entities", "villager", "villager_down.png")

### GUI ###

textbox = os.path.join("textures", "GUI", "textbox", "textbox_border.png")



class ImageCache:
    def __init__(self):
        self.cache = {}
        self.load_all_images()
    
    def load_all_images(self):
        
        image_paths = {
            "sword_wood": wood_sword_image,
            "sword_ston": stone_sword_image,
            "sword_iron": iron_sword_image,
            "sword_gold": gold_sword_image,
            "sword_diam": diamond_sword_image,
            "sword_neth": netherite_sword_image,
            "empty": empty,
            
            "clear": clear,
            "inv_cursor": inventory_cursor_image,
            "player_sheet": player_sheet,
            "inventory_image": inventory_image,
            "hotbar_image": hotbar_image,
            "villager_down": villager_down,
            "textbox": textbox,
            11: grass_side,
            12: grass_top,
            13: cobblestone,
            14: water,
            15: dirt,
            16: stair_side_left,
            17: stair_top_left,
            18: log_top,
            19: log_side,
            20: leaves_side,
            21: leaves_top,
            22: planks_side,
            23: planks_top,
            24: stair_side_right,
            25: stair_top_right,
            26: door_top,
            27: door_bottom,
            28: empty,
            29: door_one_block,
        }
        
        for tile_id, path in image_paths.items():
            self.cache[tile_id] = config.pygame.image.load(path).convert_alpha()
    
    def get_image(self, tile_id):
        return self.cache.get(tile_id)


image_cache = ImageCache()



def get_sprite(spritesheet, ext_x, ext_y, width, height):
        
        sprite = config.pygame.Surface((width, height), config.pygame.SRCALPHA)
        sprite.blit(spritesheet, (0, 0), (ext_x, ext_y, width, height))
        return sprite
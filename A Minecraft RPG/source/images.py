import os
import platform

empty = os.path.join("textures", "empty.png")

if platform.system() == "Windows":
    
    icon = os.path.join("textures", "icon", "icon.ico")
else:
    
    icon = os.path.join("textures", "icon", "icon.png")

### PLAYER IMAGES ###
player_idle_down = os.path.join("textures", "player", "idle_down.png")
player_idle_up = os.path.join("textures", "player", "idle_up.png")
player_idle_left = os.path.join("textures", "player", "idle_left.png")
player_idle_right = os.path.join("textures", "player", "idle_right.png")
player_right_1 = os.path.join("textures", "player", "playerright1.png")
player_right_2 = os.path.join("textures", "player", "playerright2.png")
player_left_1 = os.path.join("textures", "player", "playerleft1.png")
player_left_2 = os.path.join("textures", "player", "playerleft2.png")
player_down_1 = os.path.join("textures", "player", "playerdown1.png")
player_down_2 = os.path.join("textures", "player", "playerdown2.png")
player_up_1 = os.path.join("textures", "player", "playerup1.png")
player_up_2 = os.path.join("textures", "player", "playerup2.png")

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
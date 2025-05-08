import pygame
my_info = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer"
}
pygame.init()
wood_sword = {"damage": 1, 
              "image": pygame.image.load("textures\\items\\swords\\wood_sword.png")}

stone_sword = {"damage": 2, 
               "image": pygame.image.load("textures\\items\\swords\\stone_sword.png")}

iron_sword = {"damage": 3,
              "image": pygame.image.load("textures\\items\\swords\\iron_sword.png")}

gold_sword = {"damage": 2.5,
              "image": pygame.image.load("textures\\items\\swords\\gold_sword.png")}

diamond_sword = {"damage": 4,
                 "image": pygame.image.load("textures\\items\\swords\\diamond_sword.png")}

netherite_sword = {"damage": 5,
                   "image": pygame.image.load("textures\\items\\swords\\netherite_sword.png")}
from source.Main import *

class Map(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.current_map = maps.a1
    def update(self, map_x, map_y):

        # add main world maps here:
        if map_x == 1 and map_y == 1:
            self.current_map = maps.a1
            collision_rects.clear()
            warp_rects.clear()
            warp_rect_names.clear()
            warp_rect_names.append("house1")
        elif map_x==1 and map_y == 2:
            self.current_map = maps.b1
            collision_rects.clear()
            warp_rects.clear()

        elif map_x==2 and map_y==1:
            self.current_map = maps.a2
            collision_rects.clear()
            warp_rects.clear()

        elif map_x==2 and map_y == 2:
            self.current_map = maps.b2
            collision_rects.clear()
            warp_rects.clear()

        # add more building, cave, etc maps here:
        elif map_x == 100 and map_y == 100:
            
            self.current_map = maps.i1
            collision_rects.clear()
            warp_rects.clear()
            warp_rect_names.clear()
            warp_rect_names.append("exit1")
    
        x = 0
        y = 0
        for item in self.current_map:
            if item == 11:
                self.mapObject = pygame.image.load(images.grass_side)
                collision_rects.append(pygame.Rect(x, y, 50, 50))
            elif item == 12:
                self.mapObject = pygame.image.load(images.grass_top)
            elif item == 13:
                self.mapObject = pygame.image.load(images.cobblestone)
            elif item == 14:
                self.mapObject = pygame.image.load(images.water)
                collision_rects.append(pygame.Rect(x, y, 50, 50))
            elif item == 15:
                self.mapObject = pygame.image.load(images.dirt)
                collision_rects.append(pygame.Rect(x, y, 50, 50))
            elif item == 16:
                self.mapObject = pygame.image.load(images.stair_side_left)
                collision_rects.append(pygame.Rect(x, y, 50, 50))
            elif item == 17:
                self.mapObject = pygame.image.load(images.stair_top_left)
                collision_rects.append(pygame.Rect(x, y, 50, 50))
            elif item == 18:
                self.mapObject = pygame.image.load(images.log_top)
                collision_rects.append(pygame.Rect(x, y, 50, 50))
            elif item == 19:
                self.mapObject = pygame.image.load(images.log_side)
                collision_rects.append(pygame.Rect(x, y, 50, 50))
            elif item == 20:
                self.mapObject = pygame.image.load(images.leaves_side)
                collision_rects.append(pygame.Rect(x, y, 50, 50))
            elif item == 21:
                self.mapObject = pygame.image.load(images.leaves_top)
                collision_rects.append(pygame.Rect(x, y, 50, 50))
            elif item == 22:
                self.mapObject = pygame.image.load(images.planks_side)
                collision_rects.append(pygame.Rect(x, y, 50, 50))
            elif item == 23:
                self.mapObject = pygame.image.load(images.planks_top)
                collision_rects.append(pygame.Rect(x, y, 50, 50))
            elif item == 24:
                self.mapObject = pygame.image.load(images.stair_side_right)
                collision_rects.append(pygame.Rect(x, y, 50, 50))
            elif item == 25:
                self.mapObject = pygame.image.load(images.stair_top_right)
                collision_rects.append(pygame.Rect(x, y, 50, 50))
            elif item == 26:
                self.mapObject = pygame.image.load(images.door_top)
                collision_rects.append(pygame.Rect(x, y, 50, 50))
            elif item == 27:
                self.mapObject = pygame.image.load(images.door_bottom)
                warp_rects.append(pygame.Rect(x, y, 50, 50))
            elif item == 28:
                self.mapObject = pygame.image.load(images.empty)
                collision_rects.append(pygame.Rect(x, y, 50, 50))
            elif item == 29:
                self.mapObject = pygame.image.load(images.door_one_block)
                warp_rects.append(pygame.Rect(x, y, 50, 50))
            display_surface.blit(self.mapObject, (x, y))
            x += 50
            
            if x == 800 or x >= 800:
                y += 50
                x = 0
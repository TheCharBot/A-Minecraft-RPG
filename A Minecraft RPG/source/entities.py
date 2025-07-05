from source.Main import *




class Villager(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(images.villager_down)
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.show = False
        self.interact_direction = "null"
    def update(self, entity_list):
        if "sword_villager" in entity_list:
            self.rect.center = WINDOW_WIDTH/2, (WINDOW_HEIGHT/3)+1
            self.image = pygame.image.load(images.villager_down)
            self.show = True
            self.interact_direction = "up"
            collision_rects.append(self.rect)
            
            interact_rects.append(pygame.Rect(WINDOW_WIDTH/2 - 25, (WINDOW_HEIGHT/3) + 30, 50, 50))
            
            
            
        else:

            self.show = False
    
        if self.show:
            display_surface.blit(self.image, self.rect)










Entities = {"villager": Villager}
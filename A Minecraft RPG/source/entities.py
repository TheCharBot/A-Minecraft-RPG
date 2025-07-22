import source.images as images
import source.config as config




class Villager(config.pygame.sprite.Sprite):
    def __init__(self):
        config.pygame.sprite.Sprite.__init__(self)
        self.image = config.pygame.image.load(images.villager_down)
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.show = False
        self.interact_direction = "null"
        self.dialogue = ""
    def update(self, entity_list):
        if "sword_villager" in entity_list:
            self.rect.center = config.WINDOW_WIDTH/2, (config.WINDOW_HEIGHT/3)+1
            self.image = images.image_cache.get_image("villager_down")
            self.show = True
            self.interact_direction = "up"
            self.dialogue = "Hi!"
            if self.rect not in config.collision_rects:
                config.collision_rects.append(self.rect)
            
            if config.pygame.Rect not in config.interact_rects:
            
                config.interact_rects.append(config.pygame.Rect(config.WINDOW_WIDTH/2 - 25, (config.WINDOW_HEIGHT/3) + 30, 50, 50))
        else:
            self.show = False
        if self.show:
            config.display_surface.blit(self.image, self.rect)
        return self.dialogue
npc = Villager()









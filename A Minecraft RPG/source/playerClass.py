import source.config as config
import source.images as images
import source.entities as entities






class Player(config.pygame.sprite.Sprite):
    def __init__(self):
        
        config.pygame.sprite.Sprite.__init__(self)

        # Setting Self. Variables
        self.facing = "idle"
        self.speed = 250
        self.x = 0
        self.y = 0
        self.map_x = 1
        self.map_y = 1
        self.direction = config.pygame.Vector2()
        self.image = config.pygame.transform.flip(images.get_sprite(images.image_cache.get_image("player_sheet"), 0, 0, 40, 40), True, False)
        self.rect = self.image.get_rect(center = (config.WINDOW_WIDTH/2, config.WINDOW_HEIGHT/2))
        self.x_pressed = False
        self.z_pressed = False
        self.f_pressed = False
        self.e_pressed = False
        self.speaking = False
        self.movement_mode = 1
        self.inventory_switch = 0
        self.anim_on = True
        self.colliding = False
        self.rectxSAVE = 0
        self.rectySAVE = 0
        self.inventory = []
    def set_movement_mode(self, input):
        self.movement_mode = input
    def update(self, dt):
       
        # Variable creation and assignment
        keys = config.pygame.key.get_pressed()
        
        
        # Saving current location for collisions
        if self.colliding == False:
            self.rectxSAVE = self.rect.x
            self.rectySAVE = self.rect.y
        self.colliding = False
        if self.movement_mode == 0:
            
            self.anim_on = False
        elif self.movement_mode == 1:
            # Key and movement calculation
            self.direction.x = int(keys[config.pygame.K_RIGHT]) - int(keys[config.pygame.K_LEFT])
            self.direction.y = int(keys[config.pygame.K_DOWN]) - int(keys[config.pygame.K_UP])

            # Normalizing diagonal movements with the vector
            self.direction = (self.direction.normalize() if self.direction else self.direction)

            # Recalculating position and movement
            self.rect.x += self.direction.x * self.speed * dt
            self.rect.y += self.direction.y * self.speed * dt
            
        

            # Checking which way the magnitude reports the player is going
            if self.direction.magnitude() > 0: 
                if self.direction.x > 0:
                    self.facing = "right"
                    self.anim_on = True
                elif self.direction.x < 0:
                    self.facing = "left"
                    self.anim_on = True
                elif self.direction.y < 0:
                    self.facing = "up"
                    self.anim_on = True
                elif self.direction.y > 0:
                    self.facing = "down"
                    self.anim_on = True
            else:
                self.anim_on = False

        ### Collisions ###
        # Checking for collisions, if true, revert player to a previous position
        for rect in config.collision_rects:
            if self.rect.colliderect(rect):
                self.rect.x = self.rectxSAVE
                self.rect.y = self.rectySAVE
                self.colliding = True
                
                break
        
        for rect in config.warp_rects:
            if self.rect.colliderect(rect):
                
                if "house1" in config.warp_rect_names:
                    self.map_x = 100
                    self.map_y = 100
                    self.rect.x = 355
                    self.rect.y = 700
                if "exit1" in config.warp_rect_names:
                    self.map_x = 1
                    self.map_y = 1
                    self.rect.x = 355
                    self.rect.y = 210
        
        

        ### Attacking and Placing ###

        # Checking for X key getting pressed
        if config.pygame.key.get_pressed()[config.pygame.K_x]:
            self.x_pressed = True
            
        # Checking for Z key getting pressed
        if config.pygame.key.get_pressed()[config.pygame.K_z]:
            self.z_pressed = True
            
        
        # Checking for F key getting pressed (to switch the off hand item with the X or Z key items)
        if config.pygame.key.get_pressed()[config.pygame.K_f]:
            self.f_pressed = True
             

        # Checking for E key getting pressed (to open inventory)
        if config.pygame.key.get_just_pressed()[config.pygame.K_e]:
            self.e_pressed = True
            if self.inventory_switch == 1:

                self.inventory_switch = 0
            elif self.inventory_switch == 0:
                self.inventory_switch = 1



        if not config.pygame.key.get_pressed()[config.pygame.K_x]:
            self.x_pressed = False
            
        # Checking for Z key getting pressed
        if not config.pygame.key.get_pressed()[config.pygame.K_z]:
            self.z_pressed = False
            
        
        # Checking for F key getting pressed (to switch the off hand item with the X or Z key items)
        if not config.pygame.key.get_pressed()[config.pygame.K_f]:
            self.f_pressed = False
             

        # Checking for E key getting pressed (to open inventory)
        if not config.pygame.key.get_just_pressed()[config.pygame.K_e]:
            self.e_pressed = False
            
        for rect in config.interact_rects:
            if self.rect.colliderect(rect) and self.facing == entities.villager.interact_direction and self.x_pressed == True:
                 
                self.speaking = True
        config.display_surface.blit(self.image, self.rect)
    # Animation function
    def animate(self, animationState):
        # Animation State Check
        if config.is_even(animationState) and self.anim_on == True:
            if self.facing == "right":
                self.image = config.pygame.transform.flip(images.get_sprite(images.image_cache.get_image("player_sheet"), 0, 0, 40, 40), True, False)
            elif self.facing == "left":
                self.image = images.get_sprite(images.image_cache.get_image("player_sheet"), 48, 0, 40, 40)
            elif self.facing == "up":
                self.image = images.get_sprite(images.image_cache.get_image("player_sheet"), 96, 0, 40, 40)
            elif self.facing == "down":
                self.image = images.get_sprite(images.image_cache.get_image("player_sheet"), 0, 0, 40, 40)
            
        # If the animation state is odd, do a different animation
        else:
            if self.facing == "right":
                self.image = config.pygame.transform.flip(images.get_sprite(images.image_cache.get_image("player_sheet"), 48, 0, 40, 40), True, False)
            elif self.facing == "left":
                self.image = images.get_sprite(images.image_cache.get_image("player_sheet"), 0, 0, 40, 40)
            elif self.facing == "up":
                self.image = config.pygame.transform.flip(images.get_sprite(images.image_cache.get_image("player_sheet"), 96, 0, 40, 40), True, False)
            elif self.facing == "down":
                self.image = config.pygame.transform.flip(images.get_sprite(images.image_cache.get_image("player_sheet"), 0, 0, 40, 40), True, False)
           
        
    def map_movement(self):
        if self.rect.x > 760:
            self.map_x += 1
            self.rect.x = 2
            
        elif self.rect.x < 0:
            self.map_x -= 1
            self.rect.x = 758
            
        elif self.rect.y > 760:
            self.map_y += 1
            self.rect.y = 2
            
        elif self.rect.y < 0:
            self.map_y -= 1
            self.rect.y =  758
            
            
        return self.map_x, self.map_y
    def give_item(self, item):
        self.inventory.append(item)
player = Player()
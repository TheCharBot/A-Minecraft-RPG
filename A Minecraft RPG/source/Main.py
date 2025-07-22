import source.config as config
import source.images as images
import source.GUI as gui
import source.entities as entities
import source.playerClass as playerClass
import source.mapClass as mapClass


# Setup
config.pygame.init()

display_surface = config.display_surface
late_trigger = False
display_icon = config.pygame.image.load(images.icon)
config.pygame.display.set_icon(display_icon)
config.pygame.display.set_caption("A Minecraft RPG")

# Object creation





    



# Animation Stage Event

config.pygame.time.set_timer(config.ANIMATION_STATE_TRIGGER, 200)

# import of sprite classes


# Assignment of Sprite Classes to Sprite Group


all_sprites = config.pygame.sprite.Group()






all_sprites.add(gui.hotbar)
all_sprites.add(playerClass.player)


# Game Loop
#current_map = map_check()

while config.running:
    dt = config.clock.tick(30) / 1000
    
    # Checking for Quit Event and Animation Stage Shift Events
    for event in config.pygame.event.get():
        if event.type == config.pygame.QUIT:
            config.running = False
        elif event.type == config.ANIMATION_STATE_TRIGGER:
            config.animationState +=1
            if config.animationState >= 2:
                config.animationState = 0
        elif event.type == config.pygame.KEYDOWN:
            if event.key == config.pygame.K_e:
                late_trigger = True
                
    mapCoords = playerClass.player.map_movement()
    # Update sprites
    
    all_sprites.update(dt)
    
    # Animate Player
    playerClass.player.animate(config.animationState)
    
    # Refresh On-Screen Colors
    display_surface.fill("black")
    
    # Draw the map
    mapClass.map.update(mapCoords[0], mapCoords[1])
    
    
    # Drawing Player and Hotbar
    all_sprites.draw(display_surface)
    gui.textbox.set_text(entities.npc.update(config.entity_list))
    gui.textbox.update()
    
    # Updating Display
    
    gui.inventory.update()
        
    
    config.pygame.display.update()
   
    
config.pygame.quit()
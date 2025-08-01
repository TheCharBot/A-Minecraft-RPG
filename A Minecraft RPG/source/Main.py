import source.config as config
import source.images as images
import source.GUI as gui
import source.entities as entities
import source.playerClass as playerClass
import source.mapClass as mapClass


# Setup
config.pygame.init()

display_surface = config.display_surface

display_icon = config.pygame.image.load(images.icon)
config.pygame.display.set_icon(display_icon)
config.pygame.display.set_caption("A Minecraft RPG")

# Object creation




###
### STOP OPTIMIZING AND ADD MORE CONTENT!!!
###
    



# Animation Stage Event

config.pygame.time.set_timer(config.ANIMATION_STATE_TRIGGER, 200)













def draw_hotbar():
    display_surface.blit(images.image_cache.get_image("hotbar_image"), (config.WINDOW_WIDTH/2-250, config.WINDOW_HEIGHT-67))
def get_events():
    for event in config.pygame.event.get():
        if event.type == config.pygame.QUIT:
            config.running = False
        elif event.type == config.ANIMATION_STATE_TRIGGER:
            config.animationState +=1
            if config.animationState >= 2:
                config.animationState = 0
def gui_update():
    gui.textbox.update()
    gui.inventory.update()
    gui.inv_cursor.update()
# Game Loop


while config.running:
    dt = config.clock.tick(30) / 1000
    
   
    
    get_events()
    
  
    
    
    
    
    mapCoords = playerClass.player.map_movement()
    display_surface.fill("black")
    mapClass.map.update(mapCoords[0], mapCoords[1])
    
    
    
    
    playerClass.player.update(dt)
    playerClass.player.animate(config.animationState)
    entities.villager.update(config.entity_list)
    gui_update()
    draw_hotbar()
    config.pygame.display.update()
   
    
config.pygame.quit()
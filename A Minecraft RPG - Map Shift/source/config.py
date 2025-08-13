import pygame


def is_even(number):
  return number % 2 == 0

ANIMATION_STATE_TRIGGER = pygame.USEREVENT + 1
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 867
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

running = True
clock = pygame.time.Clock()
animationState = 1
collision_rects = []
warp_rects = []
warp_rect_names = []
entity_list = []
interact_rects = []
HOTBAR_X, HOTBAR_Y = 0, 800
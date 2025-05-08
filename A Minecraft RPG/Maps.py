# how maps work:
# each number correlates to a specific block(tile) on the screen
# 1 = grass with dirt
# 2 = grass from top
# 3 = cobblestone
# 4 = water

def a1():
    map = [1, 1, 4, 4, 4, 4, 4, 4, 1, 1, 
           2, 1, 4, 4, 4, 4, 4, 4, 1, 2, 
           2, 2, 1, 4, 4, 4, 4, 1, 2, 2, 
           2, 2, 2, 1, 4, 4, 1, 2, 2, 2, 
           2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 
           2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
           2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
           3, 2, 2, 2, 2, 2, 2, 2, 2, 3, 
           3, 2, 2, 2, 2, 2, 2, 2, 2, 3, 
           3, 3, 3, 2, 2, 2, 2, 3, 3, 3]
    return map

def spawnup1():
    map = []
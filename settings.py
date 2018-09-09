
WHITE       = (255,255,255)
LIGHTGRAY   = (200,200,200)
GRAY        = (140,140,140)
DARKGRAY    = ( 40, 40, 40)
BLACK       = (  0,  0,  0)
RED         = (255,  0,  0)
GREEN       = (  0,255,  0)
BLUE        = (  0,  0,255)
YELLOW      = (255,255,  0)


TITLE = "my game"
WIDTH = 1500
HEIGHT = 800
FPS = 60
BGCOLOR = DARKGRAY

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

PLAYER_SPEED = 1
PLAYER_STEPS_PER_TILE = 3

#screen tearing ist das problem
# -> double buffering
# -> vertical synchronisation

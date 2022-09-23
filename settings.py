import math

WIDTH = 1200
HEIGHT = 800

HALFWIDTH = 600
HALFHEIGHT = 400

FPS = 60

TILESIZE = 100

FOV = math.pi / 3
HALFFOV = FOV / 2
NUMRAYS = 1
MAXDEPTH = 800
DELTAANGLE = FOV / NUMRAYS
DISTANCE = NUMRAYS / (2 * math.tan(HALFFOV))
PROJECTIVECOEF = 1 * DISTANCE * TILESIZE
SCALE = WIDTH // NUMRAYS


PlayerPosition = (600, 400)
PlayerAngle = 0
PlayerSpeed = 2

White = (255, 255, 255)
Black = (0, 0, 0)
Red = (220, 0, 0)
Green = (0, 220, 0)
Blue = (0, 0, 220)
DarkGray = (110, 110, 110)
Purple = (120, 0, 120)
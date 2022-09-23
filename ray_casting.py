from settings import *
from map import world_map
import pygame
import math

def rayCasting(screen, playerPosition, playerAngle):
    curAngle = playerAngle - HALFFOV
    xo, yo = playerPosition
    for ray in range(NUMRAYS):
        sin_a = math.sin(curAngle)
        cos_a = math.cos(curAngle)
        for depth in range(MAXDEPTH):
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            #pygame.draw.line(screen, DarkGray, playerPosition, (x, y), 2)
            if (x // TILESIZE * TILESIZE, y // TILESIZE * TILESIZE) in world_map:
                
                if (depth == 0):
                    break
                depth *= math.cos(playerAngle - curAngle)
                projectiveHeight = PROJECTIVECOEF / depth
                colorByte = 255 / (1 + depth * depth * 0.00002)
                pygame.draw.rect(
                    screen,
                    (colorByte, colorByte, colorByte),
                    (ray * SCALE, HALFHEIGHT - projectiveHeight // 2, SCALE, projectiveHeight)
                )
                break
        curAngle += DELTAANGLE
import pygame 
from settings import *
from player import Player
from map import world_map
from ray_casting import rayCasting
import math

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    player.movement()
    screen.fill(Black)

    rayCasting(
        screen,
        player.position,
        player.angle
    )

    pygame.display.flip()
    clock.tick(FPS)
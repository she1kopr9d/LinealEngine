from webbrowser import get
from settings import *
import pygame
import math

class Player:
    def __init__(self):
        self.x, self.y = PlayerPosition
        self.angle = PlayerAngle

    @property
    def position(self):
        return (self.x, self.y)
    
    @property
    def intPosition(self):
            return (int(self.x), int(self.y))

    def movement(self):

        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += PlayerSpeed * cos_a
            self.y += PlayerSpeed * sin_a
        if keys[pygame.K_s]:
            self.x += -PlayerSpeed * cos_a
            self.y += -PlayerSpeed * sin_a
        if keys[pygame.K_a]:
            self.x += PlayerSpeed * sin_a
            self.y += -PlayerSpeed * cos_a
        if keys[pygame.K_d]:
            self.x += -PlayerSpeed * sin_a
            self.y += PlayerSpeed * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02
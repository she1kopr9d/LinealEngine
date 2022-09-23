from cgitb import text
from settings import *

text_map = [
    'WWWWWWWWWWWW',
    'W.W........W',
    'W.W........W',
    'W.W....W...W',
    'W.W....W...W',
    'W.....WWW..W',
    'W..........W',
    'WWWWWWWWWWWW'
]

world_map = set()

for j, row in enumerate(text_map):
    for i, wall in enumerate(row):
        if wall == 'W':
            world_map.add((i * TILESIZE, j * TILESIZE))
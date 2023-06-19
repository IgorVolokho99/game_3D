from settings import *

map_list = [
    'SSSSSSSSSSSS',
    'S......S...S',
    'S..SSS...S.S',
    'S....S..SS.S',
    'S..S....S..S',
    'S..S...SSS.S',
    'S....S.....S',
    'SSSSSSSSSSSS'
]

coor_s = set()
for j, stroka in enumerate(map_list):
    for i, char in enumerate(stroka):
        if char == 'S':
            coor_s.add((i * TILE1, j * TILE2))


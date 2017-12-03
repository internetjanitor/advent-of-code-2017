#!/usr/bin/env python

from collections import defaultdict

goal=312051

coords = defaultdict(dict)
digit = defaultdict(dict)

num = 1
x,y = 0,0

coords[x][y] = num
digit[num]['x'] = x
digit[num]['y'] = y

x += 1 # START RIGHT

while num < goal:
    num += 1
    coords[x][y] = num
    digit[num]['x'] = x
    digit[num]['y'] = y

    if y in coords.get(x-1, {}) and y+1 not in coords[x] and y-1 not in coords[x]:
        y += 1 # UP
    elif y-1 in coords[x] and y+1 not in coords[x] and y not in coords.get(x-1, {}):
        x -= 1 # LEFT
    elif y-1 not in coords[x] and y+1 not in coords[x] and y in coords.get(x+1, {}):
        y -= 1 # DOWN
    elif y-1 not in coords[x] and y+1 in coords[x] and y in coords.get(x+1, {}):
        y -= 1 # DOWN
    elif y+1 in coords[x] and y-1 not in coords[x] and y not in coords.get(x+1, {}):
        x += 1 # RIGHT
    elif y in coords.get(x-1, {}) and y+1 in coords[x] and y-1 not in coords[x]:
        x += 1 # RIGHT
    elif y in coords.get(x-1, {}) and y+1 not in coords[x] and y-1 in coords[x]:
        y += 1 # UP

print abs(digit[goal]['x']) + abs(digit[goal]['y'])

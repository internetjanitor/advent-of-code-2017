#!/usr/bin/env python

from collections import defaultdict

goal=312051

coords = defaultdict(dict)

def adjacent_sum(x, y):
    sum = 0
    if coords[x].get(y-1, {}):
        sum += coords[x][y-1]
    if coords[x].get(y+1, {}):
        sum += coords[x][y+1]
    if coords.get(x-1, {}):
        if coords[x-1].get(y, {}):
            sum += coords[x-1][y]
        if coords[x-1].get(y-1, {}):
            sum += coords[x-1][y-1]
        if coords[x-1].get(y+1, {}):
            sum += coords[x-1][y+1]
    if coords.get(x+1, {}):
        if coords[x+1].get(y, {}):
            sum += coords[x+1][y]
        if coords[x+1].get(y-1, {}):
            sum += coords[x+1][y-1]
        if coords[x+1].get(y+1, {}):
            sum += coords[x+1][y+1]
    return sum

num = 1
x,y = 0,0

coords[x][y] = num
notfound = True

x += 1 # START RIGHT

while num < goal:
    num += 1

    sum = adjacent_sum(x, y)
    if sum > goal and notfound:
        print sum
        notfound = False
    coords[x][y] = sum

    if num == goal:
        print abs(x) + abs(y)
    
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

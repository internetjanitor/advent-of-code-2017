#!/usr/bin/env python

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

count = 0
count2 = 0
for l in lines:
    words = l.split()
    if len(words) == len(set(words)):
        count += 1
    words = [str(sorted(list(word))) for word in words]
    if len(words) == len(set(words)):
        count2 += 1

print count
print count2

DEBUG = print if True else lambda *s: None

from itertools import groupby
from operator import sub

adj = lambda v1, v2: True if sum(map(abs, map(sub, v1, v2))) == 1 else False

# Input data ranges: x = 1--19, y = 0--19, z = 0--18
voxels = []
with open('input18', 'r') as file:
    for line in file:
        x, y, z = map(int, line.rstrip('\n').split(','))
        voxels.append((x,y,z),)

sa = 6 * len(voxels)

voxels.sort(key=lambda e:e[0])
for _, group in groupby(voxels, key=lambda e:e[0]):
    g = sorted(group, key=lambda e:e[1])
    for _, group2 in groupby(g, key=lambda e:e[1]):
        g2 = sorted(group2, key=lambda e:e[2])
        for v1, v2 in zip(g2, g2[1:]):
            sa -= 2 if adj(v1, v2) else 0

voxels.sort(key=lambda e:e[1])
for _, group in groupby(voxels, key=lambda e:e[1]):
    g = sorted(group, key=lambda e:e[2])
    for _, group2 in groupby(g, key=lambda e:e[2]):
        g2 = sorted(group2, key=lambda e:e[0])
        for v1, v2 in zip(g2, g2[1:]):
            sa -= 2 if adj(v1, v2) else 0

voxels.sort(key=lambda e:e[2])
for _, group in groupby(voxels, key=lambda e:e[2]):
    g = sorted(group, key=lambda e:e[0])
    for _, group2 in groupby(g, key=lambda e:e[0]):
        g2 = sorted(group2, key=lambda e:e[1])
        for v1, v2 in zip(g2, g2[1:]):
            sa -= 2 if adj(v1, v2) else 0

print(f'Part A: {sa}')
print(f'Part B: {0}')

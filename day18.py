DEBUG = print if True else lambda *s: None

from itertools import groupby
from operator import sub

adj = lambda v1, v2: map(sub, v1, v2)

DEBUG(list(adj([5,3,2],[1,2,0])))  # Expect [4,1,2]

# Input data ranges: x = 1--19, y = 0--19, z = 0--18
voxels = []
with open('input18', 'r') as file:
    cc = 0  # TODO-debug
    for line in file:
        cc += 1
        x, y, z = map(int, line.rstrip('\n').split(','))
        voxels.append((x,y,z),)
        if cc == 6:
            break

sa = 6 * len(voxels)

voxels.sort(key=lambda e:e[0])
DEBUG(voxels)
for v, g in groupby(voxels, key=lambda e:e[0]):
    print(v, g)
    for vox in g:
        print(vox)


print(f'Part A: {0}')
print(f'Part B: {0}')

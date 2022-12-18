DEBUG = print if True else lambda *s: None

UNKNOWN_SPACE = 0
UNKNOWN_FILLED = 1
EXTERIOR_SPACE = 2
EXTERIOR_FILLED = 4
INTERIOR_SPACE = 8
INTERIOR_FILLED = 16

print(\
'UNKNOWN_SPACE = 0\n' +
'UNKNOWN_FILLED = 1\n' +
'EXTERIOR_SPACE = 2\n' +
'EXTERIOR_FILLED = 4\n' +
'INTERIOR_SPACE = 8\n' +
'INTERIOR_FILLED = 16\n')

from itertools import groupby
from operator import sub

adj = lambda v1, v2: True if sum(map(abs, map(sub, v1, v2))) == 1 else False

def assign_adj_relation_to_voxel(v):
    if v == (2,2,2):
        DEBUG('LOOK HERE')  # TODO-debug
    x, y, z = v[0], v[1], v[2]
    vtype = voxel_seen(v)

    f = lambda i: [v[i]-1, v[i]+1]
    cx, cy, cz = f(0), f(1), f(2)

    for ax in cx:
        avtype = voxel_seen[(ax, y, z)]
        if vtype == UNKNOWN_FILLED and (avtype == EXTERIOR_FILLED or avtype == EXTERIOR_SPACE):
            voxel_seen[v] = EXTERIOR_FILLED; return
        if vtype == UNKNOWN_SPACE and avtype == EXTERIOR_SPACE:
            voxel_seen[v] = EXTERIOR_SPACE; return

    for ay in cy:
        avtype = voxel_seen[(x, ay, z)]
        if vtype == UNKNOWN_FILLED and (avtype == EXTERIOR_FILLED or avtype == EXTERIOR_SPACE):
            voxel_seen[v] = EXTERIOR_FILLED; return
        if vtype == UNKNOWN_SPACE and avtype == EXTERIOR_SPACE:
            voxel_seen[v] = EXTERIOR_SPACE; return

    for az in cz:
        avtype = voxel_seen[(x, y, az)]
        if vtype == UNKNOWN_FILLED and (avtype == EXTERIOR_FILLED or avtype == EXTERIOR_SPACE):
            voxel_seen[v] = EXTERIOR_FILLED; return
        if vtype == UNKNOWN_SPACE and avtype == EXTERIOR_SPACE:
            voxel_seen[v] = EXTERIOR_SPACE; return

# Input data ranges: x = 1--19, y = 0--19, z = 0--18
voxels = []
min_x, min_y, min_z =  30,  30,  30
max_x, max_y, max_z = -30, -30, -30
with open('sample18', 'r') as file:
#with open('input18', 'r') as file:
    for line in file:
        x, y, z = map(int, line.rstrip('\n').split(','))
        min_x, min_y, min_z = min(min_x, x), min(min_y, y), min(min_z, z)
        max_x, max_y, max_z = max(max_x, x), max(max_y, y), max(max_z, z)
        voxels.append((x,y,z),)  # Mark UNSEEN

voxel_lookup = set(voxels)

voxel_seen = dict.fromkeys([(u,v,w) for u in range(min_x,1+max_x) for v in range(min_y,1+max_y) for w in range(min_z,1+max_z)], UNKNOWN_SPACE)
voxel_seen |= dict.fromkeys(voxels, UNKNOWN_FILLED)

for u in range(min_x, 1+max_x):
    for v in range(min_y, 1+max_x):
        for w in [min_z, max_z]:
            check = (u,v,w)
            if check in voxel_lookup:
                voxel_seen[check] = EXTERIOR_FILLED
            else:
                voxel_seen[check] = EXTERIOR_SPACE

for u in range(min_x, 1+max_x):
    for v in [min_y, max_x]:
        for w in range(min_z, 1+max_z):
            check = (u,v,w)
            if check in voxel_lookup:
                voxel_seen[check] = EXTERIOR_FILLED
            else:
                voxel_seen[check] = EXTERIOR_SPACE

for u in [min_x, max_x]:
    for v in range(min_y, 1+max_x):
        for w in range(min_z, 1+max_z):
            check = (u,v,w)
            if check in voxel_lookup:
                voxel_seen[check] = EXTERIOR_FILLED
            else:
                voxel_seen[check] = EXTERIOR_SPACE

old_vrc = None
smallest_range = min(max_x-min_x, max_y-min_y, max_z-min_z)
while True:
    for f in range(1, smallest_range//2):  # TODO: minus 1 or not?
        for u in range(min_x+f, 1+max_x-f):
            for v in range(min_y+f, 1+max_x-f):
                for w in [min_z+f, max_z-f]:
                    assign_adj_relation_to_voxel(u,v,w)

        for u in range(min_x+f, 1+max_x-f):
            for v in [min_y+f, max_x-f]:
                for w in range(min_z+f, 1+max_z-f):
                    assign_adj_relation_to_voxel(u,v,w)

        for u in [min_x+f, max_x-f]:
            for v in range(min_y+f, 1+max_x-f):
                for w in range(min_z+f, 1+max_z-f):
                    assign_adj_relation_to_voxel(u,v,w)

    voxel_relation_counts = [sum(map((i).__eq__, voxel_seen.values())) for i in [0,1,2,4,8,16]]
    DEBUG(f'0,1,2,4,8,16: {voxel_relation_counts}')
    if old_vrc is not None:
        if all([i == j for i, j in zip(voxel_relation_counts, old_vrc)]):
            break
    old_vrc = voxel_relation_counts

    for f in range(smallest_range//2, 1, -1):  # TODO: correct?
        for u in range(min_x+f, 1+max_x-f):
            for v in range(min_y+f, 1+max_x-f):
                for w in [min_z+f, max_z-f]:
                    assign_adj_relation_to_voxel(u,v,w)

        for u in range(min_x+f, 1+max_x-f):
            for v in [min_y+f, max_x-f]:
                for w in range(min_z+f, 1+max_z-f):
                    assign_adj_relation_to_voxel(u,v,w)

        for u in [min_x+f, max_x-f]:
            for v in range(min_y+f, 1+max_x-f):
                for w in range(min_z+f, 1+max_z-f):
                    assign_adj_relation_to_voxel(u,v,w)

DEBUG('\n'.join(map(str,list(voxel_seen.items()))))

# TODO: - EXTERIOR_FILLED touching UNKNOWN_FILLED --> both EXTERIOR_FILLED.
#       - EXTERIOR_FILLED touching UNKNOWN_SPACE --> no change.
#       - EXTERIOR_SPACE touching UNKNOWN_SPACE --> both EXTERIOR_SPACE.
#       - EXTERIOR_SPACE touching UNKNOWN_FILLED --> EXTERIOR_FILLED.
# TODO: 1. Shrink search space one-by-one until u, v, or w has collapsed.
#       2. Make a note of number of exterior values.
#       3. Expand fully and shrink fully ("cycle").
#       4. If number is unchanged, change all UNKNOWN_SPACE to INTERIOR_SPACE and UNKNOWN_FILLED (if any) to INTERIOR_FILLED.
#       5. If number changes, cycle again and repeat until number is unchanged.
# TODO: - Surface area will be subtracted by 2 on each adjacent face where INTERIOR_SPACE touches EXTERIOR_FILLED.
#       - Subtract by 6 for any INTERIOR_FILLED.

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

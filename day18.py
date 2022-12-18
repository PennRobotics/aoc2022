DEBUG = print if True else lambda *s: None

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
DEBUG(*voxels)

print(f'Part A: {0}')
print(f'Part B: {0}')

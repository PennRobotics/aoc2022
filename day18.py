DEBUG = print if True else lambda *s: None

# Input data ranges: x = 1--19, y = 0--19, z = 0--18
voxels = []
with open('input18', 'r') as file:
    cc = 0
    for line in file:
        cc += 1  # TODO-debug
        x, y, z = map(int, line.rstrip('\n').split(','))
        voxels.append((x,y,z),)
        if cc == 10:
            break

DEBUG(voxels)

sort(voxels, key=voxels[0])
DEBUG(voxels)

sort(voxels, key=voxels[1])
DEBUG(voxels)

print(f'Part A: {0}')
print(f'Part B: {0}')

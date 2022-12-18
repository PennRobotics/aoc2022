DEBUG = print if True else lambda *s: None

voxels = dict()
with open('input18', 'r') as file:
    min_x, min_y, min_z = 0, 0, 0
    max_x, max_y, max_z = 0, 0, 0
    for line in file:
        x, y, z = map(int, line.rstrip('\n').split(','))
        DEBUG((x,y,z))
        min_x, max_x = min(min_x, x), max(max_x, x)
        min_y, max_y = min(min_y, y), max(max_y, y)
        min_z, max_z = min(min_z, z), max(max_z, z)
        break

DEBUG((min_x, max_x))
DEBUG((min_y, max_y))
DEBUG((min_z, max_z))

print(f'Part A: {0}')
print(f'Part B: {0}')

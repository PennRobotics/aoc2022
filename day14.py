DEBUG = print if False else lambda *s: None

from itertools import count

MIN_X = 462
MAX_X = 517
MAX_Y = 162

impact_y = None

rock_set = set()
rock_set |= set((x,50) for x in range(462,518))
print(rock_set)

sand_set = set()

# x (462, 517)
# y (13, 162)
def drop():
    global impact_y, rock_set, sand_set
    y = impact_y - 2 if impact_y else 0
    x = 500
    while True:
        if set([(x, y+1)]) & (rock_set | sand_set):
            if set([(x-1, y+1)]) & (rock_set | sand_set):
                if set([(x+1, y+1)]) & (rock_set | sand_set):
                    sand_set |= set([(x, y)])
                    return 0
                else:
                    x += 1; y += 1
            else:
                x += -1; y += 1
        else:
            y += 1
        if x < 462 or x > 517 or y > 162:  # TODO: hardcoded bounds
            return -1

#with open('sample14', 'r') as file:
with open('input14', 'r') as file:
    coords = file.read().rstrip('\n').replace('\n',' -> ').split(' -> ')
x = []; y = []
for coord in coords:
    xs, ys = coord.split(',')
    x.append(int(xs))
    y.append(int(ys))
print((min(x), max(x)))
print((min(y), max(y)))

print(sand_set)
drop(); print(sand_set)
drop(); print(sand_set)
drop(); print(sand_set)
drop(); print(sand_set)
drop(); print(sand_set)

print(f'Part A: {0}')
print(f'Part B: {0}')

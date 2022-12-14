DEBUG = print if False else lambda *s: None

from itertools import count

# TODO: hardcoded bounds
MIN_X = 462
MAX_X = 517
MAX_Y = 162

impact_y = None
rock_set = set()
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
        if x < MIN_X or x > MAX_X or y > MAX_Y:
            return -1

with open('sample14', 'r') as file:
#with open('input14', 'r') as file:
    rock_waypoints_list = file.read().rstrip('\n').split('\n')
for rock_waypoints in rock_waypoints_list:
    rock_waypoints = rock_waypoints.split(' -> ')
    print(rock_waypoints)
    for i in range(len(rock_waypoints) - 1):
        sx, sy, ex, ey = map(lambda s: int(s), ','.join([rock_waypoints[i], rock_waypoints[i+1]]).split(','))
        if sx > ex:
            sx, ex = ex, sx
        if sy > ey:
            sy, ey, = ey, sy
        if sx == ex:
            rock_set |= set((sx,y) for y in range(sy,1+ey))
        elif sy == ey:
            rock_set |= set((x,sy) for x in range(sx,1+ex))

    #print(coord)
    #print(set([tuple(map(lambda cs: int(cs), coord.split(',')))]))
    #xs, ys = coord.split(',')
    #x.append(int(xs))
    #y.append(int(ys))

def draw_board(sx,ex,ey):
    for y in range(0,1+ey):
        for x in range(sx,1+ex):
            if set([(x, y)]) & rock_set:
                c = '#'
            else:
                c = '.'
            print(c, end='')
        print('')

draw_board(494,503,9)

### print(sand_set)
### drop(); print(sand_set)
### drop(); print(sand_set)
### drop(); print(sand_set)
### drop(); print(sand_set)
### drop(); print(sand_set)

print(f'Part A: {0}')
print(f'Part B: {0}')

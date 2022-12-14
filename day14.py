# I'm sure there's a very simple, mathy solution (subtracting areas of triangles under horizontal surfaces)
# but we'll try the brute force method first and see if it finishes in a reasonable time. The bounds are
# already known, so the floor will just be plus/minus distance to opening (not infinite).

from itertools import count

# TODO: hardcoded bounds
# x (462, 517)
# y (13, 162)
MIN_X = 462
MAX_X = 517
MAX_Y = 162
CONTINUE = 0
FINISHED = -1

rock_set = set((x,164) for x in range(500-165,1+500+165))
sand_set = set()

def drop():
    global rock_set, sand_set
    x = 500
    y = 0
    while True:
        if set([(x, y+1)]) & (rock_set | sand_set):
            if set([(x-1, y+1)]) & (rock_set | sand_set):
                if set([(x+1, y+1)]) & (rock_set | sand_set):
                    sand_set |= set([(x, y)])
                    if x == 500 and y == 0:
                        return FINISHED
                    return CONTINUE
                else:
                    x += 1; y += 1
            else:
                x += -1; y += 1
        else:
            y += 1
        if y > MAX_Y + 2:
            return FINISHED

#with open('sample14', 'r') as file:
with open('input14', 'r') as file:
    rock_waypoints_list = file.read().rstrip('\n').split('\n')
for rock_waypoints in rock_waypoints_list:
    rock_waypoints = rock_waypoints.split(' -> ')
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

def draw_board(sx,ex,ey):
    for y in range(0,1+ey):
        for x in range(sx,1+ex):
            if set([(x, y)]) & rock_set:
                c = '#'
            elif set([(x, y)]) & sand_set:
                c = 'o'
            else:
                c = '.'
            print(c, end='')
        print('')

#draw_board(500-170,1+500+170,165)

for n in count(1):
    if drop() == FINISHED:
        break
    # Expect to get to between 20000 and 26000, probably closer to 26000
    if n % 100 == 0:
        print(n,flush=True)
    #if n % 100 == 0:
    #    draw_board(500-170,1+500+170,165)


#print(f'Part A: {len(sand_set)}')
print(f'Part B: {len(sand_set)}')

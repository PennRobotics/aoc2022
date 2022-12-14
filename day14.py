# I'm sure there's a very simple, mathy solution (subtracting areas of triangles under horizontal surfaces)
# but we'll try the brute force method first and see if it finishes in a reasonable time. The bounds are
# already known, so the floor will just be plus/minus distance to opening (not infinite).
# Brute force took about 20 minutes. I realized partway through, I can either solve by hand using the
# diagram or create a filled triangle and then unfill any triangles that are underneath three rocks:
#
#  .#######.
#  ..+++++#.
#  ...++++#.
#  ....+++..
#  .....+...
#  .........
#
# The + symbol denotes an unreachable area.

from itertools import count

MIN_X = 462
MAX_X = 517
MAX_Y = 162
CONTINUE = 0
FINISHED = -1

rock_set = set((x,MAX_Y+2) for x in range(500-(MAX_Y+3),1+500+(MAX_Y+3)))
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

for n in count(1):
    if drop() == FINISHED:
        break
    # Expect to get to between 20000 and 26000, probably closer to 26000 (answer was 25055)
    if n % 100 == 0:
        print(n,flush=True)


#print(f'Part A: {len(sand_set)}')
print(f'Part B: {len(sand_set)}')

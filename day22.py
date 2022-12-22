DEBUG = print if True else lambda *a,**kw: None

import re

CW = 1
CCW = -1
RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3
CIRCLE = 4

with open('input22', 'r') as file:
    maze, path = file.read().rstrip('\n').split('\n\n')
maze = maze.split('\n')
rowlen = max(map(len, maze))
maze = [row.ljust(rowlen + 1) for row in maze] + [' ' * (rowlen + 1)]
r, c, d = 1, 1 + maze[0].index('.'), RIGHT

DEBUG(path)

turn_fn = lambda t: CW if t == 'R' else CCW
path = tuple([(0, int(re.match('[0-9]+', path)[0]),)] + [(turn_fn(e[0]), int(e[1:])) for e in re.findall('[RL][0-9]+', path)])

DEBUG(path)

DEBUG('\n'.join([r + '|' for r in maze]))
DEBUG('----')

char_at = lambda p: maze[p[0]-1][p[1]-1]

vjump = {}
for col in range(1, len(maze[0])):
    vfind = (1, col,)
    while char_at(vfind) == ' ':
        vfind = (1 + vfind[0], col,)
    vend = vfind
    while char_at(vend) != ' ':
        vend = (1 + vend[0], col,)
    vjump[vfind] = vend
vjump |= dict((v,k) for k,v in vjump.items())

hjump = {}
for row in range(1, len(maze)):
    hfind = (row, 1,)
    while char_at(hfind) == ' ':
        hfind = (row, 1 + hfind[1],)
    hend = hfind
    while char_at(hend) != ' ':
        hend = (row, 1 + hend[1],)
    hjump[hfind] = hend
hjump |= dict((v,k) for k,v in hjump.items())

def next_move(row, col, di):
    if di == UP and (row,col,) in vjump:
        row, col = vjump[(row,col,)]
    if di == LEFT and (row,col,) in hjump:
        row, col = hjump[(row,col,)]
    row += 1*(di==DOWN) + -1*(di==UP)
    col += 1*(di==RIGHT) + -1*(di==LEFT)
    if di == DOWN and (row,col,) in vjump:
        row, col = vjump[(row,col,)]
    if di == RIGHT and (row,col,) in hjump:
        row, col = hjump[(row,col,)]
    return row, col

for turn, walk in path:
    maze[r-1] = maze[r-1][:c-1] + 'x' + maze[r-1][c:]
    d = (d + turn) % CIRCLE;
    for _ in range(walk):
        nr, nc = next_move(r, c, d)
        if char_at((nr,nc,)) == '#':
            #DEBUG('WALL!')
            continue
        else:
            r, c = nr, nc
            maze[r-1] = maze[r-1][:c-1] + 'x' + maze[r-1][c:]

DEBUG('\n'.join([r + '|' for r in maze]))
DEBUG('----', flush=True)

DEBUG(len(maze))  # 201
DEBUG(len(maze[0]))  # 151

#             v c=150
# o   +---+---x
#     | B | A |
#     +---z---+
#     | C |
# +---y---+
# | E | D |
# +---+---x
# | F |
# +---x  < r = 200

# Edge A Direction 0 -> D Direction 2
# Edge A Direction 1 -> C Direction 2
# Edge A Direction 2 -> B Direction 2
# Edge A Direction 3 -> F Direction 3
# Edge B Direction 0 -> A Direction 0
# Edge B Direction 1 -> C Direction 1
# Edge B Direction 2 -> E Direction 0
# Edge B Direction 3 -> F Direction 0
# Edge C Direction 0 -> A Direction 3
# Edge C Direction 1 -> D Direction 1
# Edge C Direction 2 -> E Direction 1
# Edge C Direction 3 -> B Direction 3
# Edge D Direction 0 -> A Direction 2
# Edge D Direction 1 -> F Direction 2
# Edge D Direction 2 -> E Direction 2
# Edge D Direction 3 -> C Direction 3
# Edge E Direction 0 -> D Direction 0
# Edge E Direction 1 -> F Direction 1
# Edge E Direction 2 -> B Direction 0
# Edge E Direction 3 -> C Direction 0
# Edge F Direction 0 -> D Direction 3
# Edge F Direction 1 -> A Direction 1
# Edge F Direction 2 -> B Direction 1
# Edge F Direction 3 -> E Direction 3

# TODO: Coordinate reversals @ x, y, z? (For instance, A going RIGHT or D going RIGHT both exit with rotational symmetry)

# TODO: create a jump map for all r,c,d returning next r,c,d
# Top and bottom edge of upper-half faces (while flat, e.g. face A, B, and C)
for jc in range(50,100):  # B, C
    jr = 0
    # TODO
    jr = 49
    # TODO
    jr = 50
    jr = 99
    pass
for jc in range(100,150):  # A
    jr = 0
    jr = 49
    # TODO
    pass
# Vertical-while-flat edges of top faces
for jr in range(0,50):  # A, B
    jc = 50
    jc = 99
    jc = 100
    jc = 149  # 10/24
    # ...
    pass
# Vertical edges of face C
for jr in range(50,100):
    jc = 50
    jc = 99  # 12/24
    pass
# Top and bottom horizontal-while-flat edges of faces F, E, and D
for jc in range(50,100):  # D
    jr = 100
    jr = 149
    pass
for jc in range(0,50):  # E, F
    jr = 100
    jr = 149
    jr = 150
    jr = 199  # 18/24
    pass
# Vertical-while-flat edges of faces F, E, and D
for jr in range(100,150):  # D, E
    jc = 0
    jc = 49
    jc = 50
    jc = 99  # 22/24
    pass
for jr in range(150,200):  # F
    jc = 0
    jc = 49
    pass


print(f'Part A: {1000*r + 4*c + d}')
print(f'Part B: {0}')

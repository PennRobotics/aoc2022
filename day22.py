DEBUG = print if False else lambda *a,**kw: None

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
            DEBUG('WALL!')
            continue
        else:
            r, c = nr, nc
            maze[r-1] = maze[r-1][:c-1] + 'x' + maze[r-1][c:]

DEBUG('\n'.join([r + '|' for r in maze]))
DEBUG('----', flush=True)

print(f'Part A: {1000*r + 4*c + d}')
print(f'Part B: {0}')

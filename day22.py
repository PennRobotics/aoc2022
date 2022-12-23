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

# Generate empty 3d maze for direction debugging
#maze = [' '*50 + '.'*100 + ' ']*50 + [' '*50 + '.'*50 + ' '*51]*50 + ['.'*100 + ' '*51]*50 + ['.'*50 + ' '*101]*50 + [' '*151]
#DEBUG(maze)
DEBUG('\n'.join(maze))
sr, sc, sd = 1, 1 + maze[0].index('.'), RIGHT

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

r, c, d = sr, sc, sd
for turn, walk in path:
    #maze[r-1] = maze[r-1][:c-1] + 'x' + maze[r-1][c:]
    d = (d + turn) % CIRCLE;
    for _ in range(walk):
        nr, nc = next_move(r, c, d)
        if char_at((nr,nc,)) != '#':
            r, c = nr, nc
            #maze[r-1] = maze[r-1][:c-1] + 'x' + maze[r-1][c:]

print(f'Part A: {1000*r + 4*c + d}')

DEBUG('\n'.join([r + '|' for r in maze]))
DEBUG('----', flush=True)

#              | c=150
# o   +---+---x
#     | B | A |
#     +---z---+
#     | C |
# +---y---+
# | E | D |
# +---+---x
# | F |
# +---x  _ r = 200

# Edge A Direction 0 (jc % 50 = 49) -> D Direction 2
# Edge A Direction 1 (jr % 50 = 49) -> C Direction 2
# Edge A Direction 2 (jc % 50 =  0) -> B Direction 2
# Edge A Direction 3 (jr % 50 =  0) -> F Direction 3
# Edge B Direction 0         ->        A Direction 0
# Edge B Direction 1         ->        C Direction 1
# Edge B Direction 2         ->        E Direction 0
# Edge B Direction 3         ->        F Direction 0
# Edge C Direction 0         ->        A Direction 3
# Edge C Direction 1         ->        D Direction 1
# Edge C Direction 2         ->        E Direction 1
# Edge C Direction 3         ->        B Direction 3
# Edge D Direction 0         ->        A Direction 2
# Edge D Direction 1         ->        F Direction 2
# Edge D Direction 2         ->        E Direction 2
# Edge D Direction 3         ->        C Direction 3
# Edge E Direction 0         ->        D Direction 0
# Edge E Direction 1         ->        F Direction 1
# Edge E Direction 2         ->        B Direction 0
# Edge E Direction 3         ->        C Direction 0
# Edge F Direction 0         ->        D Direction 3
# Edge F Direction 1         ->        A Direction 1
# Edge F Direction 2         ->        B Direction 1
# Edge F Direction 3         ->        E Direction 3

# HARDCODED JUMP MAP FOR ALL R,C,D RETURNING NEXT R,C,D
# =====================================================
jump_list = {}
# Top and bottom edge of upper-half faces (while flat, e.g. face A, B, and C)
for jc in range(51,101):  # B, C
    jr, jd = 1, UP  # B3 -> F0
    tr, tc, td = jc + 100, 1, RIGHT
    jump_list[(jr,jc,jd,)] = (tr,tc,td,)

    #jr, jd = 49, DOWN  # B1 -> C1 (no jump needed)

    #jr, jd = 50, UP  # C3 -> B3

    #jr, jd = 99, DOWN  # C1 -> D1

for jc in range(101,151):  # A
    jr, jd = 1, UP  # A3 -> F3
    tr, tc, td = 200, jc - 100, UP
    jump_list[(jr,jc,jd,)] = (tr,tc,td,)

    jr, jd = 50, DOWN  # A1 -> C2
    tr, tc, td = jc - 50, 100, LEFT
    jump_list[(jr,jc,jd,)] = (tr,tc,td,)

# Vertical-while-flat edges of top faces
for jr in range(1,51):  # A, B
    jc, jd = 51, LEFT  # B2 -> E0
    tr, tc, td = 151 - jr, 1, RIGHT
    jump_list[(jr,jc,jd,)] = (tr,tc,td,)

    #jc, jd = 99, RIGHT  # B0

    #jc, jd = 100, LEFT  # A2

    jc, jd = 150, RIGHT  # A0 -> D2
    tr, tc, td = 151 - jr, 100, LEFT
    jump_list[(jr,jc,jd,)] = (tr,tc,td,)

# Vertical edges of face C
for jr in range(51,101):
    jc, jd = 51, LEFT  # C2 -> E1
    tr, tc, td = 101, jr - 50, DOWN
    jump_list[(jr,jc,jd,)] = (tr,tc,td,)

    jc, jd = 100, RIGHT  # C0 -> A3
    tr, tc, td = 50, jr + 50, UP
    jump_list[(jr,jc,jd,)] = (tr,tc,td,)

# Top and bottom horizontal-while-flat edges of faces F, E, and D
for jc in range(51,101):  # D
    #jr, jd = 100, UP  # D3 -> C3

    jr, jd = 150, DOWN  # D1 -> F2
    tr, tc, td = jc + 100, 50, LEFT
    jump_list[(jr,jc,jd,)] = (tr,tc,td,)

for jc in range(1,51):  # E, F
    jr, jd = 101, UP  # E3 -> C0
    tr, tc, td = jc + 50, 51, RIGHT
    jump_list[(jr,jc,jd,)] = (tr,tc,td,)

    #jr, jd = 149, DOWN  # E1 -> F1

    #jr, jd = 150, UP  # F3 -> E3

    jr, jd = 200, DOWN  # F1 -> A1
    tr, tc, td = 1, jc + 100, DOWN
    jump_list[(jr,jc,jd,)] = (tr,tc,td,)

# Vertical-while-flat edges of faces F, E, and D
for jr in range(101,151):  # D, E
    jc, jd = 1, LEFT  # E2 -> B0
    tr, tc, td = 151 - jr, 51, RIGHT
    jump_list[(jr,jc,jd,)] = (tr,tc,td,)

    #jc, jd = 49, RIGHT  # E0 -> D0

    #jc, jd = 50, LEFT  # D2 -> E2

    jc, jd = 100, RIGHT  # D0 -> A2
    tr, tc, td = 151 - jr, 150, LEFT
    jump_list[(jr,jc,jd,)] = (tr,tc,td,)

for jr in range(151,201):  # F
    jc, jd = 1, LEFT  # F2 -> B1
    tr, tc, td = 1, jr - 100, DOWN
    jump_list[(jr,jc,jd,)] = (tr,tc,td,)

    jc, jd = 50, RIGHT  # F0 -> D3
    tr, tc, td = 150, jr - 100, UP
    jump_list[(jr,jc,jd,)] = (tr,tc,td,)

DEBUG(len(jump_list))

def next_3d_move(row, col, di):
    if (row,col,di,) in jump_list:
        DEBUG(f'jump {(row,col,di,)} -> {jump_list[(row,col,di,)]}')
        return jump_list[(row,col,di,)]
    return (row + 1*(di==DOWN) + -1*(di==UP), col + 1*(di==RIGHT) + -1*(di==LEFT), di,)

r, c, d = sr, sc, sd
for turn, walk in path:
    DEBUG('\n'.join([r + '|' for r in maze]))
    DEBUG('----')
    #keypress = input()  # TODO-debug
    maze[r-1] = maze[r-1][:c-1] + 'x' + maze[r-1][c:]
    d = (d + turn) % CIRCLE;
    for _ in range(walk):
        nr, nc, nd = next_3d_move(r, c, d)
        if char_at((nr,nc,)) != '#':
            r, c, d = nr, nc, nd
            maze[r-1] = maze[r-1][:c-1] + 'x' + maze[r-1][c:]

DEBUG(path)

DEBUG('\n'.join([r + '|' for r in maze]))
DEBUG('----')

print(f'Part B: {1000*r + 4*c + d}')  # 121245 is too high

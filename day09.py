n = [(0, 0)] * 10
n1_visited = set((n[1],))
n9_visited = set((n[9],))
head_decoder = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
tail_decoder = {
        (-2,-2): (-1,-1),
        (-2,-1): (-1,-1),
        (-2, 0): (-1, 0),
        (-2, 1): (-1, 1),
        (-2, 2): (-1, 1),
        (-1,-2): (-1,-1),
        (-1,-1): ( 0, 0),
        (-1, 0): ( 0, 0),
        (-1, 1): ( 0, 0),
        (-1, 2): (-1, 1),
        ( 0,-2): ( 0,-1),
        ( 0,-1): ( 0, 0),
        ( 0, 0): ( 0, 0),
        ( 0, 1): ( 0, 0),
        ( 0, 2): ( 0, 1),
        ( 1,-2): ( 1,-1),
        ( 1,-1): ( 0, 0),
        ( 1, 0): ( 0, 0),
        ( 1, 1): ( 0, 0),
        ( 1, 2): ( 1, 1),
        ( 2,-2): ( 1,-1),
        ( 2,-1): ( 1,-1),
        ( 2, 0): ( 1, 0),
        ( 2, 1): ( 1, 1),
        ( 2, 2): ( 1, 1) }
move_n = lambda i, v: (n[i][0] + v[0], n[i][1] + v[1])
offset = lambda i: (n[i-1][0] - n[i][0], n[i-1][1] - n[i][1])

with open('input09', 'r') as file:
    for line in file:
        path, dist = line.rstrip('\n').split(' ')
        for _ in range(int(dist)):
            n[0] = move_n(0, head_decoder[path])
            for a in range(1, 10):
                n[a] = move_n(a, tail_decoder[offset(a)])
            n1_visited = n1_visited.union((n[1],))
            n9_visited = n9_visited.union((n[9],))

print(f'Part A: {len(n1_visited)}')
print(f'Part B: {len(n9_visited)}')

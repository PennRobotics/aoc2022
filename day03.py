a_total = 0; b_total = 0
priorities = dict(map(lambda p: (p[1], p[0]), enumerate(' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')))
idx = 0

with open('input03', 'r') as file:
    for line in file:
        line = line[:-1]

        sz = len(line) >> 1
        l, r = set(line[:sz]), set(line[sz:])
        com = ''.join(l & r)
        a_total += priorities[com]

        if idx == 0:
            l_set = set(line)
        elif idx == 1 or idx == 2:
            l_set &= set(line)
        elif idx == 3:
            r_set = set(line)
        elif idx == 4 or idx == 5:
            r_set &= set(line)
        idx = idx + 1 if idx < 5 else 0
        if idx == 0:
            b_total += priorities[''.join(l_set)] + priorities[''.join(r_set)]

print(f'Part A: {a_total}')

print(f'Part B: {b_total}')

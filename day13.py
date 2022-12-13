DEBUG = print if True else lambda *s: None

from itertools import zip_longest, count
from functools import cmp_to_key

YES = 1
UNDECIDED = 0
NO = -1

indent = -2

def check_lists(l, r):
    global indent
    indent += 2
    DEBUG(''.join([' ']*indent) + f'- Compare {l} vs {r}')
    right_order = UNDECIDED
    for p in zip_longest(l, r):
        if not p[0]:
            DEBUG(''.join([' ']*indent) + f'  - Compare {p[0]} vs {p[1]}')
            right_order = YES
            break
        if not p[1]:
            DEBUG(''.join([' ']*indent) + f'  - Compare {p[0]} vs {p[1]}')
            right_order = NO
            break
        if isinstance(p[0], int) and isinstance(p[1], int):
            DEBUG(''.join([' ']*indent) + f'  - Compare {p[0]} vs {p[1]}')
            if p[0] == p[1]:
                continue
            elif p[0] < p[1]:
                right_order = YES
            else:
                right_order = NO
            break
        list_l = p[0] if not isinstance(p[0], int) else [p[0]]
        list_r = p[1] if not isinstance(p[1], int) else [p[1]]
        right_order = check_lists(list_l, list_r)
        if right_order != UNDECIDED:
            break
    indent -= 2
    return right_order

i_sum = 0
#with open('input13', 'r') as file:
with open('fix13', 'r') as file:
    for i in count(1):
        DEBUG(f'== Pair {i} ==')
        left = eval(file.readline().rstrip('\n'))
        right = eval(file.readline().rstrip('\n'))

        i_sum += i if check_lists(left, right) == 1 else 0

        if file.readline() == '':
            break
        DEBUG()

    file.seek(0)
    contents = file.read().replace('\n\n', '\n')

# TODO-debug
contents = contents.rstrip('\n')
#contents += '[[2]]\n[[6]]'
packet_list = [eval(line) for line in contents.split('\n')]

for e in packet_list:
    print(e)

print('  -1: OUT-OF-ORDER,  0: EQUAL,  1: IN-ORDER  ')
print(f'`check_lists(...)` on e[0] and e[1]: {check_lists(packet_list[0],packet_list[1])}')
print(f'`check_lists(...)` on e[2] and e[4]: {check_lists(packet_list[2],packet_list[4])}')
print(f'`check_lists(...)` on e[2] and e[3]: {check_lists(packet_list[2],packet_list[3])}')

print('\nAfter sort:')
packet_list.sort(key=cmp_to_key(check_lists), reverse=True)
for e in packet_list:
    print(e)

import sys
sys.exit(0)

packet_div2 = 1 + packet_list.index([[2]])
packet_div6 = 1 + packet_list.index([[6]])

print(f'Part A: {i_sum}')
print(f'Part B: see script comments')

# Part A
# 8844 was too high (forgot to break early if right_order == False)
# 4860 was too low (added early break, suspecting an empty list is resulting False incorrectly)
# Switched from True/False to positive/zero/negative (comparison)

# Part B
# 24038 was too high
# Manually inspecting the output:
#     ...
#     [[[[1, 8, 4], [7, 5, ...
#     [[2], [], [[], 6, [[6, ...
#     [[2, [], 2, 8, 0], [4, ...
#     [[2]]
#     [[2, [[]], 2, [[5], ...
#     ...
# The packet for [[2]] is two lines too low, while the packet for [[6]] is five lines too low.
# The original guess of 24038 uses factors 119 and 202. The guess 117 x 197 (=23049) works.
# Forcing the return value of `check_lists` does not fix the Part B result.

class BlizzardNode:
    a = 0
    b = 2
    def __init__(self):
        pass

bn = BlizzardNode()
bn.a = 5
print(bn.a)
print(bn.b)

bn2 = BlizzardNode()
print(bn.a)

import sys
sys.exit(0)

### from collections import defaultdict
### from itertools import count
### 
### is_north_empty = lambda p: (p[0]-1, p[1]-1) not in elves and (p[0]-1, p[1]) not in elves and (p[0]-1, p[1]+1) not in elves
### is_south_empty = lambda p: (p[0]+1, p[1]-1) not in elves and (p[0]+1, p[1]) not in elves and (p[0]+1, p[1]+1) not in elves
### is_west_empty = lambda p: (p[0]-1, p[1]-1) not in elves and (p[0], p[1]-1) not in elves and (p[0]+1, p[1]-1) not in elves
### is_east_empty = lambda p: (p[0]-1, p[1]+1) not in elves and (p[0], p[1]+1) not in elves and (p[0]+1, p[1]+1) not in elves
### is_perimeter_empty = lambda p: is_north_empty(p) and is_south_empty(p) and is_west_empty(p) and is_east_empty(p)
### 
### north_of = lambda p: (p[0]-1, p[1])
### south_of = lambda p: (p[0]+1, p[1])
### west_of = lambda p: (p[0], p[1]-1)
### east_of = lambda p: (p[0], p[1]+1)
### 
### heading_at_round_start = 1j
### 
#with open('sample24','r') as file:
with open('input24','r') as file:
    blizzard = [line[:-1] for line in file]
### ROW_MIN, ROW_MAX, COL_MIN, COL_MAX = 0, len(puzzle)-1, 0, len(puzzle[0])-1
### elves = set([(row_nr, col_nr) for row_nr, row in enumerate(puzzle) for col_nr, ch in enumerate(row) if ch == '#'])
### 
### def get_row_col_bounds():
###     rows, cols = zip(*[(r,c) for r,c in elves])
###     return min(rows), max(rows), min(cols), max(cols)
### 
### def draw_board():
###     min_row, max_row, min_col, max_col = get_row_col_bounds()
###     row_range = range(min(min_row, ROW_MIN), 1 + max(max_row, ROW_MAX))
###     col_range = range(min(min_col, COL_MIN), 1 + max(max_col, COL_MAX))
###     for r in row_range:
###         for c in col_range:
###             print(f'{"#" if (r,c) in elves else "."}', end='')
###         print()
###     print(flush=True)
### 
### #print('== Initial State ==')
### #draw_board()
### 
### for round_nr in count(1):
###     round_dir = 1j**((round_nr-1)%4)
###     proposed_moves = defaultdict(lambda:[])
###     for elf in sorted(elves):
###         if is_perimeter_empty(elf):
###             proposed_moves[elf].append(elf)
###             continue
###         for try_dir in [round_dir * 1j**j for j in range(4)]:
###             match try_dir:
###                 case 1:
###                     if wants_to_move := is_north_empty(elf):
###                         proposed_moves[north_of(elf)].append(elf)
###                 case 1j:
###                     if wants_to_move := is_south_empty(elf):
###                         proposed_moves[south_of(elf)].append(elf)
###                 case -1:
###                     if wants_to_move := is_west_empty(elf):
###                         proposed_moves[west_of(elf)].append(elf)
###                 case -1j:
###                     if wants_to_move := is_east_empty(elf):
###                         proposed_moves[east_of(elf)].append(elf)
###             if wants_to_move:
###                 break
###         if not wants_to_move:
###             proposed_moves[elf].append(elf)
### 
###     next_elves = set()
###     for pmove, movers in proposed_moves.items():
###         if len(movers) > 1:
###             next_elves |= set(movers)
###         else:
###             next_elves |= set([pmove,])
### 
###     if elves == next_elves:
###         break
### 
###     elves = next_elves
###     #print(f'== End of Round {round_nr} ==')
###     #draw_board()
### 
###     if round_nr == 10:
###         r1, r2, c1, c2 = get_row_col_bounds()
### 
print(f'Part A: {0}')
print(f'Part B: {0}')

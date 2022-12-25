# Step 1: Connect blizzard in a graph
# Step 2: Update position of blizzard each step
# Step 3: Party state will be (position, time)
# Step 4: Only allow valid moves
# Step 5: Optimum time starts as Manhattan distance to finish
# Step 6: Create multiple BFS trees of all possible paths from the start plus
#           t number of all possible paths from the finish going backward
#           (t[0] is optimum time e.g. no waits, t[-1] is t moves delayed)
#           (BFS should probably have number of branches/leaves at each node.)
# Step 7: Because each path will have time and position, two things happen:
#           a. The start BFS and finish BFS will not meet at wrong time.
#           b. The finish BFS can have its shortest delay paths eliminated
#                any time either BFS is forced to wait.
# It shouldn't be super important, but the state of each cell will be cyclic, i.e. every least common multiple of W & H,
#   but since there's supposed to be a solution, we won't have to deal with the BFS wrapping around on itself.
# Step 8: If this whole thing takes too long, figure out how to switch to
#           A*, D* Lite, whatever. There's probably a way to predict the
#           shortest path because obstacles will soon (a few moves away)
#           and predictably change the cost of a path.

from itertools import count

blizzard = []
#with open('sample24','r') as file:
with open('input24','r') as file:
    for rn, line in enumerate(file):
        for cn, ch in enumerate(line):
            if ch in '#.\n':
                continue
            blizzard.append(((rn, cn), (ch=='>') + 1j*(ch=='^') - (ch=='<') - 1j*(ch=='v')))
start, finish = (0, 1), (rn, cn-1)
current = start

path = [(current, 0)]

wrap = lambda n,mn,mx: (n-mn)%(mx-mn)+mn
hwrap = lambda n: wrap(1, cn)
vwrap = lambda n: wrap(1, rn)

min_t_left = lambda pt: finish[0]-pt[0] + finish[1]-pt[1]

for i in range(-3,10):
    print(f'{i}  --  {wrap(i,3,7)}')
    ### print(f'{i*1j}  --  {wrap(i*1j,3j,7j)}')

print(blizzard)
print(list(map(lambda a:a[0], blizzard)))

def print_valley(storm_list):
    for row in range(1 + finish[0]):
        for col in range(2 + finish[1]):
            #ch = 'x' if (row, col,) in map(lambda a:a[0], blizzard) else '.'
            ch = 'x' if (row, col,) in storm_list else '.'
            print(ch, end='')
        print()
    print()

start_bfs = []
finish_bfses = [[] * 10]
print(start_bfs, finish_bfses)

print_valley(list(map(lambda a:a[0], blizzard)))

simple = lambda c: (int(c.real), int(c.imag),)
for minute in count(1):
    storms = []
    for pt, heading in blizzard:
        ### print(pt, heading)
        storms.append(simple(complex(pt[0], pt[1]) + minute*heading))  # TODO: modulo
    print_valley(storms)
    input()

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

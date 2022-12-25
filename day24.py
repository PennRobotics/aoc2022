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

wrap = lambda n,mn,mx: (n-mn)%(mx-mn)+mn
vwrap = lambda n: wrap(n, 1, rn)
hwrap = lambda n: wrap(n, 1, cn)

min_t_left = lambda pt: finish[0]-pt[0] + finish[1]-pt[1]

def print_valley(storm_list):
    for row in range(1 + finish[0]):  # TODO: off-by-one?
        for col in range(2 + finish[1]):  # TODO: off-by-one?
            ch = 'x' if (row, col,) in storm_list else '.'
            print(ch, end='')
        print()
    print()

current = start
path = [(current, 0)]

start_bfs = []
finish_bfses = [[] * 10]
print(start_bfs, finish_bfses)

print_valley(list(map(lambda a:a[0], blizzard)))

simple = lambda c: (vwrap(int(c.imag)), hwrap(int(c.real)),)
for minute in count(1):
    storms = []  # TODO: add walls here
    for pt, heading in blizzard:
        ### print(pt, heading)
        storms.append(simple(complex(pt[1], pt[0]) + minute*heading))
    print_valley(storms)
    input()

print(f'Part A: {0}')
print(f'Part B: {0}')

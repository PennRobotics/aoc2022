DEBUG = print if True else lambda *s: None

class Node:
    def __init__(self, val, head=False):
        global global_head
        self.val = val
        self.pr = None
        self.nx = None
        if head:
            global_head = self
        self.head = global_head

    def rerefer_chain_to_head(self):  # Call after assigning global_head.pr but before closing the circle
        global global_head
        redo_node = self
        redo_node.head = global_head
        while redo_node.pr != None:
            redo_node = redo_node.pr
            redo_node.head = global_head

    def jump_by_n(self, n):
        if n == 0:
            return
        travel_node = self
        if n > 0:
            for _ in range(n):
                travel_node = travel_node.nx
        if n < 0:
            for _ in range(-n):
                travel_node = travel_node.pr
        move_node = self._pop_node()
        travel_node._insert_node_after(move_node)

    def redefine_next_as(self, nx):
        self.nx = nx
        nx.pr = self

    def _pop_node(self):
        bf_node, af_node = self.pr, self.nx
        bf_node.redefine_next_as(af_node)
        self.nx, self.pr = None, None
        return self

    def _insert_node_after(self, node):
        af_node = self.nx
        self.redefine_next_as(node)
        node.redefine_next_as(af_node)


def print_node_segment(i, j):
    global global_head
    ni = global_head
    for _ in range(i):
        ni = ni.nx
    print('[', end='')
    nj = ni
    for _ in range(j-i):
        print(f'{nj.val}, ', end='')
        nj = nj.nx
    print(f'{nj.val}]', flush=True)

with open('sample20', 'r') as file:
#with open('input20', 'r') as file:
    values = [int(n) for n in file.read().rstrip('\n').split('\n')]
print(values)

global_head = None
first_n = Node(values[0])
last_n = first_n
docket = [first_n]
for v in values[1:]:
    nv = Node(v, head=(v==0))
    last_n.redefine_next_as(nv)
    docket.append(nv)
    last_n = nv
global_head.rerefer_chain_to_head()
last_n.redefine_next_as(first_n)

print_node_segment(2, 8)

for i, mvmt in enumerate(docket):
    DEBUG(type(mvmt.head))
    DEBUG(i)
    mvmt.jump_by_n(mvmt.val)
    if i < 2:
        print_node_segment(2, 8)
    else:
        print_node_segment(3, 9)




# In the naive implementation, a giant list is shifted from side-to-side, and the list
# members have a reference/key that determines which element is shifted next.
# Not only would this be a bit of a pain to program, it's computationally inefficient.
# Is there a way to create a "jump list" where the indices of each element are sorted
# and stored? Then, when compiling the final version of the list (or an intermediate
# list, if that is much more efficient or understandable) the elements are placed in
# the correct place.

# Example
# =======
#
# -5,  7,  2,  4,  0,  0,  0,  0,  1,  0
#
#  (0, -5)  -> (0, 5) = (0, 0-5+10)
#  (1,  7)  -> (1, 8)
#  (2,  2)  -> (2, 4)
#  (3,  4)  -> (3, 7)
#  (4,  0)  -> (4, 4)
#  (5,  0)  -> (5, 5)
#  (6,  0)  -> (6, 6)
#  (7,  0)  -> (7, 7)
#  (8,  1)  -> (8, 9)
#  (9,  0)  -> (9, 9)

# Next step
#  d   .   .   .   .   d   d   d   d   d
#  0,  7,  2,  4,  0, -5,  0,  0,  0,  1
# -5 jumps (0, 5)

#  .   d   d   d   d   d   d   d   d   .
#  0,  2,  4,  0, -5,  0,  0,  0,  7,  1
#  7 jumps (1, 8)

#  .   d   d   d   .   .   .   .   .   .
#  0,  4,  0,  2, -5,  0,  0,  0,  7,  1
#  2 jumps (1, 3)

#  .   d   d   d   d   d   .   .   .   .
#  0,  0,  2, -5,  0,  4,  0,  0,  7,  1
#  4 jumps (1, 5)

#  d   .   .   .   .   .   .   .   .   d
#  1,  0,  2, -5,  0,  4,  0,  0,  7,  0
#  1 jumps (9, 0)

#  Included range and shift direction? (and how to deal with shift indices shifting??)

#  a   0   0   0   0  +1  +1  +1  +1  +1
#  0   b  -1  -1  -1  -1  -1  -1  -1   0
#  0   c  -1  -1   0   0   0   0   0   0
#  0   d  -1  -1  -1  -1   0   0   0   0
# -1   0   0   0   0   0   0   0   0   e

# ======================================
# -1   0  -3  -3  -2  -1   0   0   0  +1

# -5,  7,  2,  4,  0,  0,  0,  0,  1,  0
#  1,  0,  2, -5,  0,  4,  0,  0,  7,  0

# Ground truth:
#  -5  -> (0, -7) / (0, 3)  = -7 (-2)
#   7  -> (1,  8)           =  7 ( 0)
#   2  -> (2,  2)           =  0 (-2)
#   4  -> (3,  5)           =  2 (-2)
#   0  -> (4,  1)           = -3 (-3)
#   0  -> (5,  4)           = -1 (-1)
#   0  -> (6,  6)           =  0 ( 0)
#   0  -> (7,  7)           =  0 ( 0)
#   1  -> (8,  0) / (8,10)  =  2 (+1)
#   0  -> (9,  9)           =  0 ( 0)
#
# One final thought: The last list element is always going to skip the correct number
# of other elements. Unfortunately, the second-to-last could be off by one without
# knowing the start or stop point of the last element. By this point, the entire
# landscape of values is completely different than in the beginning, so there's not
# a great way I can think of to immediately know where the last element should start
# or stop.


print(f'Part A: {0}')
print(f'Part B: {0}')

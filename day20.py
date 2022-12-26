DEBUG = print if True else lambda *s: None

class Node:
    def __init__(self, val):
        self.val = val
        self.pr = None
        self.nx = None

    def jump_by_n(self, n):
        if n == 0:
            return
        bf, af = self.pr, self.nx
        bf.redefine_next_as(af)
        if n > 0:
            target_node = self.nx
            for _ in range((n-1)%4999):
                target_node = target_node.nx
        if n < 0:
            target_node = self.pr
            for _ in range((-n)%4999):
                target_node = target_node.pr

        #   MOVING b:
        #
        #    +---------+
        #    |         |
        #    |         v
        # a [b] c d e f g h
        #
        # Link a (b.pr) to c (b.nx)
        # Link f (target) to b
        # Link b to g (target.nx)

        af_target_node = target_node.nx
        target_node.redefine_next_as(self)
        self.redefine_next_as(af_target_node)

    def redefine_next_as(self, nx):
        self.nx = nx
        nx.pr = self


def node_segment_list(i, j):
    ni = first_n
    while ni.val != 0:
        ni = ni.nx
    for _ in range(i):
        ni = ni.nx
    seg = [ni.val]
    for _ in range(j-i):
        ni = ni.nx
        seg.append(ni.val)
    return seg

#with open('sample20', 'r') as file:
with open('input20', 'r') as file:
    values = [int(n) for n in file.read().rstrip('\n').split('\n')]

first_n = Node(values[0])
last_n = first_n
docket = [first_n]
for v in values[1:]:
    nv = Node(v)
    last_n.redefine_next_as(nv)
    docket.append(nv)
    last_n = nv
last_n.redefine_next_as(first_n)

for mvmt in docket:
    mvmt.jump_by_n(mvmt.val)

part_a = sum(node_segment_list(1000, 1000) + node_segment_list(2000, 2000) + node_segment_list(3000, 3000))

print(f'Part A: {part_a}')

DKEY = 811589153
first_n = Node(values[0] * DKEY)
last_n = first_n
docket = [first_n]
for v in values[1:]:
    nv = Node(v * DKEY)
    last_n.redefine_next_as(nv)
    docket.append(nv)
    last_n = nv
last_n.redefine_next_as(first_n)

for mvmt in docket * 10:
    mvmt.jump_by_n(mvmt.val)

part_b = sum(node_segment_list(1000, 1000) + node_segment_list(2000, 2000) + node_segment_list(3000, 3000))

print(f'Part B: {part_b}')

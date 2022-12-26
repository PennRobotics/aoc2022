DEBUG = print if True else lambda *s: None

class Node:
    def __init__(self, val):
        self.val = val
        self.pr = None
        self.nx = None

    def jump_by_n(self, n):
        if n == 0:
            return
        travel_node = self
        if n > 0:
            for _ in range(n):
                travel_node = travel_node.nx
        if n < 0:
            for _ in range(-n+1):
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


def node_segment_list(i, j):
    ni = first_n
    while ni.val != 0:
        ni = ni.nx
    for _ in range(i):
        ni = ni.nx
    seg = [ni.val]
    nj = ni
    for _ in range(j-i):
        seg.append(nj.val)
        nj = nj.nx
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


print(f'Part A: {part_a}')  # 1644 is too low
print(f'Part B: {0}')

# Without much background here, I would plan to get the shortest connection distance
# between each node. I believe the way to do this is to keep a dictionary of each
# known connection. When a new connection is added, iterate through the known nodes
# and update if the new node has a shorter path to existing nodes.

# I think I recall BFS having a minimum path guarantee, so I'd use that after all
# node connections are made.

DEBUG = print if True else lambda *s: None

import re

class Node:
    def __init__(self, id, flow = -1):
        DEBUG(f'Valve {id} created with flow {flow}')
        self.id = id
        self.flow = flow
        self.dist = dict()
        pass

    def __str__(self):
        return f'Valve {self.id}, {self.flow} flow rate, {" + ".join([k for k, v in self.dist.items() if v == 1])}'

    def set_flow(self, flow):
        self.flow = flow

    def add_nodes(self, nodes):
        for n in nodes:
            DEBUG(f'{self.id} linked to {n}')
            if n not in valves:
                nn = Node(n)
                valves[n] = nn
                nn.add_nodes([self.id])
            self.dist[n] = 1


valves = dict()
pat = re.compile(r'^Valve (..)[^=]*=([0-9]*);.*valves? (.*)$')
with open('input16', 'r') as file:
    for line in file:
        mat = pat.match(line)
        valve, rate, tunnel_list = mat.group(1), mat.group(2), mat.group(3).split(', ')
        if valve in valves:
            DEBUG(f'Node {valve} already exists, set flow to {rate}.')
            n = valves[valve]
            n.set_flow(rate)
        else:
            n = Node(valve, rate)
            valves[valve] = n
        n.add_nodes(tunnel_list)

# print('\n'.join([str(valves[v]) for v in valves]))

print(f'Part A: {0}')
print(f'Part B: {0}')

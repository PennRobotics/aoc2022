# By graphing this (using dot/graphviz) three details become clear:
# 1. There are a lot of valuable nodes living at the end of a long chain, e.g. expensive to reach.
# 2. Lots of smaller-valued nodes are quickly reachable.
# 3. All possible paths will probably need to be enumerated (without time-wasting moves, BUT allowing backtracking to reach a new node).

# Less clear is if there will be a way to prune less efficient moves during path creation. I suppose this would be something
#   like a dictionary of all valued nodes reached by time t (beginning with the current node) where the dict value is lowest score so far.
# It seems like a lot of work, so I would only do that if the naive/brute force solution doesn't work.

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

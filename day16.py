DEBUG = print if False else lambda *s: None

import re

_ = lambda: None

class Endpoints:
    def __init__(self):
        self._ = None
        pass

    def __str__(self):
        return f''


v = 0
pat = re.compile(r'^Valve (..)[^=]*=([0-9]*);.*valves? (.*)$')
with open('input16', 'r') as file:
    for line in file:
        mat = pat.match(line)
        print(mat)

print(f'Part A: {0}')
print(f'Part B: {0}')

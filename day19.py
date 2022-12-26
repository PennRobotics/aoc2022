DEBUG = print if True else lambda *s: None

import math
import re

#with open('sample19', 'r') as file:
with open('input19', 'r') as file:
    blueprints = [map(int, re.findall(r'\d+', l)) for l in file.read().rstrip('\n').split('\n')]

blueprints = [blueprints[0]]  # TODO-debug

t_to_build = lambda cost, cur, rate: math.ceil((cost-cur)/rate)

def search(t, o, c, x, g, r1, r2, r3, r4):
    DEBUG(t, o, c, x, g, r1, r2, r3, r4)
    if t >= 24:
        return g
    if x >= cx4 and o >= co4:  # Geode
        o -= co4
        x -= cx4
        bt = max(t_to_build(cx4, x, r3), t_to_build(co4, o, r1))
        t = t + bt
        o += r1 * bt
        c += r2 * bt
        x += r3 * bt
        g += r4 * bt
        search(t + bt, o, c, x, g, r1, r2, r3, r4+1)
    if c >= cc3 and o >= co3 and r3 < cx4:  # Obsidian
        o -= co3
        c -= cc3
        bt = max(t_to_build(cc3, c, r2), t_to_build(co3, o, r1))
        t = t + bt
        o += r1 * bt
        c += r2 * bt
        x += r3 * bt
        g += r4 * bt
        search(t + bt, o, c, x, g, r1, r2, r3+1, r4)
    if o >= co2 and r2 < cc3:  # Clay
        o -= co2
        bt = t_to_build(co2, o, r1)
        t = t + bt
        o += r1 * bt
        c += r2 * bt
        x += r3 * bt
        g += r4 * bt
        search(t + bt, o, c, x, g, r1, r2+1, r3, r4)
    if r1 < max(co1, co2, co3, co4):  # Saturation (cannot create more than one bot per turn for any material)
        bt = t_to_build(co1, o, r1)
        search(t + bt, o+r1*bt-co1, c+r2*bt, x+r3*bt, g+r4*bt, r1+1, r2, r3, r4)


quality_level = 0
for b, co1, co2, co3, cc3, co4, cx4 in blueprints:
    o, c, x, g, r1, r2, r3, r4 = 0, 0, 0, 0, 1, 0, 0, 0
    t = 0
    search(t, o, c, x, g, r1, r2, r3, r4)

print(f'Part A: {0}')
print(f'Part B: {0}')

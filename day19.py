DEBUG = print if True else lambda *s: None

import math
import re

NOTHING        = 0
ORE_ROBOT      = 1
CLAY_ROBOT     = 2
OBSIDIAN_ROBOT = 4
GEODE_ROBOT    = 8

#with open('sample19', 'r') as file:
with open('input19', 'r') as file:
    blueprints = [map(int, re.findall(r'\d+', l)) for l in file.read().rstrip('\n').split('\n')]

blueprints = [blueprints[0]]  # TODO-debug

t_to_build = lambda cost, cur, rate: math.ceil((cost-cur)/rate)

def search(state):
    if t >= 24:
        return state[4]
    if x >= cx4 and o >= co4:  # Geode
        state[8] += 1
        state[1] -= co4
        state[3] -= cx4
        bt = max(t_to_build(cx4, x, r3), t_to_build(co4, o, r1))
    elif c >= cc3 and o >= co3 and r3 < cx4:  # Obsidian
        state[7] += 1
        state[1] -= co3
        state[2] -= cc3
        bt = max(t_to_build(cc3, c, r2), t_to_build(co3, o, r1))
    elif o >= co2 and r2 < cc3:  # Clay
        state[6] += 1
        state[1] -= co2
        bt = t_to_build(co2, o, r1)
    else:  # Ore
        if o >= co1 and r1 < max(co1, co2, co3, co4):  # Saturation (cannot create more than one bot per turn for any material)
            state[5] += 1
            state[1] -= co1
            bt = t_to_build(co1, o, r1)
    bt = 0  # TODO: bt needs to be properly assigned. rethink if-elif-else order!

    state[0] = t + bt
    state[1] += r1 * bt
    state[2] += r2 * bt
    state[3] += r3 * bt
    state[4] += r4 * bt

    search(state)

quality_level = 0
for b, co1, co2, co3, cc3, co4, cx4 in blueprints:
    o, c, x, g, r1, r2, r3, r4 = 0, 0, 0, 0, 1, 0, 0, 0
    t = 0
    state = [t, o, c, x, g, r1, r2, r3, r4]
    search(state)

print(f'Part A: {0}')
print(f'Part B: {0}')

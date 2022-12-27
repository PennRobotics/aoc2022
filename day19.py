DEBUG = print if True else lambda *s: None

import math
import re

#with open('sample19', 'r') as file:
with open('input19', 'r') as file:
    blueprints = [map(int, re.findall(r'\d+', l)) for l in file.read().rstrip('\n').split('\n')]

t_to_build = lambda cost, cur, rate: max(1, math.ceil((cost-cur)/rate))

def search(t, o, c, x, g, r1, r2, r3, r4, minutes):
    global max_g
    #DEBUG(t, o, c, x, g, r1, r2, r3, r4)
    if t == minutes:
        if g > max_g:
            max_g = g
        return g
    if t > minutes:
        return
    if r3:  # Geode
        bt = max(t_to_build(cx4, x, r3), t_to_build(co4, o, r1))
        search(t + bt, o+r1*bt-co4, c+r2*bt, x+r3*bt-cx4, g+r4*bt, r1, r2, r3, r4+1, minutes)
    if r2:  # Obsidian
        bt = max(t_to_build(cc3, c, r2), t_to_build(co3, o, r1))
        search(t + bt, o+r1*bt-co3, c+r2*bt-cc3, x+r3*bt, g+r4*bt, r1, r2, r3+1, r4, minutes)
    if r2 < cc3:  # Clay
        bt = t_to_build(co2, o, r1)
        search(t + bt, o+r1*bt-co2, c+r2*bt, x+r3*bt, g+r4*bt, r1, r2+1, r3, r4, minutes)
    if r1 < max(co2, co3, co4):  # Saturation (cannot create more than one bot per turn for any material)
        bt = t_to_build(co1, o, r1)
        search(t + bt, o+r1*bt-co1, c+r2*bt, x+r3*bt, g+r4*bt, r1+1, r2, r3, r4, minutes)
    return max_g


max_g = None
quality_level = 0
for b, co1, co2, co3, cc3, co4, cx4 in blueprints:
    o, c, x, g, r1, r2, r3, r4 = 0, 0, 0, 0, 1, 0, 0, 0
    t = 0
    max_g = 0
    search(t, o, c, x, g, r1, r2, r3, r4, 23)
    quality_level += b * max_g

print(f'Part A: {quality_level}')

quality_level = 0
for b, co1, co2, co3, cc3, co4, cx4 in blueprints[:3]:
    o, c, x, g, r1, r2, r3, r4 = 0, 0, 0, 0, 1, 0, 0, 0
    t = 0
    max_g = 0
    search(t, o, c, x, g, r1, r2, r3, r4, 31)
    quality_level += b * max_g

print(f'Part B: {quality_level}')

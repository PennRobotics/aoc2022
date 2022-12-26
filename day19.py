DEBUG = print if True else lambda *s: None

import re
from copy import copy

NOTHING        = 0
ORE_ROBOT      = 1
CLAY_ROBOT     = 2
OBSIDIAN_ROBOT = 4
GEODE_ROBOT    = 8

#with open('sample19', 'r') as file:
with open('input19', 'r') as file:
    blueprints = [map(int, re.findall(r'\d+', l)) for l in file.read().rstrip('\n').split('\n')]

blueprints = [blueprints[0]]  # TODO-debug

t_to_build = lambda cost, cur, rate: (cost-cur)//rate  # TODO: this should be ceil and not floor

quality_level = 0
for b, co1, co2, co3, cc3, co4, cx4 in blueprints:
    o, c, x, g, r1, r2, r3, r4 = 0, 0, 0, 0, 1, 0, 0, 0
    t = 0
    possible_states = [[t, o, c, x, g, r1, r2, r3, r4]]
    for state in possible_states:  # t, o, c, x, g, r1, r2, r3, r4 = state
        if t >= 24:
            break

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

        possible_states = [state] + possible_states

    # TODO: check if the candidate state is feasible (can a geode robot be build by 23m?) or even optimal (how many geode robots COULD be built given a set of inputs?)
    # TODO: choose top state, go to next blueprint
    # TODO: if it's easy to check and time permits, get min and max bounds for ore and clay, figure out if there's a predictable ratio between each type of material, etc.

            #DEBUG(possible_states)
            #DEBUG('\n'.join([', '.join([str(e) for e in v]) for v in possible_states]))

            #best_state = possible_states[0]
            #for examined_state in possible_states:
                #score = 0
                #best_state = state if score > best_score else best_state
                #best_score = score if score > best_score else best_score
        DEBUG('')
        #possible_states += new_states  # TODO: switch from BFS to DFS
        DEBUG(f' ... {possible_states}')
    print(possible_states)
    print('  <>  '.join(list(map(lambda f:str(f[5]), possible_states))))

print(f'Part A: {0}')
print(f'Part B: {0}')

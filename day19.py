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

quality_level = 0
for b, co1, co2, co3, cc3, co4, cx4 in blueprints:
    o, c, x, g, r1, r2, r3, r4 = 0, 0, 0, 0, 1, 0, 0, 0
    t = 0
    possible_states = [[t, o, c, x, g, r1, r2, r3, r4]]
    while t < 24:
        DEBUG(f'== Minute {t} ==', flush=True)

        new_states = []
        for ostate in possible_states:
            state = copy(ostate)
            _, o, c, x, g, r1, r2, r3, r4 = state
            state[0] = t

            make_r = 0
            if True and o >= co1:  # TODO: conditions for building ore
                DEBUG(f'Spend {co1} ore to start building an ore-collecting robot.')
                o -= co1
                state[1] -= co1
                make_r = 1
            elif True and o >= co2:  # TODO ...
                DEBUG(f'Spend {co2} ore to start building a clay-collecting robot.')
                o -= co2
                state[1] -= co2
                make_r = 2
            elif True and o >= co3 and c >= cc3:
                DEBUG(f'Spend {co3} ore and {cc3} clay to start building an obsidian-collecting robot.')
                o -= co3
                state[1] -= co3
                c -= cc3
                state[2] -= cc3
                make_r = 3
            elif True and o >= co4 and x >= cx4:
                DEBUG(f'Spend {co4} ore and {cx4} obsidian to start building a geode-cracking robot.')
                o -= co4
                state[1] -= co4
                x -= cx4
                state[3] -= cx4
                make_r = 4

            state[1] += r1
            state[2] += r2
            state[3] += r3
            state[4] += r4

            DEBUG(f'{r1} ore-collecting robot{"s" if r1 > 1 else ""} collect{"s" if r1 == 1 else ""} {r1} ore; you now have {state[1]} ore.')
            if r2:
                DEBUG(f'{r2} clay-collecting robot{"s" if r2 > 1 else ""} collect{"s" if r2 == 1 else ""} {r2} clay; you now have {state[2]} clay.')
            if r3:
                DEBUG(f'{r3} obsidian-collecting robot{"s" if r3 > 1 else ""} collect{"s" if r3 == 1 else ""} {r3} obsidian; you now have {state[3]} obsidian.')
            if r4:
                s, ns = ('s', '') if r4 > 1 else ('', 's')
                sss = 's' if state[4] > 1 else ''
                DEBUG(f'{r4} geode-cracking robot{s} crack{ns} {r4} geode{s}; you now have {state[4]} open geode{sss}.')

            if make_r:
                state[make_r + 4] += 1
                r_type = 'ore-collecting' if make_r == 1 else 'clay-collecting' if make_r == 2 else 'obsidian-collecting' if make_r == 3 else 'geode-cracking'
                DEBUG(f'The new {r_type} robot is ready; you now have {state[make_r + 4]} of them.')

            if co1 > co2:
                DEBUG('!!')
                if o >= co1 and r1 < max(co1, co2, co3, co4):  # Saturation (cannot create more than one bot per turn for any material)
                    DEBUG('??')
                    #new_state = copy(state)
                    #new_state[1] = ORE_ROBOT  # TODO: move construction decision (from above) here or vice versa (e.g. combine these sections)
                    #if new_state not in possible_states:
                        #new_states.append(new_state)
            if o >= co2 and r2 < cc3:  # Saturation
                #new_state = copy(state)
                #new_state[1] = CLAY_ROBOT
                #if new_state not in possible_states:
                    #new_states.append(new_state)
                pass
            if co1 <= co2:
                if o >= co1 and r1 < max(co1, co2, co3, co4):  # Saturation (cannot create more than one bot per turn for any material)
                    pass
                    #new_state = copy(state)
                    #new_state[1] = ORE_ROBOT
                    #if new_state not in possible_states:
                        #new_states.append(new_state)
            if c >= cc3 and o >= co3 and r3 < cx4:
                pass
                #new_state = copy(state)
                #new_state[1] = OBSIDIAN_ROBOT  # Greedy-ish creation of obsidian
                #if new_state not in possible_states:
                    #new_states.append(new_state)
            #new_state = copy(state)
            if x >= cx4 and o >= co4:
                pass #new_state[1] = GEODE_ROBOT  # Greedy creation of geodes
            else:
                pass #new_state[1] = NOTHING
            #if new_state not in possible_states:
                #new_states.append(new_state)

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

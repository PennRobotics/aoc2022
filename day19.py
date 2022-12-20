DEBUG = print if True else lambda *s: None

import re
from copy import copy

NOTHING        = 0
ORE_ROBOT      = 1
CLAY_ROBOT     = 2
OBSIDIAN_ROBOT = 4
GEODE_ROBOT    = 8

MAX_MINUTE = 5  # TODO

with open('sample19', 'r') as file:
#with open('input19', 'r') as file:
    blueprints = [map(int, re.findall(r'\d+', l)) for l in file.read().rstrip('\n').split('\n')]

blueprints = [blueprints[0]]  # TODO-debug

quality_level = 0
for bid, cost_o_r1, cost_o_r2, cost_o_r3, cost_c_r3, cost_o_r4, cost_x_r4 in blueprints:
    job, num_o, num_c, num_x, num_g, num_r1, num_r2, num_r3, num_r4, path = NOTHING, 0, 0, 0, 0, 1, 0, 0, 0, []
    possible_states = [[0, job, num_o, num_c, num_x, num_g, num_r1, num_r2, num_r3, num_r4, path]]
    for minute in range(1, MAX_MINUTE+1):
        print(len(possible_states),minute,flush=True)
        DEBUG(f'== Minute {minute} ==', flush=True)

        for i, st in enumerate(possible_states):
            DEBUG('> ', i, st)
            if st[0] < minute:
                continue
            del possible_states[:i]

        new_states = []
        for ostate in possible_states:
            state = copy(ostate)
            _, job, num_o, num_c, num_x, num_g, num_r1, num_r2, num_r3, num_r4, opath = state
            path = copy(opath)
            state[0] = minute

            make_r = 0
            DEBUG(job == ORE_ROBOT)
            if job == ORE_ROBOT and num_o >= cost_o_r1:
                DEBUG(f'Spend {cost_o_r1} ore to start building an ore-collecting robot.')
                num_o -= cost_o_r1
                state[2] -= cost_o_r1
                make_r = 1
            elif job == CLAY_ROBOT and num_o >= cost_o_r2:
                DEBUG(f'Spend {cost_o_r2} ore to start building a clay-collecting robot.')
                num_o -= cost_o_r2
                state[2] -= cost_o_r2
                make_r = 2
            elif job == OBSIDIAN_ROBOT and num_o >= cost_o_r3 and num_c >= cost_c_r3:
                DEBUG(f'Spend {cost_o_r3} ore and {cost_c_r3} clay to start building an obsidian-collecting robot.')
                num_o -= cost_o_r3
                state[2] -= cost_o_r3
                num_c -= cost_c_r3
                state[3] -= cost_c_r3
                make_r = 3
            elif job == GEODE_ROBOT and num_o >= cost_o_r4 and num_x >= cost_x_r4:
                DEBUG(f'Spend {cost_o_r4} ore and {cost_x_r4} obsidian to start building a geode-cracking robot.')
                num_o -= cost_o_r4
                state[2] -= cost_o_r4
                num_x -= cost_x_r4
                state[4] -= cost_x_r4
                make_r = 4

            state[2] += num_r1
            state[3] += num_r2
            state[4] += num_r3
            state[5] += num_r4

            DEBUG(f'{num_r1} ore-collecting robot{"s" if num_r1 > 1 else ""} collect{"s" if num_r1 == 1 else ""} {num_r1} ore; you now have {state[2]} ore.')
            if num_r2:
                DEBUG(f'{num_r2} clay-collecting robot{"s" if num_r2 > 1 else ""} collect{"s" if num_r2 == 1 else ""} {num_r2} clay; you now have {state[3]} clay.')
            if num_r3:
                DEBUG(f'{num_r3} obsidian-collecting robot{"s" if num_r3 > 1 else ""} collect{"s" if num_r3 == 1 else ""} {num_r3} obsidian; you now have {state[4]} obsidian.')
            if num_r4:
                s, ns = ('s', '') if num_r4 > 1 else ('', 's')
                sss = 's' if state[4] > 1 else ''
                DEBUG(f'{num_r4} geode-cracking robot{s} crack{ns} {num_r4} geode{s}; you now have {state[4]} open geode{sss}.')

            if make_r:
                state[make_r + 5] += 1
                r_type = 'ore-collecting' if make_r == 1 else 'clay-collecting' if make_r == 2 else 'obsidian-collecting' if make_r == 3 else 'geode-cracking'
                DEBUG(f'The new {r_type} robot is ready; you now have {state[make_r + 5]} of them.')

            if cost_o_r1 > cost_o_r2:
                DEBUG('!!')
                if num_o >= cost_o_r1 and num_r1 < max(cost_o_r1, cost_o_r2, cost_o_r3, cost_o_r4):  # Saturation (cannot create more than one bot per turn for any material)
                    DEBUG('??')
                    new_state = copy(state)
                    new_state[1] = ORE_ROBOT
                    new_state[10] = path + [ORE_ROBOT]
                    if new_state not in possible_states:
                        new_states.append(new_state)
            if num_o >= cost_o_r2 and num_r2 < cost_c_r3:  # Saturation
                new_state = copy(state)
                new_state[1] = CLAY_ROBOT
                new_state[10] = path + [CLAY_ROBOT]
                if new_state not in possible_states:
                    new_states.append(new_state)
            if cost_o_r1 <= cost_o_r2:
                if num_o >= cost_o_r1 and num_r1 < max(cost_o_r1, cost_o_r2, cost_o_r3, cost_o_r4):  # Saturation (cannot create more than one bot per turn for any material)
                    new_state = copy(state)
                    new_state[1] = ORE_ROBOT
                    new_state[10] = path + [ORE_ROBOT]
                    if new_state not in possible_states:
                        new_states.append(new_state)
            if num_c >= cost_c_r3 and num_o >= cost_o_r3 and num_r3 < cost_x_r4:
                new_state = copy(state)
                new_state[1] = OBSIDIAN_ROBOT  # Greedy-ish creation of obsidian
                new_state[10] = path + [OBSIDIAN_ROBOT]
                if new_state not in possible_states:
                    new_states.append(new_state)
            new_state = copy(state)
            if num_x >= cost_x_r4 and num_o >= cost_o_r4:
                new_state[1] = GEODE_ROBOT  # Greedy creation of geodes
                new_state[10] = path + [GEODE_ROBOT]
            else:
                new_state[1] = NOTHING
                new_state[10] = path + [NOTHING]
            if new_state not in possible_states:
                new_states.append(new_state)

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
        possible_states += new_states
        DEBUG(f' ... {possible_states}')
    print(possible_states)
    print('  <>  '.join(list(map(lambda f:str(f[5]), possible_states))))

print(f'Part A: {0}')
print(f'Part B: {0}')

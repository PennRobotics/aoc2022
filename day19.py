DEBUG = print if True else lambda *s: None

import re
from copy import copy

NOTHING        = 0
ORE_ROBOT      = 1
CLAY_ROBOT     = 2
OBSIDIAN_ROBOT = 4
GEODE_ROBOT    = 8

MAX_MINUTE = 24  # TODO

with open('sample19', 'r') as file:
#with open('input19', 'r') as file:
    blueprints = [map(int, re.findall(r'\d+', l)) for l in file.read().rstrip('\n').split('\n')]

blueprints = [blueprints[0]]  # TODO-debug

quality_level = 0
for bid, cost_o_r1, cost_o_r2, cost_o_r3, cost_c_r3, cost_o_r4, cost_x_r4 in blueprints:
    job, num_o, num_c, num_x, num_g, num_r1, num_r2, num_r3, num_r4, path = NOTHING, 0, 0, 0, 0, 1, 0, 0, 0, []
    possible_states = [[0, job, num_o, num_c, num_x, num_g, num_r1, num_r2, num_r3, num_r4, path]]
    for minute in range(1, MAX_MINUTE+1):
        DEBUG(f'== Minute {minute} ==', flush=True)

        # max_ore_robots = 1 + first_criteria + second_criteria + third_criteria (saturated, divide remaining minutes by num of robots)
        # max_clay_robots = first_criteria + second_criteria + ... (worst case is eleven for blueprint 24, saturation here is 10)
        # max_geode_robots = some sort of triangle number thing, or (absolute most naive) ~21 minus fib number leading to x obsidian
        # max_obsidian_robots = should be able to back out the earliest robot using previous two, enumerate all cases and test individually

        for i, st in enumerate(possible_states):
            DEBUG('> ',i,st)
            if st[0] < minute - 1:
                continue
            del possible_states[:i]

        new_states = []
        for ostate in sorted(possible_states):
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
                    new_states.append(new_state)
            if num_o >= cost_o_r2 and num_r2 < cost_c_r3:  # Saturation
                new_state = copy(state)
                new_state[1] = CLAY_ROBOT
                new_state[10] = path + [CLAY_ROBOT]
                new_states.append(new_state)
            if cost_o_r1 <= cost_o_r2:
                if num_o >= cost_o_r1 and num_r1 < max(cost_o_r1, cost_o_r2, cost_o_r3, cost_o_r4):  # Saturation (cannot create more than one bot per turn for any material)
                    new_state = copy(state)
                    new_state[1] = ORE_ROBOT
                    new_state[10] = path + [ORE_ROBOT]
                    new_states.append(new_state)
            new_state = copy(state)
            if num_x >= cost_x_r4 and num_o >= cost_o_r4:
                new_state[1] = GEODE_ROBOT  # Greedy creation of geodes
                new_state[10] = path + [GEODE_ROBOT]
            elif num_c >= cost_c_r3 and num_o >= cost_o_r3 and num_r3 < cost_x_r4:
                new_state[1] = OBSIDIAN_ROBOT  # Greedy creation of obsidian
                new_state[10] = path + [OBSIDIAN_ROBOT]
            else:
                new_state[1] = NOTHING
                new_state[10] = path + [NOTHING]
            new_states.append(new_state)

    # TODO: add candidate states for each type of build option (nothing or robot)
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

print(f'Part A: {0}')
print(f'Part B: {0}')

# Hand calculation of #2:  (seemingly low-production case)
'''
build 2 ore bots, clay almost every turn (6)
build 10 clay (18)
obs almost every turn
basically 1 geode bot, if that, and certainly late

OR

build 1 ore bot, clay every other turn (3)
build 7 clay (17)
obs every other turn
maybe 2 geode bots? maybe even still zero?

1 robot = 2 ore + 16 obsidian = 2 ore + 16*(4 ore + 14 clay) = 64 ore + 224*(4 ore) = 960 ore-equivalent

16 obsidian is 1+1+2+2+3+3+4 (obs every other turn), obs 1+2+3+4+4 clay,

Trying again:
after 4, 2b. After 6, 3b. After 8, 4b., After 12, 4c. After 13, 1x, @14,5c,@15,6c,@17,7c/2x,@19,3x,@22 maybe a geode bot

'''

# Hand calculation of #24:  (seemingly high-production case)
'''
build new ore robot, clay robots can be built every turn (3)
with 5 clay robots, an obs robot can be built every other turn (8)
a surplus of ore will build (avg 1 per turn)
in the between turns, one of the others could be built and might help production
with 4 obs robots, a geode robot should be buildable every 3 turns (16)
1 geode somewhere between 13 and 15 (
2 around 17
3 around 20
4 around 23 [3+6+9+4 = 22 hopefully, and probably a few more]
'''
